# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 20:42:59 2021

@author: como2
"""

import Glassdoor_Scraper_Updated as gs
import pandas as pd 
path = "C:/Users/como2/Documents/Programming/Data_Science_Salary_Project/chromedriver.exe"

df = gs.get_jobs("data scientist",350, False, path, 5)

#df_analyst = gs.get_jobs("data analyst", 15, False, path, 5)

df
#df_analyst