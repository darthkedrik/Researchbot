import praw
import basc_py4chan
import sys
import csv
import time

reload(sys)
sys.setdefaultencoding('utf-8')

### Reddit APIs require a unique user_agent. Update version info as needed.
user_agent = "Anonymity Data Collector 0.0"

r = praw.Reddit(user_agent = user_agent)
r.login('Anon_collects', 'Anonbot!')


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

def chan_spybot(board, datalist):
    thread_count = 0
    print "Running chan_spybot on", board
    all_threads = board.get_all_threads(expand=True)
    while thread_count <100:
        for thread in all_threads:
            thread_count +=1
            post_not_present = True
            for post in thread.posts:
                if post.post_id in chan_post_ids:
                    post_not_present = False
                elif post_not_present == True:
                    postline = [post.post_id, '3-25-16', '4chan', board, 'Comment', post.text_comment]
                    datalist.append(postline)
                    chan_post_ids.append(post.post_id)
    return datalist
    
chan_datalist = list()
reddit_datalist = list()
reddit_post_ids = list()
chan_post_ids = list()


with open('corpus.csv', 'r+') as c:
    datareader = csv.reader(c)    
    for line in datareader:
        if line[2] == 'reddit':
            reddit_datalist.append(line)
            reddit_post_ids.append(line[0])
        elif line[2] == '4chan':
            chan_datalist.append(line)
            chan_post_ids.append(line[0])

chan_boards = ['b','c','ck','fit','g','his','mu','p','sci','v', 'x', 'vg', 'vr', 'sp', 'diy', 'adv']
reddit_subs = ['spacedicks','askreddit','aww','books','fitness','food','funny','gaming','history','music','photography','science','technology', '4chan', 'wtf', 'todayilearned', 'news', 'jokes', 'explainlikeimfive']

for sub in reddit_subs:
    reddit_datalist = reddit_spybot(sub, reddit_datalist)
       
for board in chan_boards:
    bname = basc_py4chan.Board(board)
    chan_datalist = chan_spybot(bname, chan_datalist)
    


full_list = reddit_datalist + chan_datalist

with open('corpus.csv', 'a+') as c:
    datawriter = csv.writer(c)
    for entry in full_list:
        datawriter.writerow(entry)


