import sys
import csv
import pandas as pd
from subprocess import call
import os.path

"""
    i : create directories
    d : download files and unzip
    p : move the files from local to hadoop
    g : move the files from hadoop to local

"""

city_list = ['asheville','austin','boston','chicago','denver','los-angeles','nashville','new-orleans','new-york-city','oakland','portland','san-diego','san-francisco','santa-cruz-county','seattle','washington-dc']
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

if sys.argv[1] == '-i' :
    for city in city_list :
        call(['mkdir', city])

elif sys.argv[1] == '-d' :
    with open('dir.txt','r') as f :
        dir_name = f.readlines()

    with open('urls.txt','r') as f :
        urls = f.readlines()

    with open('name.txt','r') as f :
        file_names = f.readlines()

    with open('date.txt','r') as f :
        dates = f.readlines()

    cur_dir_index = 0
    cur_dir_name = dir_name[0]

    final_file = 'combined_listings.csv'
    ff = open(final_file,'w')

    for i in range(len(urls)) :

        if(dir_name[i] != cur_dir_name) :
            cur_dir_name = dir_name[i]
            cur_dir_index = cur_dir_index + 1

        if file_names[i].strip() == 'listings.csv.gz' :

            name = city_list[cur_dir_index] + '/' + dates[i].strip() + file_names[i]
            output_name = city_list[cur_dir_index] + '/' + dates[i].strip() + 'datalistings.csv'


            if os.path.isfile(output_name) :

                print output_name
                # this is the file
            else :
                print output_name + 'not exist'
        if i > 100 :
            break


    #call(['gzip','-d','*.gz'])
    #gunzip -c file.gz > /THERE/file
