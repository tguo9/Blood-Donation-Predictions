# authors: DSCI 522 Group 203 
# date: 2020-01-18

"""
This script downloads and writes a csv file to your computer
Takes a URL and a local file path as arguments

Usage: load_data.py --data_url=<data_url> --local_path=<local_path>

Options:
--data_url=<data_url>         URL of the data 
--local_path=<local_path>     Local path you want the csv file to be written to
"""

import pandas as pd
from docopt import docopt

opt = docopt(__doc__)

def main(data_url, local_path):
    data = pd.read_csv(data_url)
    data.to_csv(local_path)

if __name__ == "__main__":
    main(opt["--data_url"], opt["--local_path"])
