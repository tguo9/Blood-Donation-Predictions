# authors: DSCI 522 Group 305 
# date: 2020-01-23

"Creates eda plots for the pre-processed training data from the blood donation data (from https://archive.ics.uci.edu/ml/datasets/Blood+Transfusion+Service+Center).
Saves the plots as png files.

Usage: src/plot.R --file_path=<file_path> --out_dir=<out_dir>

Options:
--file_path=<file_path> Path (including filename) to training data
--out_dir=<out_dir> Path to directory where the eds plots should be written
" -> doc

library(tidyverse)
library(ggplot2)
library(docopt)

opt <- docopt(doc)

main <- function(file_path, out_dir){
    
    # read in data
    data <- read.csv(file_path)
    
    p1 <- data %>% 
        ggplot() +
        geom_bar(aes(since_last_don, fill = factor(Class))) +
        xlab('Time Since Last Blood Donation (in months)') +
        ylab('Number of Donors') +
        labs(fill= '') +
        scale_fill_discrete(labels = c('Not donated', 'Donated')) +
        ggtitle('Time Since Last Blood Donation Distribution')

    p3 <- data %>% 
        ggplot() +
        geom_bar(aes(total_blood, fill = factor(Class))) +
        xlab('Total Blood Donation (in centilitres)') +
        ylab('Number of Donors') +
        labs(fill= '') +
        scale_fill_discrete(labels = c('Not donated', 'Donated')) +
        ggtitle('Total Blood Donation Distribution')

    p4 <- data %>% 
        ggplot() +
        geom_bar(aes(since_first_don, fill = factor(Class))) +
        xlab('Time Since First Blood Donation (in months)') +
        ylab('Number of Donors') +
        labs(fill= '') +
        scale_fill_discrete(labels = c('Not donated', 'Donated')) +
        ggtitle('Time Since First Blood Donation Distribution')
    
    try({
        dir.create(out_dir)
    })
    ggsave(p1, file=paste(out_dir, 'since_last_don.png', sep = ""))
    ggsave(p3, file=paste(out_dir, 'total_blood.png', sep = ""))
    ggsave(p4, file=paste(out_dir, 'since_first_don.png', sep = ""))

}

main(opt[["--file_path"]], opt[["--out_dir"]])