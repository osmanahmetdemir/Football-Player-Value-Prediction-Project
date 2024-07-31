# Football Player Value Prediction

## Overview
This project analyzes the transfer market for women's football, using machine learning models to predict player market values. As the popularity of women's football grows, the transfer market has become more complex, with increasing transfer fees and data analytics playing a crucial role in decision-making.

## Literature Review

### Growth in Transfers and Expenditures
- **Significant rise in both transfer numbers and fees.**
- **Example:** Transfer fees reached $3 million in summer 2022, marking a 140.8% increase.

### Importance of Data Analytics
Data-driven decision-making can enhance transfer success compared to intuition-based approaches.

### Use of Alternative Data Sources
Alternative data, like video games (e.g., FIFA), are utilized to predict player performance due to limited access to comprehensive player data.

## Project Goal
To evaluate machine learning models for predicting the value of women footballers, providing stakeholders with actionable insights for strategic decisions in the transfer market.

## Methodology

### Data Acquisition
- **Source:** Data collected from sofifa.com.
- **Process:** Python script used to scrape data, including player ratings, positions, skills, etc.
- **Output:** Data stored in `womendataset.csv`.

### Data Processing
- **Data Split:**
  - Training: 67.4%
  - Testing: 15%
  - Validation: 17.6%
- **Preprocessing:** Filling missing values and applying Min-Max normalization.

### Model Training
- **Models:** Gradient Boosting, Random Forest, K-Nearest Neighbors (KNN), etc.
- **Optimization:** Bayesian Optimization for hyperparameter tuning.

## Findings
- **Best Model:** Gradient Boosting achieved the highest accuracy.
- **Fastest Model:** KNN was the fastest in training.

## Discussion
Machine learning models, especially Gradient Boosting, effectively predict the market values of female football players. This provides clubs and agents with valuable insights for making informed transfer decisions.

## Conclusion
The study highlights the effectiveness of machine learning models in predicting football player market values. Further research is necessary to explore the broader applications of these findings in the football transfer market.
