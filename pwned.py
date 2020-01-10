#developed by Santosh Baral
#using haveibeenpwned.com
developer="""
************************ Developed By Santosh Baral ****************************     
                    This Is Made For Educational Purpose
             Visit https://santoshbrl.com.np For Developer Details
            Visit https://techohnepal.com For Any Development Projects

                    *****  ****  **** *   *        **    *   *
                      *    ****  *    *****      *    *  *****
                      *    ****  **** *   *        **    *   *

*******************************************************************************

If You Face Any Problem Make Sure You Have Install All Libraries Required For This Tool.

----------------------------------------------------------------------------------------
"""

print(developer)

import requests
import cfscrape
import json
#to make program run 
choice=True
while choice==True:
	#ask for input what user want's
	print("1. Check For Data Breach")
	print( "2. Exit The Program")
	print("\n")
	user_choice=input()
	if user_choice == "1":
		choice=True
		print("\n") #gap for getter vision
		#ask for email to check
		email=input("Enter Your Email Address To Check Data Breach ")
		#server/url to check data breach
		url = "https://haveibeenpwned.com/unifiedsearch/"
		scraper = cfscrape.create_scraper()
		html_request= scraper.get(url + email)
		#checking if data is breached or not
		if str(html_request.status_code)=="404":
			print("\n") #gap for line creating
			print("Congrats Your Account Is Safe :)")
			print("\n")
		elif str(html_request.status_code)=="200":
			print("\n") #gap for line creating
			print("Found Data Breach For Your Entered Email Address")
			print("\n") #gap for line creating
			print("Checking For Available Data Please Wait.....")
			print("\n") #gap for line creating


			#fetching json data
			full_json=html_request.json()
			#print(full_json)
			#checking for all possible data leak
			for dates in range(0,9):
			#checking/verifying for all values
				try:
					if full_json['Breaches'][dates]['IsVerified']==False or True:
						#print("\n") #gap for line creating
						title=full_json['Breaches'][dates]['Title']
						#print(full_json['Breaches'][dates]['Title'])
						print("Your Data Breach Found On " + title)
						print("\n") #gap for line creating
						breach_date=full_json['Breaches'][dates]['BreachDate']
						print("Your Data Was Breach On     " + breach_date)
						print("\n") #gap for line creating
						breach_description=full_json['Breaches'][dates]['Description']
						print("Short Information About Your Data Breach: "+" " + " "+ breach_description)
						print("\n") #gap for line creating 
						info_leaked=(full_json['Breaches'][dates]['DataClasses'])
						print("Leaked Information are ")
						print(info_leaked)
						print("\n") #gap for line creating
				except Exception as e:
					break

			print("\n")
			print("Search Finished..")
			print("\n")
	elif user_choice=="2":
		choice=False
		print('\n')
		print("Thanks For Using This Tool. Visit https://sagarbaral.com.np for other downloads")
		print("Know About Developer https://santoshbrl.com.np")

