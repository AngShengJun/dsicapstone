# Part 4: Modeling, Evaluation & Recommendations

## Overview

On the building of classifier models, several were explored and their performance measures were reported below:

| Metrics                 | LogReg | KNN   | DecisionTree | RandForest* | GradientBoost | XGB   |
| ----------------------- | ------ | ----- | ------------ | ----------- | ------------- | ----- |
| **accuracy (validate)** | 0.945  | 0.933 | 0.799        | 0.856       | 0.910         | 0.908 |
| **sensitivity**         | 0      | 0.088 | 0.672        | 0.657       | 0.226         | 0.270 |
| **precision**           | 0      | 0.300 | 0.161        | 0.217       | 0.196         | 0.213 |
| **F1**                  | NaN    | 0.122 | 0.261        | 0.326       | 0.210         | 0.238 |
| **roc_auc**             | 0.791  | 0.672 | 0.774        | 0.862       | 0.837         | 0.849 |

*RandForest (undersampling + oversampling), other models (oversampling)

As the proportion of wnv  to none wnv is approx. 5%-95%, this is an imbalanced class problem. The team utilized resampling techniques (SMOTE) to mitigate imbalanced class for machine learning. F1 score and ROC_AUC are used to evaluate the best model. The team picked both the Randforest and XGBoost models as the production model for Kaggle submissions.

The returned Kaggle (Public scores):

- XGBoost (Undersampling SMOTE): 0.74579

- RandomForest (Oversampling and Undersampling SMOTE): 0.73774

  The team further explored Undersampling and Oversampling (SMOTE) with XGBoost classifier.

The resulting scores are:

| Metrics          | Random Forest (Under + Oversample SMOTE) | XGBoost (Under + Oversample SMOTE) |
| ---------------- | ---------------------------------------- | ---------------------------------- |
| **roc_auc(val)** | 0.856                                    | 0.846                              |
| **sensitivity**  | 0.657                                    | 0.613                              |
| **precision**    | 0.217                                    | 0.196                              |
| **F1**           | 0.326                                    | 0.297                              |
| **roc_auc**      | 0.862                                    | 0.855                              |

With combination of Oversample and Undersample on the XGBoost classifier, 

the Kaggle (Public score) improved: **0.75410**

**<u>Recommendations and Way Forward.</u>**

Pesticide deployment: To improve cost-effectiveness of pesticide deployment, the proposed recommendations relies on timing and coverage area:

1. Spraying should be focused in the months of Jun to Jul (periods of high rainfall), and targeted at region of traps (see presentation slides) with high wnv as a start.

2. Moving forwards, the deployment should be tailored accordingly to match rainfall patterns; mosquito population generally spike 2 weeks after heavy rainfall.

3. The classifier model could be used to provide insights to areas for targeted spraying in the longer term, as new data on wnv clusters, and weather data is available.

---

## Annex Guide

1. An executive summary:
  - What is your goal?
  - Where did you get your data?
  - What are your metrics?
  - What were your findings?
  - What risks/limitations/assumptions affect these findings?
2. Summarize your statistical analysis, including:
  - implementation
  - evaluation
  - inference
3. Clearly document and label each section of your notebook(s)
  - Logically organize your information in a persuasive, informative manner.
  - Include notebook headers and subheaders, as well as clearly formatted markdown for all written components.
  - Include graphs/plots/visualizations with clear labels.
  - Comment and explain the purpose of each major section/subsection of your code.
  - Document your code for your future self, as if another person needed to replicate your approach.
4. Clearly document all of your decision points in the relevant sections
  - How did you acquire your data?
  - How did you transform or engineer your data?  Why?
  - How did you select your model?
  - How did you optimize hyperparameters?
5. Host your notebook and any other materials in your own public Github Repository.
  - You repo should have README file that guides us through the repository and links to important files.
  - Include links and explanations to any outside libraries or source code used.
  - Host a copy of your dataset or include a link to a remotely hosted version.

**BONUS**

Create a blog post of at least 1000 words summarizing your approach in a tutorial format and link to it in your notebook.  In your tutorial, address a slightly less technical audience; think back to Day 1 of the program - how would you explain and walk through your capstone project to your earlier self?

### Best Practices

1. The README
  - The README is the landing page of your repo.  
  - It should start with a summary of what the repo contains and provide links to important files.
  - Think of it as a table of contents for your repo.
  - You should list the external libraries/packages that you use, especially if they are not standard (i.e., not part of the base Anaconda distribution.)
  - If you wrote a blog about this project, link to it from your README.
  - Include your website, twitter handle, etc., if you would like.
2. Organizing your repo
  - If you have multiple notebooks, start each filename with a number to assist in organization.
  - Give you notebooks descriptive filenames.  For example,
    - `1_Scraping.ipynb`
    - `2_EDA.ipynb`
    - `3_Model_Development.ipynb`
  - Keep data files in a single folder off the "root" of the repo.
  - Keep documentation/reports in a dedicated folder (like data).
  - If you have any other resources (images or PDFs), keep them in a dedicated folder (called `assets`, for example.)
3. Jupyter Notebooks
  - Data science is a non-linear, iterative process, but your final notebook should contain a linear "narrative."
  - Notebooks should be reproducible, which means that I will get the _same results_ as you did if I clone your repo and run your notebook.  Consider the following:
    - Is your data stored in the repo or available via a link?
    - If you use _any_ (_ANY_) random numbers anywhere, do you have a random seed so that you **always** get the same result?
    - Is your notebook 100% free of runtime errors?
    - In short, if I open your notebook and click "Cell -> Run All", will your notebook run completely, without errors and give me the same result _every_ time?

## Necessary Deliverables / Submission

Your code and technical notebook should be posted to your **personal GitHub** (not **git.generalassemb.ly**) and linked to us no later than  _end of day, June 11, 2020_.

## Useful Resources

- [How to Report Statistics to Technical Audiences](http://abacus.bates.edu/~ganderso/biology/resources/writing/HTWstats.html)
- [What is a good way for a data scientist to construct an online portfolio?](https://www.quora.com/What-is-a-good-way-for-a-data-scientist-to-construct-an-online-portfolio)
