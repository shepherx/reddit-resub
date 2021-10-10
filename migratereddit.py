import praw

oldaccount = praw.Reddit("AccountMigrator")
newaccount = praw.Reddit("AccountMigrator")

print ("Old Account:")
oldaccount.login()

print ("New Account:")
newaccount.login()

# Remove default subreddits
for sub in newaccount.get_my_subreddits(limit=None):
	sub.unsubscribe()

# Copy Subreddits
for sub in oldaccount.get_my_subreddits(limit=None):
	newaccount.get_subreddit(sub.display_name).subscribe()

# Copy Saved
for article in oldaccount.user.get_saved(sort="new", time="all", limit=None):
	article.reddit_session = newaccount
	article.save()
