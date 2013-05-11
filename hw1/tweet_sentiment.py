import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    return str(fp.readlines())


def read_sent(sent_file):
	sent_dict = dict()
	sent_read = sent_file.read()
	sent_json = sent_read.split('\n')
	for entry in sent_json:
		sent_dict.update({str(entry.split('\t')[0]):entry.split('\t')[-1]})
	return sent_dict

	
def read_tweet(tweet_file, sentiment_file):
	sentiment_dictionary = read_sent(sentiment_file)
	tweet_read = tweet_file.readlines()


	result_list = []
	for i in tweet_read:
		load = json.loads(i)
		if load.get('text') == None:
			words = []
		else:
			words = [word for word in load.get('text').split()]
		#print words

		# Print each word in a tweet if tweet 'text' is not None
		score = 0
		if len(words) != 0:
			for word in words:
				if word in sentiment_dictionary:
					#print word, sentiment_dictionary[word]
					score += float(sentiment_dictionary[word])
					#print score
				else:
					pass
		else:
			#result_list.update({"extra":0})
			pass
		result_list.append((load.get('text'), score))
	return result_list
				
    		

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    #read_sent(sent_file)
    #sentiment_dictionary = read_sent(sent_file)
    final_result = read_tweet(tweet_file, sent_file)
    #print sentiment_dictionary
    #print final_result
    for i in final_result:
    	print "%0.2f" % (i[1])

if __name__ == '__main__':
    main()