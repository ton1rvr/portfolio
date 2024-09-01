# Data Scientist

#### Technical Skills: Python, SQL, AWS, Snowflake, MATLAB

## Education
- Ph.D., Physics | The University of Texas at Dallas (_May 2022_)								       		
- M.S., Physics	| The University of Texas at Dallas (_December 2019_)	 			        		
- B.S., Physics | The University of Texas at Dallas (_May 2017_)

## Work Experience
**Data Scientist @ Toyota Financial Services (_June 2022 - Present_)**
- Uncovered and corrected missing step in production data pipeline which impacted over 70% of active accounts
- Redeveloped loan originations model which resulted in 50% improvement in model performance and saving 1 million dollars in potential losses

**Data Science Consultant @ Shawhin Talebi Ventures LLC (_December 2020 - Present_)**
- Conducted data collection, processing, and analysis for novel study evaluating the impact of over 300 biometrics variables on human performance in hyper-realistic, live-fire training scenarios
- Applied unsupervised deep learning approaches to longitudinal ICU data to discover novel sepsis sub-phenotypes

## Projects
## 📊 My Data Analysis Portfolio 📊

### Introduction

This repository contains a collection of projects that demonstrate my expertise in data science, machine learning, and data visualization. Each project focuses on solving a real-world problem, showcasing my ability to handle complex datasets, develop predictive models, and generate meaningful insights. 
Below, you will find an overview of each project.

---

### Project 1. [Heart Attack Prediction Project](https://github.com/ton1rvr/portfolio/tree/07d5fa29fe8bedf42a502b5657f44f53c12fa21a/Project%201%20-%20Heart%20Attack%20Prediction%20(ML%20w%3A%20python))

**Objective:** The goal of this project is to develop a predictive model that can determine whether an individual is likely to experience a heart attack based on various health indicators.

- **Data:** The dataset includes features such as age, cholesterol levels, resting blood pressure, maximum heart rate achieved (`thalachh`), and others. The target variable (`output`) indicates whether the individual had a heart attack (1) or is healthy (0).
- **Techniques:**
  - **Correlation Analysis:** Explored relationships between variables, such as age and `thalachh`, identifying a moderate negative correlation.
  - **Principal Component Analysis (PCA):** Reduced dimensionality to highlight the most significant features influencing heart attack prediction.
  - **Linear Discriminant Analysis (LDA):** Used to find the linear combinations of features that best separate healthy individuals from those who had a heart attack.
  - **Support Vector Machine (SVM):** Applied both linear and non-linear kernels, with the non-linear SVM showing superior performance.
  - **Neural Networks:** Implemented to explore deeper patterns in the data, with a focus on avoiding overfitting.
- **Results:**
  - **Best Model:** The non-linear SVM achieved the highest accuracy at 92.1%.
  - **Insights:** While neural networks showed potential, they also posed a risk of overfitting, particularly with more complex architectures.
- **Visualizations:** Scatter plots, PCA explained variance, decision boundaries for SVM, and model performance charts.
- **Conclusion:** The project illustrates the application of various machine learning techniques in medical diagnostics, with the non-linear SVM model offering the best balance between accuracy and generalizability.

**How to Run:**
1. Clone the repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the Jupyter notebooks to perform the analysis.

---

### Project 2. [SMS Spam Filter Project](https://github.com/ton1rvr/portfolio/tree/07d5fa29fe8bedf42a502b5657f44f53c12fa21a/Project%202%20-%20SMS%20Spam%20Filter%20(NLP%20w%3A%20python))

**Objective:** This project aims to build an efficient SMS spam filter using natural language processing (NLP) and machine learning techniques.

- **Data:** The SMS Spam Collection dataset, which consists of 5,572 SMS messages labeled as spam (747 messages) or ham (4,825 messages).
- **Techniques:**
  - **Text Preprocessing:** Cleaned and prepared the text data by removing punctuation, converting to lowercase, and tokenizing words.
  - **TF-IDF Vectorization:** Converted text into numerical features using Term Frequency-Inverse Document Frequency, capturing the importance of words in each message.
  - **Modeling:** Tested several classifiers, including Logistic Regression, Naive Bayes, Support Vector Machine (SVM), and Random Forest.
- **Results:**
  - **Best Model:** The Naive Bayes classifier provided the highest accuracy, particularly excelling in identifying spam messages with an impressive F1-score.
  - **Confusion Matrix:** Displayed the model's performance, showing strong precision and recall for the spam class.
- **Visualizations:** Word clouds for common spam and ham terms, performance metrics for each model, and confusion matrices.
- **Conclusion:** The Naive Bayes model proved to be the most effective for this classification task, offering a good balance of speed and accuracy for text-based spam detection.

**How to Run:**
1. Clone the repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the notebook `sms_spam_filter.ipynb` to see the full process from data preprocessing to model evaluation.

---

### Project 3. [NBA Salary Prediction Using Multiple Regression](https://github.com/ton1rvr/portfolio/tree/07d5fa29fe8bedf42a502b5657f44f53c12fa21a/Project%203%20-%20NBA%20Salary%20Prediction%20(Multiple%20Reg%20w%3A%20R))

**Objective:** The goal of this project is to predict NBA player salaries based on performance metrics and other attributes using multiple regression models.

- **Data:** The dataset contains player statistics such as Points Per Game (PPG), Assists Per Game (APG), Rebounds Per Game (RPG), and corresponding salaries.
- **Techniques:**
  - **Data Preprocessing:** Handled missing values, encoded categorical variables (like player positions), and scaled features to prepare the data for modeling.
  - **Modeling:** Implemented and compared several regression techniques:
    - **Linear Regression:** Used as a baseline model to predict salaries.
    - **Ridge Regression:** Applied L2 regularization to handle multicollinearity.
    - **Lasso Regression:** Employed L1 regularization to perform feature selection.
    - **ElasticNet Regression:** Combined both L1 and L2 regularization to balance feature selection and model complexity.
- **Results:**
  - **Best Model:** Ridge Regression outperformed others, achieving the best R-squared score while minimizing RMSE.
  - **Feature Importance:** Lasso regression highlighted key predictors like Points Per Game (PPG) and Player Experience as the most influential factors in salary determination.
- **Visualizations:** Scatter plots showing the relationship between player statistics and salaries, residual plots, and regression coefficients.
- **Conclusion:** This project successfully applied multiple regression techniques to predict NBA player salaries, with Ridge Regression emerging as the most effective model.

**How to Run:**
1. Clone the repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the notebook `nba_salary_prediction.ipynb` to explore the full analysis.

---

### Project 4. [COVID-19 Vaccination and Impact Analysis](https://github.com/ton1rvr/portfolio/tree/07d5fa29fe8bedf42a502b5657f44f53c12fa21a/Project%204%20-%20COVID-19%20Analysis%20(data%20viz%20w%3A%20python))

**Objective:** This project investigates global COVID-19 vaccination trends and their impact on the spread of the virus, using data from Our World in Data.

- **Data:** The analysis uses detailed data on COVID-19 vaccinations, case counts, and deaths from various countries.
- **Techniques:**
  - **Data Cleaning and Preparation:** Handled missing values and ensured date formats were consistent across the dataset.
  - **Exploratory Data Analysis (EDA):** Analyzed vaccination trends over time and compared them with the number of new COVID-19 cases and deaths.
  - **Visualization:** Created both static and interactive visualizations using Seaborn, Plotly to explore and present the data.
- **Results:**
  - **Key Findings:** A strong correlation was observed between higher vaccination rates and the reduction of COVID-19 cases and deaths, although the impact varied across regions.
  - **Disparities:** The analysis also highlighted significant geographical disparities in vaccination coverage, underscoring the need for equitable distribution.
- **Visualizations:** Time series plots, scatter plots showing the relationship between vaccination rates and new cases, and choropleth maps visualizing global vaccination coverage.
- **Conclusion:** The project demonstrates the critical role of vaccination in controlling the pandemic and provides insights that could inform public health policies.

**How to Run:**
1. Clone the repository.
2. Install the required Python libraries using `pip install -r requirements.txt`.
3. Run the notebook `covid_vaccination_analysis.ipynb`.

---

### Project 5. [Stock Market Analysis Using Yahoo Finance API](https://github.com/ton1rvr/portfolio/tree/07d5fa29fe8bedf42a502b5657f44f53c12fa21a/Project%205%20-%20Stock%20Market%20Analysis%20(YFinance%20API%20w%3A%20python))

**Objective:** Analyze the performance of specific stocks over time using the Yahoo Finance API, focusing on both technical and fundamental analysis.

- **Data:** Stock price data, trading volumes, and financial statements for companies like Apple Inc., retrieved via the Yahoo Finance API.
- **Techniques:**
  - **Technical Analysis:** Used indicators like Moving Averages, RSI (Relative Strength Index), and Bollinger Bands to identify trends and potential entry/exit points.
  - **Fundamental Analysis:** Analyzed key financial ratios (e.g., current ratio, debt-to-equity ratio) to assess the company's financial health.
  - **Visualization:** Created static and interactive plots to explore stock performance and compare multiple stocks.
- **Results:**
  - **Technical Insights:** The analysis provided clear indicators of optimal trading strategies based on moving averages and RSI.
  - **Financial Health:** Apple Inc. demonstrated strong financial stability, with a high current ratio and low debt levels.
- **Visualizations:** Price trend charts, volume analysis, RSI plots, and interactive comparisons of multiple stocks.
- **Conclusion:** By combining technical and fundamental analysis, the project offers a comprehensive view of stock performance, aiding in more informed investment decisions.

**How to Run:**
1. Clone the repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the `stock_market_analysis.ipynb` notebook.

---
### Contacts
#### LinkedIn: Tonin RIVORY
#### Email: toninrvr@hotmail.com
