#developed by Santosh Baral
"""
										Disclaimer

 Legal disclaimer: Usage of pwned.py for attacking targets without prior mutual consent is illegal. 
 It is the end user's responsibility to obey all applicable local,state and federal laws.
  Developers assume no liability and are not responsible for any misuse or damage caused.

"""
developer="""
************************ Developed By Santosh Baral ****************************     
                    This Tool Is Made For Educational Purpose
             Visit https://santoshbrl.com.np For Developer Details
            Visit https://techohnepal.com For Any Development Projects

            This Tool is Inspired By #Nittam | @TheNittam (https://nirmaldahal.com.np)

──────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████████─██████──██████────██████████████─██████──██████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██────██░░░░░░░░░░██─██░░██──██░░██─
─██████░░██████─██░░██████████─██░░██████████─██░░██──██░░██────██░░██████░░██─██░░██──██░░██─
─────██░░██─────██░░██─────────██░░██─────────██░░██──██░░██────██░░██──██░░██─██░░██──██░░██─
─────██░░██─────██░░██████████─██░░██─────────██░░██████░░██────██░░██──██░░██─██░░██████░░██─
─────██░░██─────██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██────██░░██──██░░██─██░░░░░░░░░░██─
─────██░░██─────██░░██████████─██░░██─────────██░░██████░░██────██░░██──██░░██─██░░██████░░██─
─────██░░██─────██░░██─────────██░░██─────────██░░██──██░░██────██░░██──██░░██─██░░██──██░░██─
─────██░░██─────██░░██████████─██░░██████████─██░░██──██░░██────██░░██████░░██─██░░██──██░░██─
─────██░░██─────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██────██░░░░░░░░░░██─██░░██──██░░██─
─────██████─────██████████████─██████████████─██████──██████────██████████████─██████──██████─
──────────────────────────────────────────────────────────────────────────────────────────────


*******************************************************************************

If You Face Any Problem Make Sure You Have Install All Libraries Required For This Tool.

----------------------------------------------------------------------------------------------
|                                                                                       
|*********************** Libraries Installation Command Line ********************************
|---------------------------------------------------------------------------------------------
|	
|		pip3 install -r requirements.txt 
|	       
| 
----------------------------------------------------------------------------------------------


==============================================================================================
||
||****************** NOTE: THIS TOOL IS MADE FOR EDUCATION PURPOSE ONLY *****************
||--------------------------------------------------------------------------------------------
||************************************ Disclaimer ******************************
||--------------------------------------------------------------------------------------------
||	[!] Legal disclaimer: Usage of pwned.py for attacking targets without prior mutual 
||	consent is illegal. It is the end user's responsibility to obey all applicable local,
||	state and federal laws. Developers assume no liability and are not responsible for 
||	any misuse or damage caused.
||
==============================================================================================
"""

print(developer)

from datetime import datetime
from json2html import *
from bs4 import BeautifulSoup as BS
from urllib.request import Request, urlopen

import urllib.request
import json

now = datetime.now()
current_time = str(now.strftime("%Y-%m-%d-%H-%M-%S"))

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36', 
    'Accept-Language': 'en-US,en;q=0.8'
    }


email=input("Enter Your Email Address To Check Data Breach :  ")
req = urllib.request.Request(
  'https://haveibeenpwned.com/unifiedsearch/' + email, 
    headers=hdr
    )


try:
	with urllib.request.urlopen(req) as resp:
		print("\n") #gap
		print("\n")
		print("Found Data Breach For Your Entered Email Address")
		print("\n")  
		print("Checking For Available Data Please Wait.....")
		print("\n") 
		print("\n")
		data = json.loads(resp.read().decode("utf-8"))
		#print(data) #print the result found
		#the_page = resp.code #remove # if you want to print the http status code
		#print(the_page) #remove # if you want to print the http status code
		outputtable=(json2html.convert(json=data))
		print("\n")
		print("\n")
		print("All Found Breached Details Are Save As (.html) File In .../.../pwned-checkerv2.0")
		print("\n")
		saveFile = open(current_time + email + '.html', 'w')
		saveFile.write(str(outputtable))
		saveFile.close()



except Exception as e:
	#print(str(e)) #I am too lazy for hard work if you want to check if the code works or not than uncommnet this line and see the error if anything occur (HTTP Error 404: Not Found means it is working)
	pass
	print("\n")
	print("Congrats Your Account Is Safe ")
	print("\n")
	print("But Make Sure To Change Password Once For Your Safty")
	print("\n")
	print("And Also Make Sure To Use Strong Password With Small And Capital Alphabet Char, symbols and numbers.")
	print("\n")
	
print("\n")	
print("Search Finished..")
print("\n")

password_choice=input("Want To Check If Password Is Available Online(y/n): ")
print("\n")
if password_choice == str("y") or password_choice == str("Y"):
	url = "https://pwndb2am4tzkvold.onion.ws/"
	username = email
	domain = "%"
	if "@" in email:
		username = email.split("@")[0]
		domain = email.split("@")[1]
		if not username:
			username = '%'

	data = urllib.parse.urlencode({'luser': username, 'domain': domain, 'luseropr': 0, 'domainopr': 0, 'submitform': 'em'})
	data = data.encode('ascii')
	req = Request('https://pwndb2am4tzkvold.onion.ws', headers={'User-Agent': 'Mozilla/5.0'},data=data)
	webpage = urlopen(req).read()
	#print(webpage)

	soup = BS(webpage, 'html.parser')
	#print(soup.find('pre').text.strip())
	print("Thank Your For Using This Tool")
	for item in soup.find_all('pre'):
		#print(item.text.strip())
		arrayopt=(soup.find('pre').text.strip())
		saveFile = open(current_time + email + ' password.txt', 'w')
		saveFile.write(str(arrayopt))
		saveFile.close()
		with open(current_time + email + ' password.txt',"r") as f:
			lines = f.readlines()
			for i in range(0,8):
				del lines[0]

			with open(current_time + email + ' password.txt',"w") as f:
				for line in lines:
					if line.strip("\n") != "8":
						f.write(line)
		print("\n")
		print("\n")
		print("\n")
		print("\n")
		print("All Found Passwords Are Stored As (.txt) File In /.../.../pwned-checkerv2.0")
		print("\n")
		print("\n")
		print("\n")

			
else:
	print("\n")
	print("\n")
	print("\n")
	print("Thank Your For Using This Tool")
	print("\n")

print("\n")
print("\n")
print("Thanks For Using This Tool. Visit https://sagarbaral.com.np for other downloads")
print("\n")
print("Know About Developer https://santoshbrl.com.np")
