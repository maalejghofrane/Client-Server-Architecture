from twitter import Twitter, OAuth

#Access Token,Access Token Secret,API Key,API Key Secret
t = Twitter(auth=OAuth("1462689552959787009-LmR4YyKe5yuIEYcKa85t9OrJ6cd5o8","BB3l1fGKo3gkPVigQ6Zi3DjJnTrNGeE17h8WyuFnPtB54"
,"KXTZAbzozA6KhpXNmrOtoOP2H","MCkwqxNRExHhEzDf1b4LcwEee8cc7GD6HuYKThzOqb0WIrXOzR"))



followers = t.followers.list(screen_name="ReseauxTelecom")

x = []
for follower in followers['users']:
    print("compte" + follower['screen_name'])
    x.append(follower['screen_name'])


for i in x:
    fs = t.followers.list(screen_name=i)
    for f in fs['users']:
        print(i + " " + f['screen_name'])
