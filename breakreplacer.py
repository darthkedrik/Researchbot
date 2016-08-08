r_comments = ['reddit_comments_askreddit.txt','reddit_comments_aww.txt','reddit_comments_books.txt','reddit_comments_fitness.txt','reddit_comments_food.txt',
'reddit_comments_funny.txt','reddit_comments_gaming.txt','reddit_comments_history.txt','reddit_comments_music.txt','reddit_comments_photography.txt',
'reddit_comments_science.txt','reddit_comments_tech.txt']
r_titles = ['reddit_titles_askreddit.txt','reddit_titles_aww.txt','reddit_titles_books.txt','reddit_titles_fitness.txt','reddit_titles_food.txt','reddit_titles_funny.txt',
'reddit_titles_gaming.txt','reddit_titles_history.txt','reddit_titles_music.txt','reddit_titles_photography.txt','reddit_titles_science.txt','reddit_titles_tech.txt']
r_subs = ['askreddit','aww','books','fitness','food','funny','gaming','history','music','photography','science','technology']

c_comments = ['4chan_comments_b.txt','4chan_comments_c.txt','4chan_comments_ck.txt','4chan_comments_fit.txt','4chan_comments_g.txt','4chan_comments_his.txt',
'4chan_comments_lit.txt','4chan_comments_mu.txt','4chan_comments_p.txt','4chan_comments_sci.txt','4chan_comments_v.txt']
c_titles = ['4chan_titles_b.txt','4chan_titles_c.txt','4chan_titles_ck.txt','4chan_titles_fit.txt','4chan_titles_g.txt','4chan_titles_his.txt','4chan_titles_lit.txt',
'4chan_titles_mu.txt','4chan_titles_p.txt','4chan_titles_sci.txt','4chan_titles_v.txt']
c_boards = ['b','c','ck','fit','g','his','lit','mu','p','sci','v']

for rfile in r_comments:
    with open(rfile, 'w+') as cf:
        for line in cf.readlines():
            line.replace(' ... ', ' === ')

for cfile in c_comments:
    with open(cfile, 'w+') as cf:
        for line in cf.readlines():
            line.replace(' ... ',' === ')