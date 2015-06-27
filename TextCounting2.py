import nltk
import json
import unicodedata

jsonfile = "NBA_JSON.20150616-083859.json"
jsonfile = open(jsonfile)
jsondata = jsonfile.read()

warriors = "#warriors"
nbafinals = "#nbafinals"

alltext = ""
ftext = ""
wtext = ""
bothtext = ""
for line in jsondata.split("\n"):
    #print type(line)
    #raw_input(line)
    if line != "":

        tweettext = json.loads(line)["text"]
        tweettext = tweettext.lower()

        alltext = alltext + "\n" + unicodedata.normalize('NFKD', tweettext).encode('ascii','ignore')

        if warriors in tweettext:
           wtext = wtext + "\n" + unicodedata.normalize('NFKD', tweettext).encode('ascii','ignore')

        if nbafinals in tweettext:
            ftext = ftext + "\n" + unicodedata.normalize('NFKD', tweettext).encode('ascii','ignore')


            if warriors in tweettext and nbafinals in tweettext:
               bothtext = bothtext + "\n" + unicodedata.normalize('NFKD', tweettext).encode('ascii','ignore')
            
jsonfile.close()

#################################
# BEGIN Results summarize
#################################


#a=nltk.text.Text(alltext)
#b=nltk.text.Text(alltext.split())


from nltk.book import FreqDist

fdALL = FreqDist(nltk.word_tokenize(alltext))
fdF = FreqDist(nltk.word_tokenize(ftext))
fdW = FreqDist(nltk.word_tokenize(wtext))
fdBOTH = FreqDist(nltk.word_tokenize(bothtext))


from nltk.corpus import stopwords
mystopwords = ["A", "#", "@", "!", ",", ":", ";", "http", "https", "'", "-", "."]


for rawtext in [alltext, ftext, wtext, bothtext]:
    print len(rawtext),rawtext[:50]


#################################
# END Results summarize
#################################




#################################
# BEGIN SAVING RESULTS
#################################

"""
#################################
# BOTH TAGS, saving
#################################

tokens = nltk.word_tokenize(alltext)


print "\nTOP 50 all = PreFILTER"
print fdALL.most_common(50)

filteredtext = ""


for word in tokens:
    if word not in stopwords.words("english") and word not in mystopwords:
        filteredtext += " " + word

fdALL = FreqDist(nltk.text.Text(filteredtext.split()))

print "\nTOP 50 = ALL"
print fdALL.most_common(50)


mydict= {}
[mydict.update({k:v}) for k,v in fdALL.most_common(50)]

writer = csv.writer(open('tweet_dict.csv', 'wb'))
for key, value in mydict.items():
    writer.writerow([key, value])

outfile = open( 'Tdict.csv', 'w' )
for key, value in mydict.items():
    outfile.write( str(key) + ',' + str(value) + '\n' )
outfile.close()

#################################
# WARRIORS TAGS, saving
#################################

tokens = nltk.word_tokenize(wtext)


print "\nWARRIORS/tTOP 50 all = PreFILTER"
print fdALL.most_common(50)

filteredtext = ""


for word in tokens:
    if word not in stopwords.words("english") and word not in mystopwords:
        filteredtext += " " + word

fdALL = FreqDist(nltk.text.Text(filteredtext.split()))

print "\nWARRIORS\tTOP 50 = ALL"
print fdALL.most_common(50)


mydict= {}
[mydict.update({k:v}) for k,v in fdALL.most_common(50)]


outfile = open( 'Wdict.csv', 'w' )
for key, value in mydict.items():
    outfile.write( str(key) + ',' + str(value) + '\n' )
outfile.close()


#################################
# NBAFINALS2015 TAGS, saving
#################################

tokens = nltk.word_tokenize(ftext)


print "\nWARRIORS/tTOP 50 all = PreFILTER"
print fdALL.most_common(50)

filteredtext = ""


for word in tokens:
    if word not in stopwords.words("english") and word not in mystopwords:
        filteredtext += " " + word

fdALL = FreqDist(nltk.text.Text(filteredtext.split()))

print "\nWARRIORS\tTOP 50 = ALL"
print fdALL.most_common(50)


mydict= {}
[mydict.update({k:v}) for k,v in fdALL.most_common(50)]


outfile = open( 'Fdict.csv', 'w' )
for key, value in mydict.items():
    outfile.write( str(key) + ',' + str(value) + '\n' )
outfile.close()

"""
#################################
# END SAVING RESULTS
#################################




"""
http://stackoverflow.com/questions/15085864/how-to-upload-a-file-to-directory-in-s3-bucket-using-boto

import boto

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

bucket_name = AWS_ACCESS_KEY_ID.lower() + '-dump'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)


import boto.s3
bucket = conn.create_bucket(bucket_name,
    location=boto.s3.connection.Location.DEFAULT)

testfile = "replace this with an actual filename"
print 'Uploading %s to Amazon S3 bucket %s' % \
   (testfile, bucket_name)

import sys
def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

from boto.s3.key import Key
k = Key(bucket)
k.key = 'my test file'
k.set_contents_from_filename(testfile,
    cb=percent_cb, num_cb=10)


"""
