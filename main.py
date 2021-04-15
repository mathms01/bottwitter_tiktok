import twitter
import random
import time
from keys import keys

# Connection à l'api
api = twitter.Api(consumer_key=keys["api_key"],
                  consumer_secret=keys["api_secret"],
                  access_token_key=keys["token_key"],
                  access_token_secret=keys["token_secret"])

#définiton des variables aléatoires
randO = random.randint(2,15)
randImg = random.randint(1,5)

#création du text du tweet
string = "MY BESTO FRIEND"
for i in range(1,randO):
    string = string+"O"

#récupération de l'id du dernier tweet traité
lastTweet = 0
f = open("lastTweet.txt", 'r')
line = f.readline()
if line.strip():
    lastTweet = int(line)
f.close()


#envoie des réponses au tweets mentionnés
while(True):
    print("Scanning...")

    #récupération des tweets ou le bot est mentionné
    if lastTweet != 0:
        statusMentionned = api.GetMentions(count=5, since_id=lastTweet+1)
    else:
        statusMentionned = api.GetMentions(count=5)

    for i in statusMentionned:
        print(i.text)
        id = i.id
        user = i.user.screen_name
        # string = "@"+ user + " " + string
        status = api.PostUpdate(status = string, media = "img/besto"+str(randImg)+".jpg", in_reply_to_status_id=id, auto_populate_reply_metadata=True )
        print(status)
        print(id)
        print(lastTweet)
        if id > lastTweet:
            lastTweet = id
            f = open("lastTweet.txt","w")
            f.write(str(lastTweet))
            f.close()
    time.sleep(60)