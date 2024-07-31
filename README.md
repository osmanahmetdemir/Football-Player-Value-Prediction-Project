# <span style="color:blue">Football Player Value Prediction</span>

## <span style="color:green">Overview</span>
This project analyzes the transfer market for women's football, using machine learning models to predict player market values. As the popularity of women's football grows, the transfer market has become more complex, with increasing transfer fees and data analytics playing a crucial role in decision-making.

## <span style="color:red">Literature Review</span>

### <span style="color:orange">Growth in Transfers and Expenditures</span>
- **Significant rise in both transfer numbers and fees.**
- **Example:** Transfer fees reached $3 million in summer 2022, marking a 140.8% increase.

### <span style="color:purple">Importance of Data Analytics</span>
Data-driven decision-making can enhance transfer success compared to intuition-based approaches.

### <span style="color:brown">Use of Alternative Data Sources</span>
Alternative data, like video games (e.g., FIFA), are utilized to predict player performance due to limited access to comprehensive player data.

## <span style="color:teal">Project Goal</span>
To evaluate machine learning models for predicting the value of women footballers, providing stakeholders with actionable insights for strategic decisions in the transfer market.

## <span style="color:darkcyan">Methodology</span>

### <span style="color:darkorange">Data Acquisition</span>
- **Source:** Data collected from sofifa.com.
- **Process:** Python script used to scrape data, including player ratings, positions, skills, etc.
- **Output:** Data stored in `womendataset.csv`.

### <span style="color:darkred">Data Processing</span>
- **Data Split:**
  - Training: 67.4%
  - Testing: 15%
  - Validation: 17.6%
- **Preprocessing:** Filling missing values and applying Min-Max normalization.

### <span style="color:darkgreen">Model Training</span>
- **Models:** Gradient Boosting, Random Forest, K-Nearest Neighbors (KNN), etc.
- **Optimization:** Bayesian Optimization for hyperparameter tuning.

## <span style="color:darkblue">Findings</span>
- **Best Model:** Gradient Boosting achieved the highest accuracy.
- **Fastest Model:** KNN was the fastest in training.

## <span style="color:darkmagenta">Discussion</span>
Machine learning models, especially Gradient Boosting, effectively predict the market values of female football players. This provides clubs and agents with valuable insights for making informed transfer decisions.

## <span style="color:darkviolet">Conclusion</span>
The study highlights the effectiveness of machine learning models in predicting football player market values. Further research is necessary to explore the broader applications of these findings in the football transfer market.
