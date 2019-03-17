import whois
import os
import time
#-------clear your shell--------#
os.system('cls')
#+++++++Getting the desired site++++++
site = input("site: ")
#========Receive information and save it for processing=======
s = whois.whois(site)
#*******Show information*******
print(s)
#"""""exit"""""""
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
