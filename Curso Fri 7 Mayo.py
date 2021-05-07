#Clean the ‘sales.csv’ dataset:
#
#
#- The CustomerNumber is a float64 but it should be an int64
#- The value2016 and value2017 columns are stored as objects, not numerical values such as a float64 or int64
#- PercentGrowth and JanUnits are also stored as objects not numerical values
#- We have Month , Day and Year columns that should be converted to datetime64
#- The Active column should be a Boolean 
#- The Region column should be a category

# Ejercicio 10 
# Python_Data_Cleaning_Immune_v3.1 EN.pdf

import re
import pandas as p


df = p.read_csv("sales.csv")
