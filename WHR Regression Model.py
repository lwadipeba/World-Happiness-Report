import statsmodels.api as sm
import pandas as pd
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
df = pd.read_csv("WHR2023.csv")

#checking for null values
df.isnull().sum()

#defining the dependent and independent variables
X = df[[
    'gdp_per_capita',
    'social_support',
    'healthy_life_expectancy',
    'freedom_to_make_life_choices',
    'generosity',
    'perceptions_of_corruption',
    'DEurope*',
    'DAmericas*',
    'DAsia*'
]]

y = df['happiness_score']

#Adding constant term (intercept)
X = sm.add_constant(X)

#Fit the regression model
model = sm.OLS(y, X).fit(cov_type='HC3')

#Print the summary for full regression model
print(model.summary())

# ----Plotting actual happiness scores vs predicted scores----
df['predicted_happiness'] = model.predict(X)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['happiness_score'], y=df['predicted_happiness'])
plt.plot([df['happiness_score'].min(), df['happiness_score'].max()],
         [df['happiness_score'].min(), df['happiness_score'].max()],
         color='red', linestyle='--')  # Reference line
plt.xlabel('Actual Happiness Score')
plt.ylabel('Predicted Happiness Score')
plt.title('Actual vs Predicted Happiness Score')
plt.grid(True)
plt.show()

#----Simple Regression----
X_sample = df[['gdp_per_capita']]
X_sample = sm.add_constant(X_sample) #constant term
sample_model = sm.OLS(y, X_sample).fit(cov_type='HC3') #fit the model
print(sample_model.summary())

# ----Hypothesis Testing-----
#Creating a restricted model
X_restricted = df[[
    'gdp_per_capita',
    'healthy_life_expectancy',
    'freedom_to_make_life_choices',
    'perceptions_of_corruption',
    'DEurope*',
    'DAmericas*',
    'DAsia*'
]]
X_restricted = sm.add_constant(X_restricted)
restricted_model = sm.OLS(y, X_restricted).fit(cov_type='HC3')

#retreiving values for formula
r2_ur = model.rsquared
r2_r = restricted_model.rsquared
n = 137           # number of observations
k = 9     # number of independent variable
q = 2         # number of restrictions

# Plug into formula
numerator = (r2_ur - r2_r) / q
denominator = (1 - r2_ur) / (n - k - 1)
f_stat = numerator / denominator

#Generating critical F
from scipy.stats import f

# Set parameters
alpha = 0.05

# Calculate critical F-value
f_crit = f.ppf(1 - alpha, q, n-k-1)

print('F-stat:', f_stat)
print('F-crit:', f_crit)


#-----Breusch-Pagan test-----
from statsmodels.stats.diagnostic import het_breuschpagan
residuals = model.resid
bp_test = het_breuschpagan(residuals, model.model.exog)
bp_stat, p_value, f_stat, f_p_value = bp_test
print("Breusch-Pagan Test Statistic:", bp_stat)
print("p-value:",p_value)
print("F-statistic:",f_stat)
print("F p-value:",f_p_value)

#-----VIF scores----
from statsmodels.stats.outliers_influence import variance_inflation_factor
vif_data = pd.DataFrame()
vif_data["Variable"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif_data)


