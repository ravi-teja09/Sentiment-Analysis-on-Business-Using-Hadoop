# Sentiment-Analysis-on-Business-using-Hadoop
Performed Sentiment analysis of People on Business on Twitter data and compared that with NYTimes articles and media articles obtained using CommonCrawl. **Hadoop** is used to perform the word count and co-occurance of top words in two sets of data. I have used **Tableau** for word-could and python to implement mapper and reducer of Hadoop framework.

### Tasks Perfomed
Objective was to perform sentiment analysis on Big data. For this task we collected data from multiple sources (twitter, NYTimes and CommonCrawl) on the main topic of *Business* and 5 subtopics Markets, Economy, Money, Entrepreneur, Energy using the APIs. The data was cleaned and exploratory data anlaysis was performed. Implemented map reduce algorithm on a single-node Hadoop cluster backed by Hadoop Distributed File System,running on Docker to calculate the word count and word co-occurences by pairs and strips method.

The resulting words with highest word counts and co-occurence pairs were visualized using word cloud in Tableau and published. 

### Tools used
Python 3, Docker, Cloudera Quickstart Docker Image, Tableau, Article Search API, Common Crawl index AP

### Libraries 
NLTK, rtweet, Beautiful Soup, warcio

### Visualizations
* Top 10 words with word-count comparison:
![](https://github.com/ravi-teja-sunkara/Sentiment-Analysis-on-Business-using-Hadoop/blob/master/Images/Word%20Count%20Comparison.JPG)

* Top 10 co-occuring pairs comparison:
![](https://github.com/ravi-teja-sunkara/Sentiment-Analysis-on-Business-using-Hadoop/blob/master/Images/Co-occurence%20Comparison.JPG)


