# mds522_305: Blood Donation Predictions
* Contributors: 
  - Evelyn Moorhouse
  - Tao Guo
  - Lise Braaten 
  - Xinwen Wang
  
## Introduction

We have chosen a data set that indicates whether a person donated blood on specific date as a result of their past donation history. The goal of working with the data set is to see whether the features Recency(last donation month), Frequency(total number of donation) and Monetary(total blood donated) have any effect on whether the blood was donated on a given date. Therefore if these features have effects on donation, we can extrapolate and infer that they likely would have an effect on future donation.

The question that we aim to answer is: Do Recency(last donation month), Frequency(total number of donation) and Monetary(total blood donated) have any effect on whether the blood was donated on a specific date? With the sub-question of: which predictor has the greatest impact on donation?

We will perform classification with a decision tree. If we can generate a model with acceptable train and test accuracies based on these features, we will be able to conclude that these features are good predictors and influence donation based on donation history. Furthermore, we can then address our predictive sub question for which feature has the greatest influence.

In our EDA .ipynb file we created a summary table of the features, in addition to two other tables separated by positive and negative target values, to find the averages of the features associated with positive and negative results (donated and not donated). By creating a general summary table, as well as two tables filtered for ‘donated’ and ‘not donated’ we will be able to find the average of all the features with regards to donation history, as well as the average of the features that correspond to donated and not donated. Since we observed differences between these values, we are able infer that these features likely have an effect on whether blood will be donated based on donation history. 

For visual EDA we will dreate histograms of each feature with positive and negative target values separated. By creating histograms for each feature separated for ‘donated’ and ‘not donated’ we will be able to view the distribution of all the values of a given feature, as well as if there are any clear division based on ‘donated’ or ‘not donated’ for each feature. 

## Dependencies

Python 3.7.3 and Python packages: </br>
        sklearn==0.22.1 </br>
        pandas==0.24.2 </br>
        altair==3.2.0 </br>
        
## References

