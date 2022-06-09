import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("KXTZAbzozA6KhpXNmrOtoOP2H","MCkwqxNRExHhEzDf1b4LcwEee8cc7GD6HuYKThzOqb0WIrXOzR")
auth.set_access_token("1462689552959787009-LmR4YyKe5yuIEYcKa85t9OrJ6cd5o8","BB3l1fGKo3gkPVigQ6Zi3DjJnTrNGeE17h8WyuFnPtB54")

# Create API object
api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
    user = api.get_user(screen_name="ReseauxTelecom")
    #print (user)
    print("User details:")
    print(user.name)
    print(user.description)
    print(user.location) 
    print(user.followers_count)
except:
    print("Error during authentication")


