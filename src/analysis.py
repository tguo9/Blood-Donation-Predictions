# authors: DSCI 522 Group 305 
# date: 2020-01-22

"""
This script read in the data processed by pre-process.py and apply decision tree algorithm

Usage: src/analysis.py --train_data=<train_data>  --local_path=<local_path>

Options:
--train_data=<train_data>  Local path to the training data csv file (include file name)
--local_path=<local_path>  Local path to folder you want the analysis files to be written to 
"""

import pandas as pd
import numpy as np
from docopt import docopt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix 

opt = docopt(__doc__)

def main(train_data, local_path):
    # in console type: python src/analysis.py --train_data=./data/processed/train_data.csv  --local_path=./results
    
    #convert to pandas data frame
    train_df = pd.read_csv(train_data)

    #resample due to unbalanced data set more people not donate
    donate = train_df[train_df.Class == 2]
    not_donate = train_df[train_df.Class == 1]
    not_resample = resample(not_donate, replace = False, n_samples=len(donate), random_state= 100)
    train_df = pd.concat([donate,not_resample])
    X = train_df.drop(columns='Class')
    y = train_df[['Class']]
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state = 123)
    

    #fit and predict using decision tree classifer and gridCV to find best max_depth hyperparameter
    model = DecisionTreeClassifier()
    param_grid = {'max_depth': list(range(2,15)),'min_samples_split':list(range(2,5))}
    CV = GridSearchCV(model, param_grid, cv = 10, refit=True)          
    CV.fit(X_train, y_train)
    d = {'method':'Decision Tree',
        'Best_max_depth':[CV.best_params_['max_depth']], 
        'Bestmin_samples_split':[CV.best_params_['min_samples_split']],
        'Best_CV_Score':[CV.best_score_], 
        'Training_Error':[1 - CV.score(X_train, y_train)], 
        'Validation_Error':[1 - CV.score(X_valid, y_valid)]}
    d=pd.Series(d)
    
    
    # try random forest model
    forest = RandomForestClassifier(n_estimators =100)
    param_grid_f = {'max_depth': list(range(2,15)),'min_samples_split':list(range(2,5))}
                    #'n_estimators': list(range(80,120))}

    CV_f = GridSearchCV(forest, param_grid_f, cv = 5, refit=True)          
    CV_f.fit(X_train, np.ravel(y_train))
    d_f = { 'method':'Random Forest',
        'Best_max_depth':[CV_f.best_params_['max_depth']], 
        'Best_min_samples_split':[CV_f.best_params_['min_samples_split']],
        #'Best_n_estimators': [CV_f.best_params_['n_estimators']],
        'Best_CV_Score':[CV_f.best_score_], 
        'Training_Error':[1 - CV_f.score(X_train, y_train)], 
        'Validation_Error':[1 - CV_f.score(X_valid, y_valid)]}
    d_f=pd.Series(d_f)

    
    #try logistic regression
    model_r = LogisticRegression(solver ='lbfgs')
    param_grid_r = {'C':[0.001, 0.01, 0.1, 1, 10, 100, 1000]}
    CV_r = GridSearchCV(model_r, param_grid_r, cv = 10, refit=True)          
    CV_r.fit(X_train, y_train['Class'])
    d_r = {'method':'Logistic regression',
        'C':[CV_r.best_params_['C']], 
        'Best_CV_Score':[CV_r.best_score_], 
        'Training_Error':[1 - CV_r.score(X_train, y_train)], 
        'Validation_Error':[1 - CV_r.score(X_valid, y_valid)]}
    d_r= pd.Series(d_r)

    d_2=pd.concat([d_f,d])
    model_score =  pd.concat([d_2, d_r])

    #find out the best one is logistic regression, so we do a confusion matrix
    model_better = LogisticRegression(solver ='lbfgs', C=CV_r.best_params_['C'])
    model_better.fit(X_train, y_train['Class'])
    y_pred = model_better.predict(X_valid)
    confusion = pd.DataFrame(confusion_matrix(y_valid, y_pred))

    try:
        #write to csv
        model_score.to_csv("%s/analysis_result.csv" % local_path)
        confusion.to_csv("%s/analysis_confusion.csv" % local_path)
    except:
        os.makedirs(os.path.dirname(local_path))
        model_score.to_csv("%s/analysis_result.csv" % local_path)
        confusion.to_csv("%s/analysis_confusion.csv" % local_path)

    
    
if __name__ == "__main__":
    main(opt["--train_data"],opt["--local_path"])