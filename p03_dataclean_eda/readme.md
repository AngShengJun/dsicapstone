# Data Cleaning & EDA

## Overview

This section discusses findings from data cleaning and EDA

---

## Findings

**Data cleaning**

The GTD us encoded using ISO-8859-1 format. It consists of terrorist incidences dated 1970 to 2017. There are 181,691 observations and 135 features.

Treatment on missing values: 

- Owning to shifts in data collection over the years, there are several features with more than 100,000 missing values. These are reviewed and dropped except `motive` (required for modeling downstream). `motive` is added after 1997, it has approx. 50561 observations, still substantial mass for modeling needs.
- Columns that are assessed to be redundant or non-relevant were also dropped.
- Missing values in remaining columns were either imputed (based on contextual understanding from the GTD codebook) or dropped.
- Column names were shortened
- Textual data (except names of Country, Region and terrorist group names) were lowercased and shortened for brevity, where applicable.

**Data dictionary for cleaned data**

- | Column name/ Datatype                     | Explanation                                                  |
  | :---------------------------------------- | ------------------------------------------------------------ |
  | **eventid** [integer]                     | Incidents from the GTD follow a 12-digit Event ID system.<br/>• First 8 numbers – date recorded “yyyymmdd”.<br/>• Last 4 numbers – sequential case number for the given day |
  | **iyear, imonth, iday** [integer]         | year, month, day of incidents                                |
  | **country, region** [object]              | name of country, geographical region of incident             |
  | **lat, lon** [float]                      | geographical coordinates of incident                         |
  | **crit1,2,3** [integer]                   | Categorical variable. Inclusion criteria, allows users to filter out those incidents whose inclusion was based on a criterion which they believe does not constitute terrorism proper.<br/>• crit1: act must be aimed at attaining a political, economic, religious, or social goal.<br/>• crit2: act with intention to coerce, intimidate, or convey some other message to a larger audience (or audiences)<br/>• crit3: act is outside the context of legitimate warfare activities; targets non-combatants (i.e. the act contravenes International Humanitarian Law as reflected in the Additional Protocol to the Geneva Conventions of 12 August 1949 and elsewhere)<br/> **1** : meets criterion<br/> **0** :  does not meet criterion |
  | **success** [integer]                     | Categorical variable. Whether or not the attack type took place.<br/> **1** : Yes<br/> **0** :  No |
  | **suicide** [integer]                     | Categorical variable. Coded “Yes” in those cases where there is evidence that the perpetrator did not intend to escape from the attack alive. <br/>**1** : Yes<br/> **0** :  No |
  | **atkmode** [object]                      | General method of attack and often reflects the broad class of tactics used. Nine categories: 'assassination', 'hostage kidnap', 'bombing', 'armed assault', 'facility attack', 'hijack', 'unarmed assault', 'hostage taking', 'unknown'. |
  | **targtype, targnat,** **gname** [object] | - General type of target/victim. 22 categories: 'citizens and property', 'diplomats', 'journalists', 'police', 'military', 'general', 'education', 'business', 'party', 'unknown', 'transportation', 'utilities', 'airtransport', 'religion rep', 'telecommunication', 'food/water', 'ngo', 'T/VNSA', 'other', 'tourists', 'maritime', 'abortion related'.<br/>- Nationality of target<br/>- Name of group that carried out the attack |
  | **motive** [object]                       | When reports explicitly mention a specific motive for the attack, this motive is recorded in the `motive` field. This field may also include general information about the political, social, or economic climate at the time of the attack if considered relevant to the motivation underlying the incident. |
  | **indiv** [integer]                       | Categorical variable. Coded “Yes” if attack was carried out by an individual or several individuals not known to be affiliated with a group or organization alive. <br/>**1** : Yes<br/> **0** :  No |
  | **weaptype** [object]                     | Categorical variable. General type of weapon used in the incident. It consists of the following categories: <br/>'unknown', 'explosives', 'firearms', 'incendiary', 'chemical', 'melee', 'sabotage equipment', 'vehicle', 'fake weapons', 'radiological', 'other', 'biological'. |
  | **nkill, nwound** [integer]               | Number of fatalities, Number of wounded from incident.       |
  | **property** [integer]                    | Categorical variable. Coded “Yes” if there is evidence of property damage from the incident. <br/>**1** : Yes<br/> **0** :  No |

**EDA**

Prelim thoughts for EDA

- Visually explore the dataset for insights:
  - Which countries/region are the most targeted?
  - Which countries/region have most casualties?
  - How have the casualties changed over time?
  - How have the mode of attacks evolved over time?
  - Are countries more adapt at countering certain mode of attacks?



------

## Annex B (For Reference)

## Data Guidelines

What should you thinking about and looking for as you collect your capstone data?

- Source and format your data
  - Create a data dictionary to accompany your data.
- Perform initial cleaning and munging.
  - Organize your data relevant to your project goals.
  - Write functions to automatically clean and munge data as necessary.
  - Take copious notes, for both others and yourself, describing your assumptions and approach.


## EDA Guidelines

Think about the following as you perform your initial EDA.

- Identify the data types you are working with.
- Examine and summarize the distributions of your data, numerically and/or visually.
- Identify outliers.
- Identify missing data and look for patterns of missing data.
- Describe how your EDA will inform your modeling decisions and process.

### BONUS

- Create roadmap of your project with milestones.
- Write a blog post on what you learned from your EDA (pending github posting upon graduation).

## Useful Resources

- [Best practices for data documentation](https://www.dataone.org/all-best-practices)
- [Describing data visually](http://www.statisticsviews.com/details/feature/6314441/Visualising-Statistics-The-importance-of-seeing-not-just-describing-data.html)
- [WSJ Guide to Information Graphics (book)](https://www.amazon.com/Street-Journal-Guide-Information-Graphics/dp/0393347281)
- [Storytelling with Data (book)](https://www.amazon.com/Storytelling-Data-Visualization-Business-Professionals/dp/1119002257/)

------

Capstone-Check-in pointers

1. Do you have data fully in hand and if not, what blockers are you facing?
2. Have you done a full EDA on all of your data?
3. Have you begun the modeling process? How accurate are your predictions so far?
4. What blockers are you facing, including processing power, data acquisition, modeling difficulties, data cleaning, etc.? How can we help you overcome those challenges?
5. Have you changed topics since your lightning talk? Since you submitted your Problem Statement and EDA? If so, do you have the necessary data in hand (and the requisite EDA completed) to continue moving forward?
6. What is your timeline for the next week and a half? What do you _have_ to get done versus what would you _like_ to get done?
7. What topics do you want to discuss during your 1:1?

