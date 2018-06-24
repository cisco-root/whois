import whois
import os
os.system('cls')
site = input("site: ")

s = whois.whois(site)

print(s)
import urllib.request
import time
time.sleep(6)
print('''
 _____ _____  _____  _____ ____  
 / ____|_   _|/ ____|/ ____/ __ \ 
| |      | | | (___ | |   | |  | |
| |      | |  \___ \| |   | |  | |
| |____ _| |_ ____) | |___| |__| |
 \_____|_____|_____/ \_____\____/ 
''')
print ("by cisco")
input("\n\n Press enter to exit")
