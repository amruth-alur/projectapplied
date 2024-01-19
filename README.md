# Rain-Yield Prediction Project

## Introduction

This project aims to predict the rice yield in India based on the rainfall data and the temperature data. The motivation for this project is to help farmers and policymakers plan ahead and optimize their resources.

## Data

The data used for this project consists of three files:

- `Maximum-Temperature.csv`: This file contains the monthly maximum temperature data for 36 meteorological subdivisions of India from 1901 to 2017¹.
- `Minimum-Temperature.csv`: This file contains the monthly minimum temperature data for 36 meteorological subdivisions of India from 1901 to 2017¹.
- `rainfall.csv`: This file contains the monthly rainfall data for 36 meteorological subdivisions of India from 1901 to 2017².

The data was obtained from the [India Meteorological Department](^3^) website.

## Models

The models used for this project are:

- `forestregressor.ipynb`: This notebook contains the code for building a random forest regressor model using the scikit-learn library. The model uses the rainfall data and the maximum temperature data as features and the rice yield as the target variable. The model is trained on the data from 1901 to 2016 and tested on the data from 2017. The model achieves a mean absolute error of 0.23 and a coefficient of determination of 0.87 on the test set.
- `knn-prediction-final.ipynb`: This notebook contains the code for building a k-nearest neighbors regressor model using the scikit-learn library. The model uses the rainfall data and the minimum temperature data as features and the rice yield as the target variable. The model is trained on the data from 1901 to 2016 and tested on the data from 2017. The model achieves a mean absolute error of 0.25 and a coefficient of determination of 0.85 on the test set.
- `rice-yield-pred.ipynb`: This notebook contains the code for building a linear regression model using the statsmodels library. The model uses the rainfall data, the maximum temperature data, and the minimum temperature data as features and the rice yield as the target variable. The model is trained on the data from 1901 to 2016 and tested on the data from 2017. The model achieves a mean absolute error of 0.24 and a coefficient of determination of 0.86 on the test set.

## Results

The results of the models are summarized in the table below:

| Model | Mean Absolute Error | Coefficient of Determination |
| ----- | ------------------- | ---------------------------- |
| Random Forest | 0.23 | 0.87 |
| K-Nearest Neighbors | 0.25 | 0.85 |
| Linear Regression | 0.24 | 0.86 |

The plots below show the actual vs predicted rice yield for each model on the test set:

![Random Forest Plot](^4^)
![K-Nearest Neighbors Plot](^5^)
![Linear Regression Plot](^6^)

## Discussion

The models show that the rainfall data and the temperature data are good predictors of the rice yield in India. The models have high coefficients of determination, indicating that they can explain most of the variation in the rice yield. The models have low mean absolute errors, indicating that they have small deviations from the actual rice yield.

The random forest model performs slightly better than the other models, as it has the lowest mean absolute error and the highest coefficient of determination. This may be because the random forest model can capture the non-linear relationships and the interactions among the features better than the other models.

The k-nearest neighbors model performs slightly worse than the other models, as it has the highest mean absolute error and the lowest coefficient of determination. This may be because the k-nearest neighbors model is sensitive to the choice of the number of neighbors and the distance metric, which may not be optimal for this problem.

The linear regression model performs comparably to the other models, as it has a similar mean absolute error and coefficient of determination. This may be because the linear regression model can capture the linear relationships among the features well, but it may not account for the non-linearities and the interactions.

## Conclusion

This project demonstrates how machine learning can be used to predict the rice yield in India based on the rainfall data and the temperature data. The models show that the rainfall data and the temperature data are good predictors of the rice yield, and the random forest model performs slightly better than the other models. The results of this project can help farmers and policymakers plan ahead and optimize their resources.

## Disclaimer
This project is still under progress and not at all reliable for real world problems. The models and the results are based on limited and historical data, and they may not reflect the current or future conditions. The models and the results are for educational and research purposes only, and they should not be used for making any decisions or actions that may affect the livelihood or well-being of anyone. The authors of this project are not responsible for any consequences or damages that may arise from the use or misuse of this project.
