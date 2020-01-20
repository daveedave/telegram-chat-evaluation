import argparse
import time
import json
import numpy as np
from collections import Counter


start = time.time()
string_array = np.array([])
char_array = np.array([])
words = []
final_list = []
most_occur = []

#argparse
parser = argparse.ArgumentParser(description='This little script will output the most used words')
parser.add_argument('--filepath', metavar='f', help='filepath to your json export', required=True)
parser.add_argument('--name', metavar='n', help='add the name of an username', required=True)


args = parser.parse_args()

def main():
    global string_array
    global char_array
    global words
    global final_list
    global Counter
    global most_occur




    
    with open(args.filepath) as f:
        d = json.load(f)

    #spereate info of json file in more usable smaller parts
    profile_pics = d["profile_pictures"]
    contacts = d["contacts"]
    c_list = contacts["list"]
    chats = d["chats"]
    chat_list = chats["list"]
    

    #get all messages from name
    for item in chat_list:
    
        if len(item) == 4:
            if item["name"] == args.name:
            
                for i in range(len(item["messages"])):
            #print(item["messages"][i]["text"])
                    string_array = np.append(string_array , item["messages"][i]["text"])
        

    
    #split and append to word list
    for item in string_array:
        if isinstance(item, str):
            split_it = item.split()
            words.append(split_it)



    #add every word to list
    for item in words:
    
        final_list = final_list + item
      
    #calculate most common word
    go = [x.upper() for x in final_list]
    Counter = Counter(go) 
    most_occur = Counter.most_common(10) #this number can be modfied. Right now only 10 most common words are displayed
    print(most_occur)


    #print(d)
    #print(args.name)






main()


#only to save output 
#with open("words_with_" + str(args.name) + ".txt", "w") as output:
    #output.write(str(most_occur))


end = time.time() - start 
print('This script took:', end, ' seconds')