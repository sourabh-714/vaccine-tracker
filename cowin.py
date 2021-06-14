
import time

import requests
# from pygame import mixer
from datetime import datetime, timedelta
import json


print("search for open slots")

age = int(input("enter the age"))
# age=65
pin = input("enter the pin")
pincodes = []
pincodes.append(pin)

# pincodes = ["462003"]

print_flag = 'Y'


# no_of_days=int(input("enter the no of days you want to check for availavility"))
no_of_days = 2

today_date = datetime.today()
# print(today_date)
# run a loop to convert the no of days in list and iteraate,timedelta represents the differnce between the dates
list_format = [today_date + timedelta(days=i) for i in range(no_of_days)]
# print(list_format)

actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]

# rint(struc_dates)

# run a loop to fetch details of slot
# loop1-fetch details of evey pincode
#  fetch each date in the pin code


while True:
    counter = 0
    for pincode in pincodes:
        for tarikh in actual_dates:
             # URL="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode,tarikh)
               URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(
                   pincode, tarikh)
               header = {
                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

               results = requests.get(URL, headers=header)
               #print(results.text)

               if results.ok:
                   response_json = results.json()
                   flag = False
                   if response_json["centers"]:
                       if(print_flag.lower()) == 'y':
                           for kendra in response_json["centers"]:
                               # print(kendra)
                               for session in kendra["sessions"]:
                                   if(session["min_age_limit"] <= age and session["available_capacity"] > 0):
                                       print("pincodes>>>>>>>>>>>>>>", pincode)
                                       print("avaialbility on >>>>>>>>>", tarikh)
                                       print("\t", kendra["name"])
                                       print("\t Price", kendra["fee_type"])
                                       print("availabililty",
                                             session["available_capacity"])

                                       if(session["vaccine"] != ''):
                                           print("\t Vaccine type:",
                                                 session["vaccine"])
                                       print("\n")
                                       counter+=1
                                   else:
                                       pass
                                        
                                   
                                   

                                    
                                       
                                 
                                    
                                    

                       else:
                            pass
               else:
                    print("no response>>>>>>>>>>>>>")

    if counter==0:
        print("no vaccination slot is available")
    else:
        print(">>>>>>>>>>>>>search complete")

    # fetch data in real time
    dt=datetime.now()+timedelta(2)
    while(datetime.now())<dt:
        time.sleep(1)
     





                        



                            
                             
                       
            

            



