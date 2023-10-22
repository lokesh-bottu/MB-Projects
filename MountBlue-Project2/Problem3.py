import csv
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime



def get_data(file_name):
    file = open(file_name)
    pincode_reader = csv.DictReader(file)
    return pincode_reader




# Create a dictionary to store 'pincode.csv' data
#read the Pincode file and make a dictionary of district and pincodes of it
# pincode as the key and its value as district


def get_pincode(pincode_reader):
    pincode_data = {}
    for dist in pincode_reader:
        pincode_data[dist["Pin Code"]] = dist["District"]
    return pincode_data


 

def get_districtdic(pincode_data,data):
    District_registration = defaultdict(int)
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

        address = company["Registered_Office_Address"]
        district_code = address[-6:]

        if year == "2015" and district_code in pincode_data:

            #if year = 2015 then find the district of that pincode using the above created dictionary.
            district = pincode_data[district_code]
            
            District_registration[district] += 1
    return District_registration



pincode_data = get_data("pincode.csv")
pincode_data = get_pincode(pincode_data)

Maha_data = get_data("Maharashtra.csv")
District_registration = get_districtdic(pincode_data,Maha_data)

for lokesh, count in District_registration.items():
    print(lokesh, " : ", count)




  
#Method 2

# import csv
# from collections import defaultdict
# import matplotlib.pyplot as plt
# from datetime import datetime
# with open('Maharashtra.csv',newline='',encoding='ISO-8859-1') as csvfile:
#     data= csv.DictReader(csvfile)
#     District_registration={}
#     for company in data:
#         year = str(company["DATE_OF_REGISTRATION"])
#         if len(year) == 8:
#             year = year[6:]
#             if int(year)>=0 and int(year)<=20:
#                 year = "20"+year
#             else:
#                 year = "19"+year
#         else:
#             year = year[:4]
#         address= company["Registered_Office_Address"]
#         district_code = address[(len(address)-6):]
#         if(year == "2015"):
#             with open('pincode.csv',newline='',encoding='ISO-8859-1') as csvfile1:
#                 pincode_data = csv.DictReader(csvfile1)
#                 try:
#                     if(int(district_code)):
#                         for dist in pincode_data:
#                             if(dist["Pin Code"] == str(district_code)):
#                                 District_registration[dist["District"]] = District_registration.get(dist["District"],0) +1
#                                 break
#                 except:
#                     pass
#         else:
#             pass    
#     for lokesh in District_registration:
#         print(lokesh," : ",District_registration[lokesh])