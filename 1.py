import urllib
s = 'payload'
print(urllib.parse.quote_plus(s.encode("IBM037"))) 
