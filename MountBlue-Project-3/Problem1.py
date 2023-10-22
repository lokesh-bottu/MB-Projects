import csv
from collections import defaultdict
import matplotlib.pyplot as plt


    
def get_data(file):
    file_name = open(file)
    data = csv.DictReader(file_name)
    return data

def get_population(data):
    india_population = {}
    for row in data:

        #Get the Region if it is India then get the population of that year.
        if(row["Region"] == "India"):
            india_population[row["Year"]] = int(float(row["Population"]))

    for i in india_population:
        print(i," : ",india_population[i]," ",type(india_population[i]))
        
    return india_population



def plot_graph(years,registrations):
    plt.bar(years, registrations)
    plt.xlabel('Year')
    plt.ylabel('Population of the Year')
    plt.title('India Population')
    plt.xticks(rotation = 90)
    plt.show()



data = get_data("population-estimates_csv.csv")

india_population = get_population(data)
years = list(india_population.keys())
registrations = list(india_population.values())
plot_graph(years,registrations)