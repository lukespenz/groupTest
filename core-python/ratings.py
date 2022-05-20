dict = {}  # empty dict to place key value pairs of the resturuants and ratings

# declares new variable "scores" to store the text from the scores.txt file
with open("scores.txt", 'r') as scores:
    for lines in scores:  # for loop goes through every line in the .txt doc
        # strips the whitespace and splits into an array wherever there's a colon
        line = lines.rstrip().split(':')
        # destructures the line array into two new variables, the names and ratings
        name, rating = line
        score_dict = {
            name: rating
        }  # puts the names and ratings into a dictionary to be set as a key-value pair in the real dictionary
        dict.update(score_dict)


def sortDict():
    print(dict)
    lst = dict.items()  # turns the dictionary into a list to be sorted
    # sorts list alphabetically by the key. the lambda is a function which keeps the values connected to the keys
    name_rating = sorted(lst, key=lambda x: x[0])
    for item in name_rating:  # for loop through the names and ratings which prints a sentence with the proper info
        print(item[0] + " is rated at " + item[1] + ".")


new_restaurant = str(input("What's a restaurant you would like to add?\n"))
new_score = str(input("What would you rate this place from 1 - 5?\n"))
score_dict = {new_restaurant: new_score}

dict.update(score_dict)
sortDict()