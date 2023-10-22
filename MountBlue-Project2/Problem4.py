import csv
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime

with open('Maharashtra.csv', newline='', encoding='ISO-8859-1') as csvfile:
    company_registrations = {}
    data = csv.DictReader(csvfile)
    principals_list = []
    
    for company in data:
        year = str(company["DATE_OF_REGISTRATION"])
        
        if len(year) == 8:
            year = year[6:]
            if 0 <= int(year) <= 20: 
                year = "20" + year
            else:
                year = "19" + year
        else:
            year = year[:4]
        
        principal = company["PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"]


    #get the year and check if it in in last 10 years or not
        if year != "NA" and int(year) >= 2011 and int(year) <= 2021:
            if(year not in company_registrations.keys()):
                company_registrations[year]={}
            company_registrations[year][principal] = company_registrations[year].get(principal,0) +1

            
    #after getting each principal business frequency then make a new temporary dic for sorting the dic inside a dictionary
    #this should be done for all the sub dictionaries

    for each_company in company_registrations:
        new_dic = company_registrations[each_company]
        #this line sort sub dic by sort by values.
        new_dic = dict(sorted(new_dic.items(),key = lambda x:x[1],reverse=True))


        # top_5 is temporrary dictionary
    #run a loop for 5 times and add the 1st 5 values into the temporary dictionary

        top_5 = {}
        cnt = 1
        for company in new_dic:
            top_5[company]=new_dic[company]
            if cnt==5:
                break
            else:
                cnt+=1
        #assign the temporary dictionary to the original one 

        company_registrations[each_company] = top_5
        #now for each year there will top 5 companies in its values

    for company in company_registrations:
        print("------Year",company)
        for i in company_registrations[company]:
            print(i,company_registrations[company][i])



    years = list(company_registrations.keys())
    companies = list(company_registrations[years[0]].keys())

    # Set the width and positions for the bars
    width = 0.2
    x = range(len(years))

    plt.figure(figsize=(12, 6))

    # Loop through the years and plot bars for each company
    for i, company in enumerate(companies):
        company_counts = [company_registrations[year].get(company, 0) for year in years]
        plt.bar([pos + i * width for pos in x], company_counts, width=width, label=company)

    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.title('Company Registrations Over Time')
    plt.xticks([pos + 1.5 * width for pos in x], years)
    plt.legend(loc='upper right', title='Business Principles')
    plt.show()

