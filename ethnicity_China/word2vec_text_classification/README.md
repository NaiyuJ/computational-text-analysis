## Word2vec Text Classification


I used word2vec model to do text classification by measuring the cosine similarity scores. Measuring the similarity between the post and the full dictionary of a speciﬁc category, the algorithm would generate similarity scores on each category for each post. After obtaining all these similarity scores, I classiﬁed posts based on which category got the highest similarity score.

### Supporting scripts for measuring similarity
* [msr.py](https://github.com/NaiyuJ/computational-text-analysis/blob/main/ethnicity_China/word2vec_text_classification/msr.py)
* [test_utility.py](https://github.com/NaiyuJ/computational-text-analysis/blob/main/ethnicity_China/word2vec_text_classification/test_utility.py)
