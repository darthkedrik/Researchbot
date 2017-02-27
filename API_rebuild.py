import urllib
import praw
import basc_py4chan
import codecs
import time

### Reddit APIs require a unique user_agent. Update version info as needed.
user_agent = "Anonymity Data Collector 1.00"

r = praw.Reddit(user_agent = user_agent)

### Need to compile these into a .txt, one for reddit posts, one for reddit
### titles, and one each for 4chan.
### 4chan doesn't require titles. Write escape to make sure Subject = None
### is instead replaced with the first five words of the selfpost text to
### avoid duplication and avoid skipping duplicate post titles.

### Readers of various texts. I tried to contain as much of the API
### differences within these two differences. reddit_reader uses reddit
### API, chan_reader uses 4chan API.
### The rest of the code should be about as free of API-specific text
### as can be made possible, minus title checking.


'''

    This code is old, in need of restructuring. Since the library csv
    exists, this should likely be an output to a csv file for ease of
    scanning and reading. The newer version of the code is present in
    Data_scraper.py. Consolidate these into less files and make sure
    it is all working.


def reddit_reader(submission, text):
    ### flattens out the comment tree using praw.helpers
    flat_tree = praw.helpers.flatten_tree(submission.comments)
    ### writes the submission title surrounded by ***, and the selftext
    ### of the post surrounded with ...
    text.write('***')
    text.write(submission.title)
    text.write('***')
    text.write('   ===   ')
    text.write(submission.selftext)
    text.write('   ===   ')
    ### Writes each comment to the file. try is necessary because of
    ### "more comments" loaders.
    for comment in flat_tree:
        try:
            text.write('   ---   ')
            text.write(comment.body)
            text.write('   ---   ')
        except AttributeError:
            continue
    return

def chan_reader(thread, text, title):
    ### 4chan API doesn't require flattening of a comment tree.
    ### thread.topic is the subject post, while thread.replies is a
    ### list of all replies to the topic.
    ### thread contains topic, subject, and replies.
    text.write('***\n')
    text.write(title)
    text.write('***\n')
    text.write('   ===   ')
    text.write(thread.topic.text_comment)
    text.write('   ===   ')
    for reply in thread.replies:
        text.write('   ---   ')
        text.write(reply.text_comment)
        text.write('   ---   ')
    return

'''

def reddit_spybot(sub, tf, cf):
    submissions = r.get_subreddit(sub).get_hot(limit=100)
    for post in submissions:
        titles = codecs.open(tf, 'r', encoding = 'utf-8').read()
        if post.title in titles:
            continue
        elif post.title not in titles:
            with codecs.open(tf, 'a', encoding='utf-8') as tff:
                tff.write(post.title)
                tff.write(' \n')
            with codecs.open(cf, 'a', encoding='utf8') as cff:
                reddit_reader(post, cff)
    return

def chan_checker(thread, title_file):
    if thread != None:
        if thread.topic.subject != None:
            with codecs.open(title_file, 'a+', encoding='utf-8') as tf:
                if thread.topic.subject in tf:
                    return False
                else:
                    return thread.topic.subject
        else:
            title_str = thread.topic.comment[0:10]
            with codecs.open(title_file, 'a+', encoding='utf-8') as tf:
                if title_str in tf:
                    return False
                else:
                    return title_str

def chan_spybot(board, tf, cf):
    threads = board.get_all_thread_ids()
    for thread in threads:
        post = board.get_thread(thread)
        title = chan_checker(post, tf)
        if title != False and title != None:
            with codecs.open(tf, 'a+', encoding='utf-8') as tff:
               tff.write(title)
               tff.write(' \n')
            with codecs.open(cf, 'a+', encoding='utf-8') as cff:
                chan_reader(post, cff, title)
        elif title == False:
            continue
    return

r_comments = ['reddit_comments_askreddit.txt','reddit_comments_aww.txt','reddit_comments_books.txt','reddit_comments_fitness.txt','reddit_comments_food.txt',
'reddit_comments_funny.txt','reddit_comments_gaming.txt','reddit_comments_history.txt','reddit_comments_music.txt','reddit_comments_photography.txt',
'reddit_comments_science.txt','reddit_comments_tech.txt','reddit_comments_4chan.txt', 'reddit_comments_wtf.txt', 'reddit_comments_spacedicks.txt',
'reddit_comments_til.txt', 'reddit_comments_news.txt', 'reddit_comments_jokes.txt', 'reddit_comments_eli5.txt']
r_titles = ['reddit_titles_askreddit.txt','reddit_titles_aww.txt','reddit_titles_books.txt','reddit_titles_fitness.txt','reddit_titles_food.txt','reddit_titles_funny.txt',
'reddit_titles_gaming.txt','reddit_titles_history.txt','reddit_titles_music.txt','reddit_titles_photography.txt','reddit_titles_science.txt','reddit_titles_tech.txt',
'reddit_titles_4chan.txt', 'reddit_titles_wtf.txt', 'reddit_titles_spacedicks.txt', 'reddit_titles_til.txt', 'reddit_titles_news.txt', 'reddit_titles_jokes.txt', 'reddit_titles_eli5.txt']
r_subs = ['askreddit','aww','books','fitness','food','funny','gaming','history','music','photography','science','technology', '4chan', 'wtf', 'spacedicks', 'todayilearned', 'news', 'jokes', 'explainlikeimfive']

c_comments = ['4chan_comments_b.txt','4chan_comments_c.txt','4chan_comments_ck.txt','4chan_comments_fit.txt','4chan_comments_g.txt','4chan_comments_his.txt',
'4chan_comments_lit.txt','4chan_comments_mu.txt','4chan_comments_p.txt','4chan_comments_sci.txt','4chan_comments_v.txt']
c_titles = ['4chan_titles_b.txt','4chan_titles_c.txt','4chan_titles_ck.txt','4chan_titles_fit.txt','4chan_titles_g.txt','4chan_titles_his.txt','4chan_titles_lit.txt',
'4chan_titles_mu.txt','4chan_titles_p.txt','4chan_titles_sci.txt','4chan_titles_v.txt']
c_boards = ['b','c','ck','fit','g','his','mu','p','sci','v']

for sub in r_subs:
    while True:
        try:
            comm_file = r_comments[r_subs.index(sub)]
            title_file = r_titles[r_subs.index(sub)]
            reddit_spybot(sub, title_file, comm_file)
        except SocketError as e:
            if e.errno != errno.ECONNRESET:
                raise
            time.sleep(5)
            continue
        break


for board in c_boards:
    bname = basc_py4chan.Board(board)
    title_file = c_titles[c_boards.index(board)]
    comm_file = c_comments[c_boards.index(board)]
    chan_spybot(bname, title_file, comm_file)
