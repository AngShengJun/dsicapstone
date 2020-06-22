# Part 3: Data Cleaning & EDA

## Overview

This section discusses findings from data cleaning and EDA

---

## **Data cleaning** 

The GTD is encoded using ISO-8859-1 format. It consists of terrorist incidences dated 1970 to 2017. There are 181,691 observations and 135 features.

Treatment on missing values: 

- Owning to shifts in data collection over the years, there are several features with more than 100,000 missing values. These are reviewed and dropped except `motive` (required for modeling downstream). `motive` is added after 1997, it has approx. 50561 observations, still substantial mass for modeling needs.
- Columns that are assessed to be redundant or non-relevant were also dropped.
- Missing values in remaining columns were either imputed (based on contextual understanding from the GTD codebook) or dropped.
- Column names were shortened
- Textual data (except names of Country, Region and terrorist group names) were lowercased and shortened for brevity, where applicable.

## **Data dictionary for cleaned data**

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

## **EDA** :bar_chart:

- How have terrorist incidence varied over the years?
>A: Sharp increase in incident counts from 2012 onwards (new automated data collection, increased data source connectivity and terrorism trends). Incidences peak in 2014-2015. Highest casualties in 2001 (Sep 11 by AQ)(Fig.1).
>
>![Figure1](https://github.com/AngShengJun/dsicapstone/blob/master/misc/1.jpg)
- Which groups inflicted most casualties?
>A: 3062 groups recorded in dataset. In terms of highest wounded by individual incidents, AQ has highest (16,000 wounded; Sep 11) followed by Aum ShirinKyo (5,500 wounded; release of sarin in metro).  
>A: Top 5 most active groups: taliban, isil, sl, boko haram, al-shabaab. Emerging in 2015, isil has highest activity rate. (Fig.2)
>A: Top 5 groups inflicted highest casaulties: isil, taliban, AQ, boko haram, ltte.
>
>![Fig2](https://github.com/AngShengJun/dsicapstone/blob/master/misc/2.jpg)
- How have the attack modes evolved over time? Which attack mode account for highest casualties? Have target choice changed over the years? Which attack mode has highest successes?
>A: isil favored bombing, AQ conducted the least incidents, but accounted for high casualties through Sep 11. (Fig.3.1, 3.2) 
>
>![Fig3.1](https://github.com/AngShengJun/dsicapstone/blob/master/misc/3.1.jpg)
>
>![Fig3.2](https://github.com/AngShengJun/dsicapstone/blob/master/misc/3.2.jpg)
>
>There does not appear to be a fundamental shift in the general modes of attacks over the years. Bombing remains the favored tactic, followed closely by armed assault and kidnapping in more recent years. Bombing accounts for highest casualties (total); hijacking accounts for highest average casualties. (Fig.4.1, 4.2, 5)
>
>![Fig4.1](https://github.com/AngShengJun/dsicapstone/blob/master/misc/4.1.jpg)
>
>![Fig4.2](https://github.com/AngShengJun/dsicapstone/blob/master/misc/4.2.jpg)
>
>![Fig5](https://github.com/AngShengJun/dsicapstone/blob/master/misc/5.jpg)
>
>A: General populace and property remained top target of choice regardless of the years. (Fig.4.3, 4.4)
>A: Little publicized nuclear-related incidents (10 incidents in Japan by unknown perpetrator). I did not manage to uncover any further details regarding these incidents. (Fig.4.5)
>A: In general, all attackmodes has more successes than failures. By proportion, since bombing has highest proportion, it also has the highest number of successes. (Fig.6 )
>
>![Fig6](https://github.com/AngShengJun/dsicapstone/blob/master/misc/6.jpg)
- Which countries/region are the most targeted?
>A: Incidents mostly centered regions: South Asia, the Middle East & North Africa, Sub-Saharan Africa and SouthEast Asia. South Asia increasingly accounted for 50% of total yearly incidences since 2003 (due to taliban, maoist groups) (Fig.7.1, 7.2)
>
>![Fig7.1](https://github.com/AngShengJun/dsicapstone/blob/master/misc/7.jpg)
>
>![Fig7.2](https://github.com/AngShengJun/dsicapstone/blob/master/misc/7.2.jpg)
>
>A: Pakistan, Afgan, India, Colombia and Peru are top 5 most targeted. (Fig.8)
>
>![Fig8](https://github.com/AngShengJun/dsicapstone/blob/master/misc/8.jpg)
- What motives drive the tactics of terror groups?

>A: Combination of several pre-disposing factors such as social as well as ideological goals motivates terror groups. A common underlying theme is sectarian violence (Fig.9)
>
>![Fig9](https://github.com/AngShengJun/dsicapstone/blob/master/misc/9.jpg)

- Using spaCy dependency visualization, we can see that the motive words is generally structured as follows:

  > 1. Context (describes if part of series of events with source citation. If unknown, sources for hypothesis is stated.
  > 2. Group name (either claimed or identified by sources)/
  > 3. Goal of attack.
  > 4. Further sources or information to support context.
  >
  > ![Fig10](https://github.com/AngShengJun/dsicapstone/blob/master/misc/10.jpg)

------



