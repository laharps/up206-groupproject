#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt
import numpy as np
from shapely import wkt
import plotly.express as px

from numpy import nan


# In[2]:


nyc_ztca_demdata=gpd.read_file('/home/jovyan/206a assigment/Midterm/nyc_ztca_demdata.geojson')
nyc_ztca_demdata.head()


# In[3]:


nyc_ztca_demdata.columns.to_list()


# In[4]:


columns_to_keep=['zcta',
 'Percent Non Hispanic',
 'Percent Hispanic',
 'Percent Non Hispanic White',
 'Percent Non Hispanic Black',
 'Percent Non Hispanic American Indian and Alaska Native',
 'Percent Non Hispanic Asian',
 'Percent Non Hispanic Native Hawaiian and Other Pacific Islander',
 'Percent Non Hispanic Some other race',
 'Percent Non Hispanic Two or more races',
  'Percent with Disabilities',
 'Percent Over 65',
 'Percent Living in Poverty',
 'Percent_ForeignBorn',
 'Percent_LessHSDiploma',
 'Percent_bachelorsbeyond']

nyc_dem_trimmed=nyc_ztca_demdata[columns_to_keep]
nyc_dem_trimmed.head()


# In[5]:


vacc_walk=gpd.read_file('/home/jovyan/206a assigment/Midterm/vac_walk.geojson')
vacc_walk.head()


# In[6]:


gdf= vacc_walk.merge(nyc_dem_trimmed, on='zcta')
gdf.head(2)


# In[7]:


gdf.columns.to_list()


# In[8]:


gdf.plot()


# In[10]:


gdf.to_file('gdf.geojson', driver='GeoJSON')


# In[ ]:




