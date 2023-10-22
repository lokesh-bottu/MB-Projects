import matplotlib.pyplot as plt
import csv
from collections import defaultdict


def get_data():
    file = open("umpires.csv")
    umpires = csv.DictReader(file)  
    return umpires

def get_umpires_country(umpires):
    umpire_country = {}
    for person in umpires:
        country = person[" country"]

        #get the umpires country and then compare it with india if it is not india then only we will proceed further
        if country != " India":
            umpire_country[country] = umpire_country.get(country,0)+1
        
    for i in umpire_country:
        print(i," : ",umpire_country[i])

    return umpire_country


def plot_graph(umpiress,count):
    plt.bar(umpiress, count)
    plt.xlabel('Umpires Country')
    plt.ylabel('No of Umpires')
    plt.title('Foreign Umpire Analysis')
    plt.show()


umpires = get_data()

umpire_country = get_umpires_country(umpires)


umpiress = list(umpire_country.keys())
count = list(umpire_country.values())
plot_graph(umpiress,count)

