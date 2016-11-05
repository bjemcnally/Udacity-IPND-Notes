import urllib

def read_text():
    quotes = open("C:/Users/bjerickson/Desktop/movie_quotes.txt")
    contents_of_file = quotes.read()
    # print contents_of_file
    quotes.close()
    check_profanity(contents_of_file)
    # make_piratey(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    # print output
    connection.close()
    if "true" in output:
        print ("Profanity alert!!")
    elif "false" in output:
        print ("This document has no curse words!")
    else:
        print ("Could not scan document properly.")

"""def make_piratey(text_to_check):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text=" + text_to_check)
    output = connection.read()
    # print output
    connection.close()
    print output"""

read_text()