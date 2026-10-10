# World Happiness Report 2023: Regression Analysis

## Overview

This project uses multiple linear regression to examine how economic,
social, health, and regional factors are associated with country-level
happiness scores in a 2023 World Happiness dataset. The analysis was
completed for ECON 318 and uses Python statistical modeling tools to
estimate regression models and evaluate common model diagnostics.

## Research Question

How are GDP per capita, social support, healthy life expectancy, freedom
to make life choices, generosity, perceptions of corruption, and
regional indicators associated with a country's happiness score?

## Dataset

The dataset, `WHR2023_Econ318.csv`, contains **137 observations and 12
columns**. It includes country and region information, the happiness
score, six explanatory variables, and three regional indicator
variables.

Variables used in the analysis:

-   **Outcome variable:** `happiness_score`
-   **Explanatory variables:** `gdp_per_capita`, `social_support`,
    `healthy_life_expectancy`, `freedom_to_make_life_choices`,
    `generosity`, and `perceptions_of_corruption`
-   **Regional indicators:** `DEurope*`, `DAmericas*`, and `DAsia*`

The dataset file is included separately in this repository. Please
retain the original data attribution and check the dataset's licensing
or usage terms before redistributing it.

## Methods

The Python script performs the following analyses:

1.  **Data check:** Checks the dataset for missing values.
2.  **Multiple linear regression:** Estimates an OLS model using the six
    explanatory variables and three regional indicators, with HC3
    heteroskedasticity-robust covariance estimates.
3.  **Actual vs. predicted visualization:** Plots observed happiness
    scores against model-predicted scores and includes a 45-degree
    reference line.
4.  **Simple regression:** Estimates a separate OLS model using GDP per
    capita as the only explanatory variable, also with HC3 robust
    covariance estimates.
5.  **Restricted-model comparison:** Fits a restricted model that omits
    social support and generosity, then calculates an F-statistic using
    the models' R-squared values.
6.  **Heteroskedasticity diagnostic:** Runs the Breusch--Pagan test.
7.  **Multicollinearity diagnostic:** Calculates variance inflation
    factors (VIFs) for the regressors.

## Tools and Libraries

-   Python
-   pandas and NumPy
-   statsmodels
-   scikit-learn
-   Matplotlib
-   Seaborn
-   SciPy

## How to Run

1.  Install Python 3.

2.  Install the libraries used in the script:

    ``` bash
    pip install pandas numpy statsmodels scikit-learn matplotlib seaborn scipy
    ```

3.  Keep `WHR2023.csv` in the same directory as the Python
    script.

4.  Run the script:

    ``` bash
    python "WHR Regression Model.py"
    ```

The script prints regression summaries and diagnostic results to the
console and displays the actual-versus-predicted plot.

## Interpreting the Results

Use the regression coefficients and p-values to assess the direction and
statistical evidence of associations between the explanatory variables
and happiness scores. The actual-versus-predicted plot provides a visual
check of model fit. The Breusch--Pagan test assesses evidence of
heteroskedasticity, while VIF values help identify potential
multicollinearity.


## Limitations

-   The analysis is observational and identifies associations, not
    necessarily causal effects.
-   The dataset contains 137 observations, so conclusions should be
    interpreted with appropriate caution.
-   The script assumes the CSV file is available at the specified
    relative path.
-   The regional indicator variables and the omitted reference region
    should be clearly documented when interpreting regional
    coefficients.
