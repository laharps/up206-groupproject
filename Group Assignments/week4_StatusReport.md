# Project Proposal Update 

### by Lauren Harper and Nataly Rios 

<p>We, unfortunately, learned that the data we originally planned to utilized was not available. For this week, we will be describing two new potential ideas for our midterm and final project. We are really excited about our first idea, but we are unsure of the feasibility, so we want to ensure we have a plan in case we determine that we can not do the project after meeting with Yoh this week. </p>
For more information about our original proposal, please click [here](https://github.com/laharps/up206-groupproject/blob/main/Group%20Assignments/Group%20Assignment%201.md).

## Idea 1 
### NYC COVID-19 Vaccination Site Access

### Roles 
<p> Harper: Data Wrangler Master: Explore ways to access COVID-19 site information and transform the data into a workable format. 

<p> Nataly: Statistician Extraordinaire: Explore the relationship between COVID-19 cases and COVID-19 vaccination sites. 

### Status Update
We are starting off with a new idea since the data we were hoping to use for our previous proposal is not available (there was a typo in the documentation and they didn’t start collecting the data until Januray 2021, not 2020!). 

Our new study questions are as following:

Are COVID-19 vaccine locations accessible by walking to neighborhoods that were hit the hardest by COVID-19? 
And Are COVID-19 vaccine locations accessible to vulnerable demographics? 

To answer these questions, we will first create isochronous maps for all of New York City COVID-19 vaccination sites to illustrate which areas have sites within a 20-minute walk. In order to define “hardest-hit neighborhoods, we will convert the COVID-19 case rate data to quintiles and flag an zip code that falls in the highest quintile. We will then map, both the 20-min walk polygons and the hardest hit COVID-19 neighborhoods to visually examine whether or not the neighborhoods with the highest cases of COVID-19 are within a walking distance to COVID-19 vaccination sites. After, we will conduct a spatial joint to link the 20-min walk polygons to their corresponding zip code. We will use this spatial join to add a flag to each zip code tract that falls within a 20 min walk from a zip code tract location.  We will then compare the sociodemographic characteristics of the zip code tracts that are within walking distance from COVID-19 case sites to those that are not within walking distance. Additionally, we will examine the prevalence of vulnerable populations within COVID-19 within a walking distance to COVID-19 sites. Since we will only be utilizing ACS data to identify vulnerable populations, we will look at the prevalence of people over 65, as well as Black and Lantix individuals since they have been the demographic groups hit the hardest by COVID-19 in New York City. 


### Data Update
* <b> NYC COVID-19 Vaccination Sites </b> NYC provides a list of all of their COVID-19 vaccination locations via  [ArcGIS Online webmap](https://www.arcgis.com/home/webmap/viewer.html?useExisting=1&layers=1e7c164f55014dd4a89a7c4add163eab). Please see the concerns section for comments on this dataset. 
* <b> NYC COVID-19 Case Rates </b> We will be downloading ZCTA COVID-19 case data directly from NYC’s Department of Health Github page. It can be accessed [here](https://github.com/nychealth/coronavirus-data/blob/master/totals/data-by-modzcta.csv). 
* <b> NYC 2015-2019 ACS Census Tract Demographic Data</b> We will be downloading \ACS demographic data about race/ethnicity, age, income, education, and disability status directly from the [census reporter.](https://censusreporter.org/)



### Concerns
We have two main concerns about the feasibility of this project. 

Currently, there is no CSV file (or any other data type), to access the COVID-19 vaccination site data. The data, however, is hosted in an [ArcGIS Online webmap](https://www.arcgis.com/home/webmap/viewer.html?useExisting=1&layers=1e7c164f55014dd4a89a7c4add163eab). For some initial research, it seems like it might be possible to use the ArcGIS Python API to access the webmap dataset for our project. However, the ArcGIS Python API requires running Jupyter Notebook on desktop, which is an additional challenge, and we are not positive that the API will allow us to use the dataset as we need for the project. We are hoping to meet with Yoh this week to discuss this. 
We are also worried about the feasibility of running isochrones for all 100 vaccines sites in NYC or, at least for even just two counties. If it is not possible to do the analysis at the borough level, our backup plan is to do the analysis on the zipcodes hit the hardest by COVID-19. The information for those sites can be found [here.](https://www1.nyc.gov/site/neon/programs/covid-neighborhoods.page)

## Idea 2
### Air Quality and Vehicle Miles Traveled in 2020
Examine trends between air quality by county and reduction of Vehicle Miles Traveled (VMT) during the first part of the pandemic. 

### Roles 
<p> Harper: Data Wrangler Master: Cleaning and presenting the data

<p> Nataly: Statistician Extraordinaire: Creating beautiful and meaningful tables and analytics

### Status Update
We are currently exploring options with this project. We have decided to look at the state of California with the county as our unit of analysis. The VMT data is published only by county, so that is the lowest level of analysis possible. While the VMT data covers January - August 2020, we will conduct our analysis on VMT and air quality data from January - June 2020, in order to avoid air quality impacts of the megafires from July-September 2020. We hope to explore the relationship between decreased VMT and improved air quality directly before and during the initial part of the pandemic. The resulting visualizations could be percent change in air quality by county, percent change in VMT by county, as well as overlays of racial and income demographics of the county. 

### Data Update
* <b> Vehicle Miles Traveled: </b> Streetlight has provided traffic metrics for free to researchers over the course of the pandemic. Dr. Ong has provided us with a VMT dataset (.csv) that includes daily VMT totals per county for the entire nation, from January 1st to August 2nd, 2020. 

* <b> Air Quality Data: </b> Using the [EPA Air Quality data](https://www.epa.gov/outdoor-air-quality-data/download-daily-data), we can look at daily AQI by county in the US. Rather than downloading a massive dataset, we may also want to use the [AirNow AP](https://docs.airnowapi.org/about) in order to access daily Air Quality Index (AQI) per county.


### Concerns
Our main concern is that the county-level analysis will not be granular enough to see significant correlation between VMT and air quality. We might scale the project up from California to the United States since both datasets have county-level datasets for the entire country. This might result in more significant regional differences. 
