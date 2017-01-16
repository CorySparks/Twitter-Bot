import tweepy, time, sys, random

argfile = str(sys.argv[1])

Customer_Key = "Customer_Key"
Customer_Secret = "Customer_Secret"
Access_Token = "Access_Token"
Access_Secret = "Access_Secret" 

auth = tweepy.OAuthHandler(Customer_Key, Customer_Secret)
auth.set_access_token(Access_Token, Access_Secret)
api = tweepy.API(auth)
'''
filename = open(argfile,'r')
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    nap = random.randint(300, 3600)
    time.sleep(nap)
print(str(time.sleep(nap)))
'''
twt = api.search("Hello CorBot")

t = ['Hello',
    'Hey',
    'Hi',
    'Whats Up',
    'CorBot',
    'Cory',
    'Who',
    'Are',
    'You']

for s in twt:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "Hello @%s! As you can see i've been learning a lot!" % (sn)
            s = api.update_status(m, s.id)
