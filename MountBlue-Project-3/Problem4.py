import csv
from collections import defaultdict
import matplotlib.pyplot as plt



 
def get_data(path):
    file = open(path)
    return csv.DictReader(file)
    
def get_country_population(data):
    country=["Brunei", "Cambodia", "Indonesia", "Laos", "Malaysia", "Myanmar", "Philippines", "Singapore", "Thailand", "Vietnam"]
    country_population ={}
    #In this case we have two condition the year should be present in last 10 years and it should be the Asean Country 
    for row in data:
        if(row["Region"] in country and (2014 >= int(row["Year"]) >= 2004)):

            if (row["Year"] not in country_population.keys()):
                #check if the year is not present then add the year as a key with empty dic
                country_population[row["Year"]] = {}
                #get method gives 0 if the key is not present, if present it just gives the present value of it.
            country_population[row["Year"]][row["Region"]] = country_population[row["Year"]].get(row["Region"],0) + int(float(row["Population"]))

    for i in country_population:
        print(i,country_population[i])
    
    return country_population


def plot_graph(years,countries):
    data = {country: [country_population[year][country] for year in years] for country in countries}

    # Grouped bar chart
    bar_width = 0.15
    index = range(len(years))
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Colors for different countries

    for i, country in enumerate(countries):
        plt.bar([x + i * bar_width for x in index], data[country], width=bar_width, label=country, color=colors[i])

    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population by Year and Country')
    plt.xticks([i + 3 * bar_width for i in index], years)
    plt.legend(countries, loc='upper left', title='Countries')

    plt.tight_layout()
    plt.show()


data = get_data("population-estimates_csv.csv")
country_population = get_country_population(data)

years = list(country_population.keys())
countries = list(country_population[years[0]].keys())

plot_graph(years,countries)