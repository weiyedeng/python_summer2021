
#%% SETUP
import importlib
import os
import tweepy
import time
# change directory
os.chdir('E:/mine/academics_career/API_keys')

twitter = importlib.import_module('start_twitter')
api = twitter.client

polisci = api.get_user('@WUSTLPoliSci') ## get wustlpolisci account
followers = api.followers(polisci.id, count = 200)
friends = api.friends(polisci.id, count = 200) ## but only 161 friends

layman_followers = [] # layman followers list
expert_followers = [] # expert followers list
celebrity_followers = [] # celebrity followers list

layman_friends = [] # layman friends list
expert_friends = [] # expert friends list
celebrity_friends = [] # celebrity friends list

for follower in followers:
    if follower.followers_count < 100:
        layman_followers.append(follower)
    elif follower.followers_count >= 100 and follower.followers_count < 1000:
        expert_followers.append(follower)
    else:
        celebrity_followers.append(follower)

for friend in friends:
    if friend.followers_count < 100:
        layman_friends.append(friend)
    elif friend.followers_count >= 100 and friend.followers_count < 1000:
        expert_friends.append(friend)
    else:
        celebrity_friends.append(friend)





#%% ONE DEGREE OF SEPARATION
followers_tweet_count = {} # each follower: tweet count
followers_followers_count = {} # each follower: followers count

layman_followers_tweet_count = {} # each layman follower's name: each layman follower's tweet count
layman_friends_tweet_count = {} # each layman friend's name: each layman friend's tweet count
expert_followers_tweet_count = {} # each expert follower's name: each expert follower's tweet count
expert_friends_tweet_count = {} # each expert friend's name: each expert friend's tweet count
celebrity_followers_tweet_count = {} # each celebrity follower's name: each celebrity follower's tweet count 
celebrity_friends_tweet_count = {} # each celebrity friend's name: each celebrity's tweet count

friends_followers_count = {} # each friend: followers count


for follower in followers:
    followers_tweet_count[follower.name] = follower.statuses_count # match each follower with their tweet count
    followers_followers_count[follower.name] = follower.followers_count # match each follower with their followers count

for layman in layman_followers:
    layman_followers_tweet_count[layman.name] = layman.statuses_count

for expert in expert_followers:
    expert_followers_tweet_count[expert.name] = expert.statuses_count

for celebrity in celebrity_followers:
    celebrity_followers_tweet_count[celebrity.name] = celebrity.statuses_count # match each follower with their tweet count (celebrity)

for layman in layman_friends:
    layman_friends_tweet_count[layman.name] = layman.statuses_count # match each friend with their tweet count (layman)

for expert in expert_friends:
    expert_friends_tweet_count[expert.name] = expert.statuses_count # match each friend with their tweet count (expert)

for celebrity in celebrity_friends:
    celebrity_friends_tweet_count[celebrity.name] = celebrity.statuses_count # match each friend with their friends count (celebrity)

for friend in friends:
    friends_followers_count[friend.name] = friend.followers_count # match each friend with their followers count
     
### most active follower
print('The most active follower is %s, with %d tweets' % (max(followers_tweet_count, key=followers_tweet_count.get), max(followers_tweet_count.values()))) 

### most popular follower
print('The most popular follower %s, with %d followers' % (max(followers_followers_count, key=followers_followers_count.get), max(followers_followers_count.values()))) 

### most active layman friend
print('The most active layman friend is %s, with %d tweets' % (max(layman_friends_tweet_count, key=layman_friends_tweet_count.get), max(layman_friends_tweet_count.values()))) 

### most active layman friend
print('The most active expert friend is %s, with %d tweets' % (max(expert_friends_tweet_count, key=expert_friends_tweet_count.get), max(expert_friends_tweet_count.values()))) 

### follower with most followers (celebrity)
print('The most active celebrity friend is %s, with %d tweets' % (max(celebrity_friends_tweet_count, key=celebrity_friends_tweet_count.get), max(celebrity_friends_tweet_count.values()))) 

### friend with most followers 
print('The most popular friend is %s, with %d friends' % (max(friends_followers_count, key=friends_followers_count.get), max(friends_followers_count.values()))) 





#%% TWO DEGREE OF SEPARATION
layman_expert_followers = layman_followers + expert_followers # get only layman and expert followers
layman_expert_followers_tweet_count = {**layman_followers_tweet_count, **expert_followers_tweet_count} ## merge the layman-follower dict and the expert-follower dict that matches name with tweet count
layman_expert_followers_most_active_followers = {} # store the most active follower for each layman follower of polisci

i=0 # counter
j=0 # counter
for account in layman_expert_followers:
    try:         
        account_identified = api.get_user("@" + account.screen_name) # get_user for each layman follower of polisci           
        try:
            layman_expert_followers_followers = api.followers(account_identified.id, count = 200) # get followers for each layman follower of polisci
        except:
            layman_expert_followers_followers = [] # fail to the get the followers because of authorization problem, give an empty list instead
     
        layman_expert_followers_followers_tweet_count = {} # layman follower's followers' name: layman follower's followers' tweet count
        try:
            for follower in layman_expert_followers_followers:
                layman_expert_followers_followers_tweet_count[follower.name] = follower.statuses_count # layman's follower's name: layman's follower's tweet count
            
            layman_expert_followers_most_active_followers_name = max(layman_expert_followers_followers_tweet_count, key = layman_expert_followers_followers_tweet_count.get) # get the name of the layman follower's most active follower
            layman_expert_followers_most_active_followers_count = max(layman_expert_followers_followers_tweet_count.values()) # get the tweet count of the layman's follower's most active follower           
            layman_expert_followers_most_active_followers[layman_expert_followers_most_active_followers_name] = layman_expert_followers_most_active_followers_count # layman's most active follower's name: layman's most active follower's tweet count
        
            i += 1 # counter for successful recording of layman_most_active_followers
            print("success (follower): i = %d" % (i))
        except:
            j += 1 # counter of failed recording of layman_most_active_followers
            print("get the user but cannot get the followers: j = %d" % (j))
    except:
        time.sleep(15*60)

### Check the dict
layman_expert_followers_most_active_followers

### Among the followers of @WUSTLPoliSci and their friends, who is the most active?
if max(layman_expert_followers_tweet_count.values()) <= max(layman_expert_followers_most_active_followers.values()):
    print('Among the followers of @WUSTLPoliSci and their followers, the most active account is %s with %d tweets' % (max(layman_expert_followers_most_active_followers, key=layman_expert_followers_most_active_followers.get), max(layman_expert_followers_most_active_followers.values()))) 
else:
    print('Among the followers of @WUSTLPoliSci and their followers, the most active account is %s, with %d tweets' % (max(layman_expert_followers_tweet_count, key=layman_expert_followers_tweet_count.get), max(layman_expert_followers_tweet_count.values()))) 



################################################################################
layman_expert_friends = layman_friends + expert_friends# get only layman and expert friends
layman_expert_friends_tweet_count = {**layman_friends_tweet_count, **expert_friends_tweet_count} ## merge the layman-friend dict and the expert-friend dict
layman_expert_friends_most_active_friends = {} # store the most active friend for each layman follower of polisci

m=0 # counter
n=0 # counter
for account in layman_expert_friends[0:5]:
    try:         
        account_identified = api.get_user("@" + account.screen_name) # get_user for each layman follower of polisci       
    
        try:
            layman_expert_friends_friends = api.friends(account_identified.id, count = 200) # get followers for each layman follower of polisci
        except:
            layman_expert_friends_friends = []
   
        layman_expert_friends_friends_tweet_count = {} # layman follower's friends' name: layman follower's friends' tweet count
        try:
            for friend in layman_expert_friends_friends:
                layman_expert_friends_friends_tweet_count[friend.name] = friend.statuses_count # layman's follower's name: layman's follower's tweet count
            
            layman_expert_friends_most_active_friends_name = max(layman_expert_friends_friends_tweet_count, key = layman_expert_friends_friends_tweet_count.get) # get the name of the layman follower's most active follower
            layman_expert_friends_most_active_friends_count = max(layman_expert_friends_friends_tweet_count.values()) # get the tweet count of the layman's follower's most active follower           
            layman_expert_friends_most_active_friends[layman_expert_friends_most_active_friends_name] = layman_expert_friends_most_active_friends_count # layman's most active follower's name: layman's most active follower's tweet count
        
            m += 1 # counter for successful recording of layman_most_active_followers
            print("success (follower): m = %d" % (m))
        except:
            n += 1 # counter of failed recording of layman_most_active_followers
            print("get the user but cannot get the followers: n = %d" % (n))
    except:
        time.sleep(15*60)

### Check the dict
layman_expert_friends_most_active_friends

### Among the followers of @WUSTLPoliSci and their followers, who is the most active?
if max(layman_expert_friends_tweet_count.values()) <= max(layman_expert_friends_most_active_friends.values()):
    print('Among the friends of @WUSTLPoliSci and their friends, the most active account is %s with %d tweets' % (max(layman_expert_friends_most_active_friends, key=layman_expert_friends_most_active_friends.get), max(layman_expert_friends_most_active_friends.values()))) 
else:
    print('Among the friends of @WUSTLPoliSci and their friends, the most active account is %s, with %d tweets' % (max(layman_expert_friends_tweet_count, key=layman_expert_friends_tweet_count.get), max(layman_expert_friends_tweet_count.values()))) 
