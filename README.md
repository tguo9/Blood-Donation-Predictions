# Blood Donation Predictions
* Contributors: 
  - Evelyn Moorhouse
  - Tao Guo
  - Lise Braaten 
  - Xinwen Wang
  
## Introduction

We have attempted to build a classification model to determine if a person donated blood on specific date as a result of their past donation history. The goal of working with the data set is to see whether the features Recency(last donation month), Frequency(total number of donation) and Monetary(total blood donated) have any effect on whether the blood was donated on a given date. Therefore if these features have effects on donation, we can extrapolate and infer that they likely would have an effect on future donation.

The question that we aimed to answer was: Do Recency(last donation month), Frequency(total number of donation) and Monetary(total blood donated) have any effect on whether the blood was donated on a specific date? 

We preformed classification with three different models: Decision Tree, Random Forest and Logistic Regression. Our best validation results were obtained from the Random Forest model with a 0.30 error, however, our Logistic regression model had a much smaller difference between train and validation errors, with a validation error of 0.32. Since our errors were so high, we would not recommend using a model based on these features to predict blood donation from past donors. However, if it is necessary we would recommend the Logistic Regression classifier since the smaller difference between train and validation error would imply it is better for generalizing to new data. 

Based on our results we infer that the features of 1) time since last donation, 2) total number of donations, 3) total blood donated, and 4) the time since the first donation, all combined have some predictive power for whether a patient will donate blood. However, since our accuracy and cross validation scores were low, the combined predictive power of these features is low. Since the predictive power is so low, we suggest that these features don’t have a strong influence on whether a patient donates blood or not. We would suggest that other factors may provide better predictions as to whether blood is donated by a past donor.

## Report

The final report can be found [here](/doc/report.md)

## Dependency Diagram

![](Makefile.png)

## Usage

#### 1\. Using Docker

*note - the instructions in this section also depends on running this in
a unix shell (e.g., terminal or Git Bash)*

To replicate the analysis, install
[Docker](https://www.docker.com/get-started). Then clone this GitHub
repository and run the following command at the command line/terminal
from the root directory of this project:

    docker run --rm -v $(pwd):/home/mds522_305 tguo3/mds make -C '/home/mds522_305' all

To reset the repo to a clean state, with no intermediate or results
files, run the following command at the command line/terminal from the
root directory of this project:

    docker run --rm -v $(pwd):/home/mds522_305 tguo3/mds make -C '/home/mds522_305' clean

#### 2\. Without using Docker

To replicate the analysis, clone this GitHub repository, install the dependencies listed below, and run the following command at the command line/terminal from the root directory of this project:

```
make all
```

To clean the repo and reset it to a state with no intermediate files or results run the following command at the command line/terminal from the root directory of this project:

```
make clean
```

## Dependencies

Python 3.7.3 and Python packages: </br>
sklearn==0.22.1 </br>
pandas==0.24.2 </br>
altair==3.2.0 </br>
datapackage==1.11.0 </br>
docopt==0.6.2 </br>
requests==2.22.0 </br>

R version 3.6.1 and R packages: </br>
tidyverse==1.2.1 </br>
ggplot2==3.2.1 </br>
kableExtra==1.1.0</br>
        
## References

Armitage, C. J., & Conner, M. (2001). Social cognitive determinants of blood donation. Journal of applied social psychology, 31(7), 1431-1457.
</br></br>
de Jonge, Edwin. 2018. Docopt: Command-Line Interface Specification Language. https://CRAN.R-project.org/package=docopt.
</br></br>
Gillespie, T. W., & Hillyer, C. D. (2002). Blood donors and factors impacting the blood donation decision. Transfusion Medicine Reviews, 16(2), 115-130.
</br></br>
Keleshev, Vladimir. 2014. Docopt: Command-Line Interface Description Language. https://github.com/docopt/docopt.
</br></br>
Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Vanderplas, J. (2011). Scikit-learn: Machine learning in Python. Journal of machine learning research, 12(Oct), 2825-2830
</br></br>
R Core Team. 2019. R: A Language and Environment for Statistical Computing. Vienna, Austria: R Foundation for Statistical Computing. https://www.R-project.org/.
</br></br>
Van Rossum, Guido, and Fred L. Drake. 2009. Python 3 Reference Manual. Scotts Valley, CA: CreateSpace.
</br></br>
VanderPlas et al. Altair: Interactive Statistical Visualizations for Python. Journal of Open Source Software (2018)
</br></br>
Wes McKinney. Data Structures for Statistical Computing in Python, Proceedings of the 9th Python in Science Conference, 51-56 (2010) (publisher link)
</br></br>
Wickham, H. (2016). ggplot2: elegant graphics for data analysis. Springer.
</br></br>
Wickham, Hadley. 2017. Tidyverse: Easily Install and Load the ’Tidyverse’. https://CRAN.R-project.org/package=tidyverse.
</br></br>
Xie, Yihui. 2014. “Knitr: A Comprehensive Tool for Reproducible Research in R.” In Implementing Reproducible Computational Research, edited by Victoria Stodden, Friedrich Leisch, and Roger D. Peng. Chapman; Hall/CRC. http://www.crcpress.com/product/isbn/9781466561595.
</br></br>
Yeh, I. C., Yang, K. J., & Ting, T. M. (2009). Knowledge discovery on RFM model using Bernoulli sequence. Expert Systems with Applications, 36(3), 5866-5871
</br></br>
