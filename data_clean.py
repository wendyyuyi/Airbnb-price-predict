import pandas as pd
import pylab as pl
import numpy as np

filename ='output.csv'
features_notnum = [
    'id',
    'zipcode',
    'property_type',
    'room_type',
    'accommodates',
    'bedrooms',
    'beds',
    'bed_type',
    'number_of_reviews',
    'review_scores_rating',
    'availability_30',
    'minimum_nights',
    'bathrooms'
]

df = pd.read_csv(filename,delimiter  = "," , usecols = features_notnum+target )

###drop NA value###
for col in df.columns:
    print col + ', Number of Missing Values:', len(df[col][df[col].isnull()])
df = df.dropna(how='any')

df['zipcode'] = df['zipcode'].str.replace(r'[^-+\d.]', '')

###data clean####
df_list = list(df['price'])				#price
del_list = []
for i in range(len(df_list)) :
    if df_list[i][0] != '$' :
        del_list.append(df.index[i])
df = df.drop(del_list)

df['price'] = df['price'].str.replace(r'[^-+\d.]', '')   

df_list = list(df['bathrooms'])			#bathrooms
del_list = []
for i in range(len(df_list)) :
    if df_list[i].isalnum() != True :
        del_list.append(df.index[i])
df = df.drop(del_list)

df_list = list(df['bedrooms'])			#bedrooms
del_list = []
for i in range(len(df_list)) :
    if df_list[i].isalnum() != True :
        del_list.append(df.index[i])
df = df.drop(del_list)

df_list = list(df['beds'])				#beds
del_list = []
for i in range(len(df_list)) :
    if df_list[i].isalnum() != True :
        del_list.append(df.index[i])
df = df.drop(del_list)

df_list = list(df['minimum_nights'])	#minimum_nights
del_list = []
for i in range(len(df_list)) :
    if df_list[i].isalnum() != True :
        del_list.append(df.index[i])
df = df.drop(del_list)

df_list = list(df['availability_30'])	#availability_30
del_list = []
for i in range(len(df_list)) :
    if df_list[i].isalnum() != True :
        del_list.append(df.index[i])
df = df.drop(del_list)

df_list = list(df['zipcode'])			#zipcode
del_list = []
for i in range(len(df_list)) :
    if df_list[i].isalnum() != True :
        del_list.append(df.index[i])
df = df.drop(del_list)


#confirm all entries are float type
df['price'] = df['price'].astype(float)
df['zipcode'] = df['zipcode'].astype(float)
df['bathrooms'] = df['bathrooms'].astype(float)
df['bedrooms'] = df['bedrooms'].astype(float)
df['beds'] = df['beds'].astype(float)
df['minimum_nights'] = df['minimum_nights'].astype(float)
df['availability_30'] = df['availability_30'].astype(float)
df['number_of_reviews'] = df['number_of_reviews'].astype(float)
df['review_scores_rating'] = df['review_scores_rating'].astype(float)

#optimize data
df_list = list(df['review_scores_rating'])		#rating < 80
del_list = []
for i in range(len(df_list)) :
    if df_list[i] < 80 :
        del_list.append(df.index[i])
print 'delete rating < 80 : ',len(del_list) 
df = df.drop(del_list)

df_list = list(df['number_of_reviews'])			#rating num < 10
del_list = []
for i in range(len(df_list)) :
    if df_list[i] < 10 :
        del_list.append(df.index[i])
print 'delete rating num < 10 : ',len(del_list) 
df = df.drop(del_list)

df_list = list(df['price'])						#price > 200
del_list = []
for i in range(len(df_list)) :
    if df_list[i] > 200 :
        del_list.append(df.index[i])
print 'delete price > 200 : ',len(del_list) 
df = df.drop(del_list)

#do one hot encoding
room_dummies = pd.get_dummies(df['room_type'])
property_dummies = pd.get_dummies(df['property_type'])
bed_dummies = pd.get_dummies(df['bed_type'])

dummy_list = [df,room_dummies.astype(int),property_dummies.astype(int),bed_dummies.astype(int)]

df_concat = pd.concat(dummy_list,axis = 1)

#output csv 
df_concat.to_csv("output_clean_under200.csv")
        
print "done"