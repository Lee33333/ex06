def file_to_dict(files):
    file_dict = {}
    score_file = open(files)
    for line in score_file:
        line = line.rstrip()
        line = line.split(":")
        file_dict[line[0]] = line[1] 
    return file_dict

def sorting(dictss):
    listkeys = sorted(dictss)
    for item in listkeys:
        print "Restaurant: %s is rated at %s " % (item, dictss[item])

def main():
    file_dict = file_to_dict("scores.txt")
    sorting_file = sorting(file_dict)
    return sorting_file

if __name__ == "__main__":
    main()

# # # setup
# # create an empty scores dictionary
# restaurant_scores = {}
# # open the file 'sorted.txt'
# score_file = open("scores.txt")
# # # main loop
# # for each line in the file:
# for line in score_file:
# #     split the line by the separator ":"
#     line = line.rstrip()
#     line = line.split(":")
# #     using the first token as a key, insert the second token into the dictionary as a value
#     restaurant_scores[line[0]] = line[1] 

# create a list of keys
# listkeys = sorted(file_dict)
# print listkeys
# # for each key in the sorted keys:
# for item in listkeys:
# #     print the restaurant name and score
#     print "Restaurant: %s is rated at %s " % (item, file_dict[item])