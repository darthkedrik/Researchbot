import csv
import time

def ids_reader(f_name):
    outlist = []
    with open(f_name, 'r+') as f:
        idr = csv.reader(f)
        for line in idr:
            outlist.append(line)
    return outlist

    # csv reader of f_name
    # return list of strings
def ids_writer(post_id, f_name):
    with open(f_name, 'a+') as f:
        idw = csv.writer(f)
        idw.writerow(post_id)

def corpus_writer(site_name, data_input):

    corpus_name = site_name + '_' + time.strftime("%d_%m_%Y") + '_corpus.csv'

    if site_name == '4chan':
        board_input = data_input[0]
        post_input = data_input[1]
        with open(corpus_name, 'a+') as corn:
            corn.writerow([time.strftime("%d/%m"), site_name, board_input,
                           post_input.post_id, post_input.text_comment])
    elif site_name == 'reddit':
        sub_input = data_input[0]
        post_input = data_input[1]
        if data_input[2] == 'comment':
            with open(corpus_name, 'a+') as corn:
                corn.writerow([time.strftime("%d/%m"), site_name, sub_input,
                               post_input.id, post_input.body]) # As a wishlist marker, in the future I want this to include the score and gilded status of the comment/submission, as that is a better rating of the standing in the community
        elif data_input[2] == 'submission':
            with open(corpus_name, 'a+') as corn:
                corn.writerow([time.strftime("%d/%m"), site_name, sub_input,
                               post_input.id, post_input.text_comment])
        else:
            sys.exit("Error in writing to Corpus, exiting to protect data...")
    else:
        sys.exit("Error in writing to Corpus, exiting to protect data...")



def corpus_reader(corpus_file, limit_by_site=None, limit_by_board=None, limit_by_user=None,
                  limit_by_date=None):
    ret_list = []
    for x in [limit_by_date, limit_by_site, limit_by_user, limit_by_board]:
        if x == None:
            x = ''

    with open corpus_file as cf:
        datareader = csv.reader(cf)
        if limit_by_site in line[0]:
            if limit_by_board in line[] and limit_by_user in line[] and limit_by_date in line[]:
                ret_list.append(line)

    return ret_list
