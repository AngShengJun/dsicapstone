# Part 4: Modeling, Evaluation & Recommendations

## Overview

This section discusses the model workflow and findings from model evaluation.

---

## Model workflow & Evaluation Metrics

- first split data into i) train and test set, then split the train set into train subsets and validate subsets.

- only fit on the train set then score on validate set. (Similar principle applies on test set). 

- evaluate model

  This would prevent data leakage (inadvertent count vectorize (a transformer) the entire data before doing train-test-split).

The cost of a false negative is **higher** than false positive (potentially higher casualties); it is better that CT ops be more prepared in event of an actual bombing incident than be under-prepared. Therefore, the priority is to minimize false negatives**.

Model metrics for evaluation:
- `sensitivity` (reduce false negatives) AND
- `ROC-AUC` (measures model's skill in classification)

---

## Model Evaluation

The logistic regression and Naive Bayes models were explored and their performance measures were evaluated using train and validate data set: 

| Metrics                 | Logistic Regression | Naive Bayes |
| ----------------------- | ------------------- | ----------- |
| **accuracy (validate)** | 0.6781              | 0.6593      |
| **sensitivity**         | 0.8512              | 0.8246      |
| **roc_auc**             | 0.7460              | 0.7272      |

Prioritization is on correct classification of bomb attack mode as a misclassified actual bomb attack mode could lead to relatively more dire consequences (more casualties). In this regard, we would want to pick the model with highest True Positive Rate (sensitivity), for as much correct classification of the bomb attack modes as possible. Therefore, we pick the Logistic Regression model as the production model.

Next, fit LR model on full train set, test on test set, review misclassified samples and then explore tuning the production model.

---

## Model Tuning & Findings :mag_right:

On model tuning exploration, several means were explored:

- removal of fifty words that contributed to false negative
- removal of significant occurring overlap words (more than 1200 occurrences)

Summary of model scores (Full train set on Test set)

| Metrics         | LR model | LR model (50 false neg wrd removed) | LR model (sigfn ovrlap wrd removed) |
| --------------- | -------- | ----------------------------------- | ----------------------------------- |
| **accuracy**    | 0.6898   | 0.6859                              | 0.6841                              |
| **sensitivity** | 0.8584   | 0.8610                              | 0.8597                              |
| **roc_auc**     | 0.7622   | 0.7566                              | 0.7526                              |

With remove of words contributing to false negatives, there is a marginal increase in sensitivity but at a cost to the roc_auc (trade-off between sensitivity and specificity). The removal of significantly occurring overlap words would not necessarily improve the model performance (sensitivity and roc_auc) as these words are also a dominant feature for the class 1 prediction, and there exists a variance between the proportion of overlap (higher proportion on positive bomb class). This means sensitivity could decrease with the removal of the words.

## Recommendations (Part1)

The Logistic Regression (LR) model performs better than the naive bayes model in terms of the sensitivity and roc_auc scores. In general, the LR production model versions has good sensitivity and roc_auc (priority is to minimize false negatives) above 85% and 75% respectively. False positive is not considered a high cost for CT, since they will be expecting an terror incident). Considering the sensitivity and roc_auc score, I propose the second logistic regression model (50 false negative words removed) as the finalized production model (best sensitivity score, with roc_auc above 75%. 

The removal of common occurring words (between classes) that has low frequency is a common technique used for tuning model performance; however, from the distribution of word features between the two classes, this is assessed to be not suitable for this particular dataset.

In the next part, topic modeling is discussed.  

---

## Topic Modeling

Topic modelling was conducted on the train data set. The optimum number of topics was determined to be 42 topics, based on the coherence value to topics plot. An LDA model is trained using the train data. From here, 

1. The probability distributions of the topics are then used as feature vectors in the Logistic Regression model for binary classification (bomb vs. non-bomb) on the validate data set. 
2. Thereafter, the trained LDA model is used to derive probability distributions of the topics from the test data. 
3. Run Logistic Regression model on these topic probability distributions, to see if model generalizes. 

The results looks promising: 

| Metrics         | Validate set | Test set |
| --------------- | ------------ | -------- |
| **accuracy**    | 0.5767       | 0.5958   |
| **sensitivity** | 0.8004       | 0.7806   |
| **roc_auc**     | 0.5957       | 0.6264   |



Next, the  topic probability distributions are added to the count vectorized word features for both train and test dataset. The dataset is then run through the Logistic Regression model to determine overall model generalizability.

| Metrics         | LR model | LR model (topic model vectors) | LR model (topic model + count vectorizer vectors) |
| --------------- | -------- | ------------------------------ | ------------------------------------------------- |
| **accuracy**    | 0.6859   | 0.5958                         | 0.5366                                            |
| **sensitivity** | 0.8610   | 0.7806                         | 0.8577                                            |
| **roc_auc**     | 0.7566   | 0.6264                         | 0.7060                                            |



## Recommendations (Part2)

From the model metric summaries, the model using topic distributions alone as feature vectors has the lowest performance scores (sensitivity and roc_auc). The addition of feature vectors from count vectorizer improved model sensitivity and roc_auc. Model generalizability using LDA topic distributions has been demonstrated, though the best performing model remains the production Logistic Regression model using count vectorized word features.

The approach applied in this project could work in general, for similar NLP-based classifiers.

---

## Future Work :briefcase:

Terrorism is a complex topic as it covers politics, psychology, philosophy, military strategy, etc. The current model is a very simplistic in that it classifies a terrorist attack mode as 'bomb' or 'non-bomb' based solely on one form of intel (motive text). Additional sources or forms of intel are not included, nor were political and social factors trends that could serve as supporting sources of intelligence.

I aim to discuss more regarding my learning journey through this project and will update with the blog link shortly. 

Here are a few areas that I would like to revisit for future project extensions:
- source for additional data to widen perspective
- feature engineer spatial and temporal aspects (e.g. attacks by region, attacks by decades)
- explore model performance using Tfidf vectorizer and spaCy
- explore other classification models (currently only 2 models explored; time allocated between studying the dataset variables, motive texts, longer than usual modeling times with the inherent size of the dataset, and research on topic modeling (LDA) and spaCy)

When I started out on this project, incorporating LDA into the model workflow was on the drawing board, but not considered a firm decision. LDA is an unsupervised machine learning technique and it hadn't dawned upon me that it could be used to augment supervised machine learning. Andrew  Ng's work on LDA, and Marc Kelechava's sentiment prediction on yelp reviews using LDA technique provided the inspiration on the potential possibilities of LDA.

Thanks for reading, and hopefully, the work has provided you some ideas on how best to tackle your own NLP project. I believe in paying it forward; the code hosted on github is intended to be shared and remixed. I appreciate attribution for the usage of the codes.

---

