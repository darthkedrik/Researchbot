import basc_py4chan
import csv

def spybot(board_list):
    # Take a list of basc_py4chan.Board objects and iterate through,
    # write the id of each thread to appropriate id_file and write
    # data to 4chan datafile
    # Print which board we're running on while working
    for board in board_list:
        print("Currently pulling data from", board._board_name)
        all_threads = board.get_all_threads(expand=True)
        id_file = DATA_DIR + board._board_name + "_ids.csv"

        cur_ids = ids_reader(id_file)

        for thread in all_threads:
            for post in thread.posts:
                if post.post_id in cur_ids:
                    continue
                elif post.post_id not in cur_ids:
                    ids_writer(id_file, post.post_id)
                    post_data = [board, post]
                    corpus_writer('4chan', post_data)

def analysis():

'''
    Do we want to make another method for scraping data, potentially using
    scrapy?

    Do we want to implement other utilizations in 4chan such as creating
    specific corpora with user generated names?

    Do we want to create input methods and make this more user friendly for
    others to use, or is that even worth bothering with right now?

    Do we want to incorporate 4chan specific analysis in this same folder?

    '''
