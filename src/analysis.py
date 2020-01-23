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
from docopt import docopt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

opt = docopt(__doc__)

def main(train_data, local_path):
    # in console type: python src/analysis.py --train_data=./data/processed/train_data.csv  --local_path=./results
    
    #convert to pandas data frame
    train_df = pd.read_csv(train_data)
    X = train_df.drop(columns='Class')
    y = train_df[['Class']]
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state = 123)
    

    #fit and predict using decision tree classifer
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    model_score = pd.DataFrame(cross_val_score(model, X_valid, y_valid, cv=10))
    model_score.columns=['test_score']
    model_score['train_score'] = cross_val_score(model, X_train, y_train, cv=10)

    #write to csv
    model_score.to_csv("%s/analysis_result.csv" % local_path)
    
  
if __name__ == "__main__":
    main(opt["--train_data"],opt["--local_path"])