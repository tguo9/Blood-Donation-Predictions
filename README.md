# mds522_305: Social Network Add Purchases Predictor
* Contributors: 
  - Evelyn Moorhouse
  - Tao Guo
  - Lise Braaten 
  - Xinwen Wang
  
## Introduction


We have chosen a data set which shows whether a person donated blood on specific date as a result of their past donation history. The goal of working with the data set is to see whether the features Recency(last donation month), Frequency(total number of donation) and Monetary(total blood donated) have any effect on whether the blood was donated on that date. Therefore if these features have effects on donation, we can extrapolate and infer that they likely would have an effect on future donation.

We will perform classification with a decision tree. If we can generate a model with acceptable train and test accuracies based on these features, we will be able to conclude that these features are good predictors and influence donation based on donation history. Furthermore, we can then address our predictive sub question for which feature has the greatest influence.


## Dependencies

Python 3.7.3 and Python packages: </br>
        sklearn==0.22.1 </br>
        pandas==0.24.2 </br>
        altair==3.2.0 </br>
        
## References

Kirill Eremenko and Hadelin de Ponteves, https://archive.ics.uci.edu/ml/datasets/Blood+Transfusion+Service+Center