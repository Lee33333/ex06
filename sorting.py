
# # setup
# create an empty scores dictionary
restaurant_scores = {}
# open the file 'sorted.txt'
score_file = open("scores.txt")
# # main loop
# for each line in the file:
for line in score_file:
#     split the line by the separator ":"
    line = line.rstrip()
    line = line.split(":")
#     using the first token as a key, insert the second token into the dictionary as a value
    restaurant_scores[line[0]] = line[1] 

# create a list of keys
listkeys = sorted(restaurant_scores)
# for each key in the sorted keys:
for item in listkeys:
#     print the restaurant name and score
    print "Restaurant: %s is rated at %s " % (item, restaurant_scores[item])