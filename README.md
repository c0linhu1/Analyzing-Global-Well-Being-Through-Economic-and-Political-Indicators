# Analyzing Global Well-Being Through Economic and Political Indicators

## 📊 Project Overview
A group data science project that analyzes the relationship between economic factors and political well-being using World Bank development indicators and machine learning models such as linear regression, polynomial regression, and K-Nearest Neighbors. We use these machine learning models and see which is the best model when predicting Voice & Accountability scores (VA.EST) based off of the three economic indicators of GDP per Capita (NY.GDP.PCAP.CD), Military expenditure (% of GDP) (MS.MIL.XPND.GD.ZS), and Total Population (SP.POP.TOTL)

### Key Questions
- How do economic indicators correlate with political voice and accountability?
- Which machine learning model best predicts governance quality from economic data?
- Is there a correlation between economic/political indicators and predicted region?

## 🎯 Features

- **Multi-model Machine Learning**: Implementation of Linear Regression, Polynomial Regression, and KNN algorithms
- **World Bank API Integration**: Direct data retrieval from World Bank indicators
- **Visualization Suite**: Custom plots for model performance, feature importance, and regional trends
- **Reproducible Pipeline**: Modular code structure for data preparation, analysis, and visualization


## 📈 Machine Learning Models

### Linear Regression
- Baseline model using economic indicators as features
- Manual implementation using Normal Equation
- Provides interpretable coefficients for each feature

### Polynomial Regression
- Captures non-linear relationships between features and target
- Degree selection based on cross-validation
- Balances model complexity with prediction accuracy

### K-Nearest Neighbors (KNN)
- Non-parametric approach for comparison
- Distance-based predictions using feature similarity
- K value optimized through grid search

### Model Evaluation
- **Metrics**: R², MSE
- **Visualization**
    - Scatterplot of Residuals vs Order (independence)
    - Scatterplot of Residuals vs Fitted (homoscedasticity)
    - Q-Q Plot (Normality)
    - Histogram of Residuals (Normality)

## World Bank Indicators Used

- **GDP per capita** (NY.GDP.PCAP.CD)
- **Military expenditure (% of GDP)** (MS.MIL.XPND.GD.ZS)
- **Total Population** (SP.POP.TOTL)
- **Voice and Accountability** (Target variable - governance indicator) (VA.EST)
- Additional economic and social indicators were incorporated when originally cleaning the data but 
  could not be incorporated in the ml models due to the amount of null values 

## 🔍 Key Findings
- 
- More shown in Final Report 
- All visualization shown in Final Report as well as Jupyter Notebooks

## 👥 Contributors

- **Colin Hui** - [@c0linhu1](https://github.com/c0linhu1)
- **Derek Aslan** - [@WiseHunter42](https://github.com/WiseHunter42)
- **Aydan Ali** - [@aydanali](https://github.com/aydanali)
- **Conor Cummings** 