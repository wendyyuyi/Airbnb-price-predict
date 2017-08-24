import gmplot
import pandas as pd
import pylab as pl
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import confusion_matrix
import pydotplus 
from IPython.display import Image 
import csv 


def verify(num):
	return ('float', 'int')[round(float(num)) == float(num)]

def isanum(str):
    try:
        float(str);
        return True;
    except ValueError:
        return False;


"""
with open('listing_clean.csv') as csvfile:
        #readCSV = csv.reader(csvfile, delimiter=',') 
        pickup_longs = [] 
        pickup_las = []
        dropoff_longs = []
        dropoff_las =[] 
        #for row in readCSV:
        for (i, row) in enumerate(csv.reader(open('listing_clean.csv'))):
            if(i != 0):
            	#if isanum(row[45]) == True and isanum(row[46]) == True:
                	pickup_long = float(row[3])
                	pickup_la = float(row[4]) 
                	pickup_longs.append(pickup_long) 
                	pickup_las.append(pickup_la) 
                #dropoff_long = row[9]
                #dropoff_la = row[10]
                #dropoff_longs.append(dropoff_long)
                #dropoff_las.append(dropoff_la)
                


"""
filename = 'datalistings_asheville.csv'


df = pd.read_csv(filename,delimiter  = ",")


lats = []
lons = []

lats= df['latitude']
lons= df['longitude']
#lats.append(df2['latitude'])
#lons.append(df2['longitude'])
#lats.append(df3['latitude'])
#lons.append(df3['longitude'])

# declare the center of the map, and how much we want the map zoomed in
gmap = gmplot.GoogleMapPlotter(0, 0, 2)
# plot heatmap


gmap.heatmap(lats, lons)

# save it to html
gmap.draw("Earthquake_heatmap.html")