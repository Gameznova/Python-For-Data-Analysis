# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:19:35 2023

@author: Gamez
"""
'''
FoodWheel is a startup delivery service that takes away the struggle of deciding where to eat! 
FoodWheel picks you an amazing local restaurant and lets you order through the app.

What cuisines does FoodWheel offer? Which areas should the company search for more restaurants to partner with?
How has the average order amount changed over time? What does this say about the trajectory of the company?
How much has each customer on FoodWheel spent over the past six months? What can this tell us about the average FoodWheel customer?
'''

from matplotlib import pyplot as plt
import pandas as pd
import os

print(os.listdir())

restaurants = pd.read_csv('restaurants.csv')

# How many different types of cuisine does FoodWheel offer?
cuisine_options_count = restaurants.cuisine.nunique()
print("Unique Opetions:", cuisine_options_count)

# Let’s count the number of restaurants of each cuisine. Use groupby and count. Save your results to cuisine_counts
cuisine_counts = restaurants.groupby('cuisine')\
                            .name.count()\
                            .reset_index()

print(cuisine_counts)

# create two variables cuisines and counts from groupby df
cuisines = cuisine_counts.cuisine.values
counts = cuisine_counts.name.values



plt.pie(counts,labels=cuisines, autopct="%d%%")
plt.title('% of Cuisines Share in Neighborhood')
plt.show()