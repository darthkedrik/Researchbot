import praw
import csv
from .. import base_definitions

def spybot(sub_list):
    PRI = LOGIN()
    for sub in sub_list:
        print "Running spybot on: /r/" + sub

'''
def reddit_spybot(sub, datalist):
    print "Running reddit_spybot on", '/r/' + sub
    while True:
        try:
            submissions = r.get_subreddit(sub).get_hot(limit=150)
            for post in submissions:
    	        all_comments = praw.helpers.flatten_tree(post.comments)
                post_not_present = True
                if post.id in reddit_post_ids:
                    post_not_present = False
                elif post_not_present == True:
                    #print 'Adding a post...'
                    postline = [post.id, '3-25-16', 'reddit', sub, 'Post', post.selftext]
                    datalist.append(postline)
                    reddit_post_ids.append(post.id)
                for c in all_comments:
                    if type(c) is not praw.objects.MoreComments:
                        comment_not_present = True
                        if c.id in reddit_post_ids:
                            comment_not_present = False
                        elif comment_not_present == True:
                            cline = [c.id, '3-25-16', 'reddit', sub, 'Comment', c.body]
                            datalist.append(cline)
                            reddit_post_ids.append(c.id)
        except OSError(ConnectionError):
                time.sleep(5)
                continue
        break

    return datalist
'''
reddit_subs = ['spacedicks','askreddit','aww','books','fitness','food','funny','gaming','history','music','photography','science','technology', '4chan', 'wtf', 'todayilearned', 'news', 'jokes', 'explainlikeimfive']
