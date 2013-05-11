import urllib
import json

URL = "http://search.twitter.com/search.json?q=microsoft&page="


response_list = []
for page in range(1,11):
	response = urllib.urlopen(URL+str(page))
	#print page, '\n'
	twitter_response = json.load(response)['results']

	for i in twitter_response:
		response_list.append(i['text'])
	#print response_list

for i in response_list:
	print i, '\n'