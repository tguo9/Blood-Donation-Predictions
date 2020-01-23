# authors: DSCI 522 Group 305 
# date: 2020-01-18

"""
This script downloads and writes a csv file to your computer
Takes a URL and a local file path as arguments

Usage: load_data.py --data_url=<data_url> --local_path=<local_path>

Options:
--data_url=<data_url>      URL of the data 
--local_path=<local_path>  Local path you want the csv file to be written to (include file name)
"""

import datapackage
import pandas as pd
from docopt import docopt

opt = docopt(__doc__)

def main(data_url, local_path):
    # in console type: python load_blood_donor_data.py --data_url 'https://datahub.io/machine-learning/blood-transfusion-service-center/datapackage.json' --local_path ../data/raw_data.csv
    
    #data_url = 'https://datahub.io/machine-learning/blood-transfusion-service-center/datapackage.json'

    # to load Data Package into storage
    package = datapackage.Package(data_url)

    # to load only tabular data
    resources = package.resources
    for resource in resources:
        if resource.tabular:
            data = pd.read_csv(resource.descriptor['path'])
    

    data.to_csv(local_path)

if __name__ == "__main__":
    main(opt["--data_url"], opt["--local_path"])