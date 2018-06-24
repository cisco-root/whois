import whois

site = input("site: ")

s = whois.whois(site)
print(s)
input("\n\n Press enter to exit")