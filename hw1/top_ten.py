import sys
import json
from collections import Counter
	
def read_tweet(tweet_file):
	tweet_read = tweet_file.readlines()


	result_list = []
	hash_list = []
	for i in tweet_read:
		load = json.loads(i)
		if load.get('entities') == None:
			pass
		else:
			if load.get('entities').get('hashtags') != []:
				hash_list.append(load.get('entities').get('hashtags'))
				#print hash_list
			else:
				pass
		#print words
	return hash_list
		
def read_hashtags(hashtag_list):
	hashtag_text_list = []
	for i in hashtag_list:
		#print i
		for q in i:
			#print q
			hashtag_text_list.append(q.get('text'))
	#print hashtag_text_list
	return hashtag_text_list

def list_counter(list):
	top_entry = []
	counter = Counter(list)
	#print counter
	for w in sorted(counter, key=counter.get, reverse=True):
  		top_entry.append((w, float(counter[w])))
  	return top_entry[:10]

    		

def main():
    tweet_file = open(sys.argv[1])
    tweeted_hash = read_tweet(tweet_file)
    hashtag_list = read_hashtags(tweeted_hash)
    for i in (list_counter(hashtag_list)):
	    print "%s %0.2f" % (i[0], i[1])


if __name__ == '__main__':
    main()