import whois

site = input("site: ")
s = whois.whois(site)

print(s)