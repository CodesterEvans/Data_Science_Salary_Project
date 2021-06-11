# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 20:42:59 2021

@author: como2
"""

import Glassdoor_Scraper as gs
import pandas as pd 
path = "C:/Users/como2/DocumentsP/rogramming/Data_Science_Salary_Project"

df = gs.get_jobs("data scientist", 15, False, path, 15)