## Unexpectedly Hopeful Ethnic Minorities in China: The Minority Mind
#### Naiyu Jiang (nyjiang@uchicago.edu)

### Research question

* How do authoritarian institutions accommodate marginalized groups such as ethnic minorities?
* Why and how do ethnic minorities feel satisﬁed with their social status even though they are economically disadvantaged?

### Steps:
* Scrape Tieba data: [Tieba-scraper](https://github.com/NaiyuJ/computational-text-analysis/tree/main/ethnicity_China/Tieba-scraper)
  * also scrape extra training corpus for word embeddings.
* Train word2vec model: [train-word2vec-model](train-word2vec-model)
* Use word2vec model to do text classification: [word2vec_text_classification](https://github.com/NaiyuJ/computational-text-analysis/tree/main/ethnicity_China)
* Use fine-tuned BERT model to do sentiment analysis: [sentiment-analysis](https://github.com/NaiyuJ/computational-text-analysis/tree/main/ethnicity_China/sentiment-analysis)
* Analyze and visualize the results: [Analysis.Rmd](https://github.com/NaiyuJ/computational-text-analysis/blob/main/ethnicity_China/Analysis.Rmd)
* Influence networks: [networks-analysis](https://github.com/NaiyuJ/computational-text-analysis/tree/main/ethnicity_China/networks-analysis)

