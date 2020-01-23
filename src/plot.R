# > Rscript plot.R ../data/processed/train_data.csv results/
# Usage: Rscript plot.R

"This script makes 4 different graphs.

Usage: plot.R <file_path> <output>
" -> doc

library(tidyverse)
library(ggplot2)
library(docopt)

opt <- docopt(doc)

main <- function(file_path, output){
    
    # read in data
    data <- read.csv(file_path)
    
    p1 <- data %>% 
        ggplot() +
        geom_bar(aes(since_last_don, fill = factor(Class))) +
        xlab('Since Last Donation') +
        ylab('Number of Donors') +
        ggtitle('Donor Since Last Donation Distribution')

    p2 <- data %>% 
        ggplot() +
        geom_bar(aes(total_dons, fill = factor(Class))) +
        xlab('Total Donation') +
        ylab('Number of Donors') +
        ggtitle('Total Donation Distribution')

    p3 <- data %>% 
        ggplot() +
        geom_bar(aes(total_blood, fill = factor(Class))) +
        xlab('Total Blood Donation') +
        ylab('Number of Donors') +
        ggtitle('Donor Total Blood Donation Distribution')

    p4 <- data %>% 
        ggplot() +
        geom_bar(aes(since_first_don, fill = factor(Class))) +
        xlab('Since First Donation') +
        ylab('Number of Donors') +
        ggtitle('Donor Since First Donation Distribution')
    
    ggsave(p1, file=paste('../', opt$output, 'since_last_don.png', sep = ""))
    ggsave(p2, file=paste('../', opt$output, 'total_dons.png', sep = ""))
    ggsave(p3, file=paste('../', opt$output, 'total_blood.png', sep = ""))
    ggsave(p4, file=paste('../', opt$output, 'since_first_don.png', sep = ""))

}

main(opt$file_path, opt$output)
