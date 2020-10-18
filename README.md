# TAMU-Datathon
This repository contains the scripts and data for our submission to the TAMU Datathon 2020.

This submission is for the [WALMART COMPANY CHALLENGE](https://tamudatathon.com/challenges#td_open)

Team Members: Daniel Chavez, Bhaskar, Tapan Ganatma Nakkina, Srishti Saha


The challenge was divided into sub tasks. We spend a significant time scraping the data and finally realized we could parallelize it. It was much faster and we could collect around 12,000 data points. Based on the recommendations available on the site, we built a recommender system to build a recommendation system "just" based on graph connectivity metrics and not using any of the semantics or keywords. We also built a categorization algorithm to find out what group a particular search query belonged to.


## Video Submissions:
* [Classifier Demo](https://www.youtube.com/watch?v=4yyQNJGJmeY&feature=youtu.be);
* [Recommender Systems Demo](https://www.youtube.com/watch?v=vynHLFwdmPw);
* [Final Presentation](https://www.youtube.com/watch?v=Ibpqs3JcxEE)



## About the Repo

#### Data Scraping
The data scraping folder has all our scripts for crawling through the Walmart website. The pulled data is in the data folder here.

The script **WLMT_looped_URLsets.ipynb** has all the URL sets and the unoptimized version of the scraping script. The script **Multithread__BB_Fuse.ipynb** has the multithread optimized version of scraping which we used to pull our data.



#### Classification

This folder contains all the scripts for developing, training and testing the classification model. The model finds the best suited category for a paticular product that is provided as the input. The demo video has been linked above


#### Graph Analysis

This folder has all the scripts for doing the graph analysis and showcasing the results. It plugs in to the recommender system that recommends several other products based on a particular product choice. The demo video is linked above.


