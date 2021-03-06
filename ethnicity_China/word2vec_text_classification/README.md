## Word2vec Text Classification


I used word2vec model to do text classification by measuring the cosine similarity scores. Measuring the similarity between the post and the full dictionary of a speciﬁc category, the algorithm would generate similarity scores on each category for each post. After obtaining all these similarity scores, I classiﬁed posts based on which category got the highest similarity score.

### Run
* [word2vec_classification.ipynb](https://github.com/NaiyuJ/computational-text-analysis/blob/main/ethnicity_China/word2vec_text_classification/word2vec_classification.ipynb)

### Supporting scripts for measuring similarity
* [msr.py](https://github.com/NaiyuJ/computational-text-analysis/blob/main/ethnicity_China/word2vec_text_classification/msr.py)
* [test_utility.py](https://github.com/NaiyuJ/computational-text-analysis/blob/main/ethnicity_China/word2vec_text_classification/test_utility.py)

### Input
* The total posts I scraped from seven Baidu Tieba: [total_posts.csv](https://www.dropbox.com/s/4tp552pse156tw6/total_posts.csv?dl=0)

### Output (posts with categories)
* [total_cat.csv](https://www.dropbox.com/s/sk1mympp087f022/total_cat.csv?dl=0)
