# UP 206 Project Proposal

## Research Question
We are looking at the connection between government responses to the COVID-19 pandemic and willingness of citizens to receive the COVID-19 vaccine. This analysis will be conducted in the United States at the state-level. Over the course of the pandemic, we have seen varied responses at both the individual and government level to the pandemic, ranging from crisis response to hoax. This disparity has fallen primarily on the political spectrum, with right-wing politicians downplaying severity, not promoting individual caution, and speaking out against government shutdowns. Additionally, states run by left-leaning politicians often promoted weak stay-at-home orders, fearing disastrous enconomic downturn as a result of public health measures. As a result, government policies to the pandemic varied significantly from state to state. Distrust in the government to efficiently respond to the pandemic has turned into distrust around the vaccine. As vaccines become available, there remains hesistancy about their safety and efficacy. We are interested in understanding the relationship between government policies to the pandemic and views about the vaccine. 

## Data Sources
Our analysis will rely on two data sources:

* [Household Pulse Survey from the US Census Bureau](https://www.census.gov/data/experimental-data-products/household-pulse-survey.html)
* [Coronavirus Government Response Tracker from the University of Oxford](https://www.bsg.ox.ac.uk/research/research-projects/coronavirus-government-response-tracker#data)

The US Census Bureau created the Household Pulse Survey to track the social and economic effects of the pandemic on households. In particular, the survey asks respondants about their likelihood of recieving the COVID-19 vaccine. This dataset is available at the Metropolitan Statistical Area (MSA) level and the state level. We will conduct our analysis at the state level.

The University of Oxford created the Coronavirus Government Response Tracker collects information on government responses to the pandemic and uses 18 indicators (such as school closures and travel restrictions) to classify the level of government response over the course of the pandemic. This dataset is available at the state-level in the US. 

## Methodology
First, we will download our data, inspect, and clean our two datasets. Then, we will spatializing explore each dataset. We will map different variables at the state-level and look for patterns and areas for further inquiry. Second, we will merge the data by state, so we have one working dataset. Then, we will conduct statistical tests to find correlations between variables in each dataset. We are especially interested in examining any correlations between governmental COVID-19 policies and COVID-19 vaccination views. However, we will also investigate the relationship between COVID-19 views and potential confounders, such as age, race, income, and education. If appropriate, we will conduct multilevel modeling. Finally, we will create visualizations of the datasets to display any correlations.  <br>

Visualizations could include: 
* an interactive dashboard that allows the user to select variables from each dataset and display them on a map
* static graph showing the correlation between government response and COVID cases
* static graph showing the party of state governor and willingness to take the vaccine

![flowchart](https://github.com/laharps/up206-groupproject/blob/main/Group%20Assignments/images/206a_assigment1.jpg)

## Conclusion
We hope this analysis will reveal how government policy responses to the pandemic may have influenced opinions around the vaccine. Additionally, we hope to see how government response and vaccine willingess correlate with COVID-19 cases and political party. We anticipate seeing a stark divide between red states and blue states with respect to government responses and vaccine willingness. We hope that our findigns will help illiminate which elements of govermental action have fuel individual distrust in goverment, so that in the future, we are able to hold our officals more accountable for their actions. 

