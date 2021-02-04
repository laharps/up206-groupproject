# Project Proposal: Walkability of Vaccine Distribution Locations in New York City
by Lauren Harper and Nataly Rios

## Research Question
<p> Are COVID-19 vaccine locations accessible by walking to neighborhoods that were hit the hardest by COVID-19? And are COVID-19 vaccine locations accessible to vulnerable demographics? </p >

<p> While New York City has more robust public transportation than most American cities, our analysis will focus strictly on access to vaccine distribution sites by walking. First, many New Yorkers do not own cars. Second, using public transportation or a taxi is a possible site of exposure to or transmission of COVID-19. We want to know not only where vaccine distribution centers are concentrated, but also who can access the sites within a 15-20 minute walk. We will look at the demographics of surrounding neighborhoods, including race, age, ability, and income, as well as the number of cases reported in that neighborhood. Our goal is to determine whether vaccine distribution sites are easily accessible by walking to the most vulnerable demographics in the city. </p>

## Data Sources
* <b>NYC COVID-19 Vaccination Sites:</b> NYC provides a list of all of their COVID-19 vaccination locations via [this ArcGIS Online webmap.](https://vaccinefinder.nyc.gov/locations)
* <b>NYC COVID-19 Case Rates:</b> We will download COVID-19 cases per zip code  directly from NYC’s Department of Health Github page. It can be accessed [here.](https://github.com/nychealth/coronavirus-data/blob/master/totals/data-by-modzcta.csv)
* <b> NYC 2015-2019 ACS Census Tract Demographic Data:</b> We will be downloading ACS demographic data about race/ethnicity, age, income, education, and disability status directly from the [census reporter.](https://censusreporter.org/)

## Methodology
To answer these questions, we will first create isochrones for all New York City COVID-19 vaccination sites to show 15-minute walksheds for each site. In order to define “hardest-hit neighborhoods," we will convert the COVID-19 case rate data to quintiles and flag any zip code that falls in the highest quintile. We will then map both the 15-min walk polygons and the hardest hit COVID-19 neighborhoods to visually examine whether or not the neighborhoods with the highest cases of COVID-19 are within a walking distance to COVID-19 vaccination sites. After, we will conduct a spatial joint to link the 15-min walk polygons to their corresponding zip code. We will use this spatial join to add a flag to each zip code that falls within a 15 min walk from a zip code location. We will then compare the sociodemographic characteristics of the zip code tracts that are within walking distance from COVID-19 case sites to those that are not within walking distance. Additionally, we will examine the prevalence of vulnerable populations within COVID-19 within a walking distance to COVID-19 sites. Since we will only be utilizing ACS data to identify vulnerable populations, we will look at the prevalence of people over 65, as well as Black and Lantix individuals since they have been the demographic groups hit the hardest by COVID-19 in New York City.

## Conclusion
As vaccines become more available for a wider portion of the population, it is vital that vaccine distribution sites be easily and safely accessible, particularly for the hardest hit communities. We hope this analysis will reveal locations where new vaccine distribution sites can prioritize serving vulnerable demographics. 
