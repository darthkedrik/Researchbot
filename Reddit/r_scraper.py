import praw
import csv
from .. import base_definitions

def spybot(sub_list):

    def spybot_id_checker(subm_comm, sc_type):
        if subm_comm.id in cur_ids:
            pass
        elif subm_comm.id not in cur_ids:
            ids_writer(subm_comm.id, id_file)
            post_data = [sub, subm_comm, sc_type]
            corpus_writer('reddit', post_data)
        else:
            print("Error in reading previously collected post ids. Please adjust data directory and verify integrity of corpora.")
            break

    PRI = LOGIN()
    for sub in sub_list:
        print("Running spybot on: /r/" + sub)
        id_file = DATA_DIR + sub _ "_ids.csv"
        cur_ids = ids_reader(id_file)
        submissions = PRI.subreddit(sub).hot(limit=1000)
        for submission in submissions:
            submission.comments.replace_more(limit=0)
            comments = submission.comments.list()
            spybot_id_checker(submission, 'submission')
            for comment in comments:
                spybot_id_checker(comment, 'comment')


'''
should write methods for determining interactions such as if the comment is top-level
or if the comment is a reply, and the id of the reply, hopefully allowing for
better analysis based on if the thread turns more negative, more positive, or remains
the same as the conversation continues. For sanity's sake, this will be a
wishlist of features for now.

Would also be nice to have the scores of each comment, as that plays a role in
the determination of positive/negative views by the community, as well as gilding.

'''


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
