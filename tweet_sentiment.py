import sys, os, io, json

os.chdir("C:/Users/Laptop/Documents/Repos/TwitterSentimentAnalysis")
output = open("C:/Users/Laptop/Documents/Repos/TwitterSentimentAnalysis/3minutetweets.txt")

afin = open("AFINN-111.txt")

scores = {}
struct = {}

for line in afin:
    term, score = line.split("\t")
    scores[term] = int(score)


data = json.loads(dataform)
data = json.load(output)
with open("output.json") as jsonfile:
	data = json.loads(jsonfile.read())

dataform = str(output).strip("'<>() ").replace('\'', '\"')
struct = json.loads(dataform)

print(data[0:100])
# i=0
# for line in output:
#     i+=1
#     val = 0
#     nline = json.loads(line)
#     try:
#         tweet = nline['text']
#         #print(tweet)
#         for key, value in scores.items():
#             if key in tweet.split(" "):
#                 #print(key, value)
#                 val += value
#         print(val)
#     except:
#         pass

