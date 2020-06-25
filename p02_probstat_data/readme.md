# Part 2: Problem Statement &  Dataset Information

## Overview

This section elaborates on the project chosen, problem statement,  the goal of the model, and the data used to explore that model.

## Problem Statement

**Context:** Terrorist attacks have led to loss of innocent lives and properties over the years. Though the threat from terrorism has somewhat abated with Covid-19 situation, it would be wise to be remain prepared and vigilant. Terrorism is defined as (further literature review are detailed in **Annex A**): 

> "The threatened or actual use of illegal force and violence by a non-state actor to attain a political, economic, religious, or social goal through fear, coercion, or intimidation." - Global Terrorism Database
>
> An incident must possess all three attributes to be considered as a terrorism event:
>
> - The incident must be intentional (conscious calculation on the part of a perpetrator).
> - The incident must entail some level of violence or immediate threat of violence -(on property, people).
> - The perpetrators of the incidents must be sub-national actors. GTD  does not include acts of state terrorism.

Counter terrorism relies on intelligence to foil terror incidents. However, the analysis of such intel data requires much manpower and training, and the amount of intel data collected has seen exponential growth with technological advancements over the years. 

Illustration of Global Terror Incidents year 2000-2017

![Gif](https://github.com/AngShengJun/dsicapstone/blob/master/misc/output_hMJYEE.gif)

**Proposed Solution:** 

- A machine learning model is proposed to classify bombing (alternative knife; subject to tailor as more insights uncovered with EDA) attacks. It is hypothesized that bombing accounts for the highest casualties per attacks.  Such a model is expected to support intelligence analyst and alleviate their workload.

- At this point of time, the proportion of class of interest is expected to be imbalanced; therefore, the guiding metric would be **F1** score and **area under the ROC curve**. The model will be benchmarked against the baseline of class proportion. Having utilized NLP techniques to build text classification models in Project 3(Web API and classification of Subreddit posts), I intend to explore other NLP tools and techniques such as spaCy and Topic Modeling.  I will also use Latent Dirichlet Allocation (LDA to uncover) insights regarding the topics of the terrorist's motive and (LDA) model to classify terrorist attack modes based on a provided motive input, if possible.

- I will also review and propose recommendations on: 
  1. the features that influences the model's classifications for further fine-tuning of model
  
  2. exploration of other modelling methods ​that could improve the model's performance. 
  
     
  
  Data source: The Global Terrorism Database (GTD) is an open-source database on terrorist attacks around the world from 1970 through 2017. It includes both domestic and international terrorist incidents, and more than 100 variables on the location, tactics, perpetrators, targets, and outcomes. The database is maintained by the "National Consortium for the Study of Terrorism and Responses to Terrorism (START), University of Maryland. (2018). Link for database: https://www.kaggle.com/START-UMD/gtd

**Potential Challenges :warning:/ Mitigations & Considerations:**

- Initially considered, a regression model to predict casualties may be feasible but not implementable in real world context (i.e. model prediction output are based on post-incident data). Having discussed with the Instructor, we are of view that the forecasting of incidents requires time-critical intel and reliable sources. In this regard, Classifier models would have better value proposition in providing insights on motives and MO with respect to different perpetrator groups for CT-efforts.
- Considering the legacy and context of records, it is foreseen that there may be numerous missing or empty entries where data is simply not available.
- Care must be exercised in interpretation of trends over time; Global patterns are driven by diverse trends in particular regions, and data collection is influenced by fluctuations in access to media coverage over both time and place.

**Project technical readiness assessment:** A classifier model is assessed to be feasible within the time constraints (3 weeks.) 

------

## Data Set Information

**Observations from the GTD codebook (data dictionary)​ :book:**

- Salient points regarding the structure and organization of the GTD are recorded below.

- <u>Terrorism incidents excluded from GTD</u>. These data were lost prior to START’s compilation of the GTD from multiple data collection efforts. Due to the challenges of retrospective data collection for events of more than 25 years ago, recollected 1993 incidences accounts for only 15% of estimated attacks. Therefore, they were dropped entirely to prevent users from misinterpreting the low frequency in 1993. 

- <u>Caution in interpretation of trends over time</u> :chart:. While the GTD team has applied a single definition of terrorism over the full span of the database, access to source materials and the efficiency of workflows have varied over time. Differences in levels of attacks and casualties before and after January 1, 1998; April 1, 2008; and January 1, 2012 may be partially explained by shifts in data collection.

- <u>New variables added GTD (post-1997).</u> These variables were added due to shifts in data collection effort. Wherever possible, values for these new variables were retroactively coded for the original incidents. For any newly added variables that were not retroactively coded and thus only exist for post-1997 cases, these were annotated with the following:
  Note: This field is presently only systematically available with incidents occurring after 1997.

- <u>Current Data Collection Methodology (2012-present).</u> The availability of valid source documents varies considerably, often over time and by location. Hence, the GTD team assesses the quality of the sources for updates. The GTD team prioritizes **High-quality sources** that are:

  - Independent: free of influence from the government, political perpetrators, or corporations
  - Routinely report externally verifiable content

  Information must be documented by at least one high-quality source to be recorded in the GTD.

- <u>Automated classification implemented in 2012.</u> The dramatic increase in the total number of worldwide terrorist attacks over 2011 likely reflects a **combined effect** of recent patterns of terrorism and automated data collection approaches. The exponential increase of available source materials has allowed for the collection of more comprehensive data on terrorism than any previous effort. 

- Additional information of terrorism incident definition is recorded in Annex A.

  ​																																											[Next](https://github.com/AngShengJun/dsicapstone/tree/master/p03_dataclean_eda)

---

## Annex A (Literature Review)

In addition to the three attributes for terrorisms definition, GTD specifies at least two of the following three criteria must be present for an incident for inclusion:

- Criterion 1: The act must be aimed at attaining a political, economic, religious, or social goal. In terms of economic goals, the exclusive pursuit of profit does not satisfy this criterion. It must involve the pursuit of more profound, systemic economic change.
- Criterion 2: There must be evidence of an intention to coerce, intimidate, or convey some other message to a larger audience (or audiences) than the immediate victims. It is the act taken as a totality that is considered, irrespective if every individual involved in carrying out the act was aware of this intention. As long as any of the planners or decision-makers behind the attack intended to coerce, intimidate or publicize, the intentionality criterion is met.

- Criterion 3: The action must be outside the context of legitimate warfare activities. That is, the act must be outside the parameters permitted by international humanitarian law, insofar as it targets non-combatants.

  ------

  