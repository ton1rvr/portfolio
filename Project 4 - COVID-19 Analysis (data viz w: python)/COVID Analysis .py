# COVID-19 Vaccination and Impact Analysis

## 1. Introduction
# This notebook explores the global trends in COVID-19 vaccinations and analyzes their impact on the spread of the virus.

## 2. Data Collection and Preparation

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load COVID-19 vaccination data from Our World in Data
url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
data = pd.read_csv(url)

# Display the first few rows of the dataset
data.head()

# Convert 'date' column to datetime
data['date'] = pd.to_datetime(data['date'])

# Select relevant columns for the analysis
columns_of_interest = ['location', 'date', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated', 'new_cases', 'new_deaths']
data = data[columns_of_interest]

# Handle missing values
data.fillna(0, inplace=True)

# Display the cleaned data
data.head()

## 3. Exploratory Data Analysis (EDA)

# Example: Vaccination trend over time for a specific country (e.g., United States)
us_data = data[data['location'] == 'United States']

plt.figure(figsize=(10,6))
sns.lineplot(x='date', y='people_vaccinated', data=us_data, label='Partially Vaccinated')
sns.lineplot(x='date', y='people_fully_vaccinated', data=us_data, label='Fully Vaccinated')
plt.title('Vaccination Trend in the United States')
plt.xlabel('Date')
plt.ylabel('Number of People')
plt.legend()
plt.show()

# Correlation between vaccination rates and new cases
plt.figure(figsize=(10,6))
sns.scatterplot(x='people_vaccinated', y='new_cases', data=us_data)
plt.title('Correlation between Vaccination and New Cases in the United States')
plt.xlabel('People Vaccinated')
plt.ylabel('New Cases')
plt.show()
