import csv
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime


def get_data(path):
    file = open(path)
    data = csv.DictReader(file)
    return data


def get_registrations(data):
    year_registration={}
    for company in data:
        year = str(company["DATE_OF_REGISTRATION"])
        if len(year) == 8:
            year = year[6:]
            if int(year)>=0 and int(year)<=20:
                year = "20"+year
            else:
                year = "19"+year
        else:
            year = year[:4]
            
        year_registration[year] = year_registration.get(year,0) +1

        # for i in year_registration:
        #     print(i," : ",year_registration[i])
    return year_registration

def plot_graph(years,registrations):
    plt.bar(years, registrations)
    plt.xlabel('Year of Registration')
    plt.ylabel('No of Registrations')
    plt.title('Company Registrations by Year')
    plt.xticks(rotation=90)
    plt.show()


data = get_data("Maharashtra.csv")
year_registration = get_registrations(data)
years = list(year_registration.keys())
registrations = list(year_registration.values())
plot_graph(years,registrations)
    






















































# import csv
# from collections import defaultdict
# import matplotlib.pyplot as plt
# from datetime import datetime


# with open('Maharashtra.csv',newline='',encoding='ISO-8859-1') as csvfile:
#     data= csv.DictReader(csvfile)

#     year_registration={}
#     for company in data:
#         year = str(company["DATE_OF_REGISTRATION"])
#         if len(year) == 8:
#             format_string = '%d-%m-%y'
#         else:
#             format_string = '%y-%m-%d'
#         try:
#             year = datetime.strptime(company["DATE_OF_REGISTRATION"],format_string).year
#             # if(year == "2042"):
#             #     print(company["Company_Name"])
#             year_registration[year] = year_registration.get(year,0) +1
#         except:
#             pass

#     # for i in year_registration:
#     #     print(i," : ",year_registration[i])



#     years = list(year_registration.keys())
#     registrations = list(year_registration.values())

#     plt.bar(years, registrations)
#     plt.xlabel('Year of Registration')
#     plt.ylabel('No of Registrations')
#     plt.title('Company Registrations by Year')
#     for i, count in enumerate(registrations):
#         plt.text(i, count, str(count), ha='center', va='bottom')
#     plt.show()

















