
import json
from difflib import get_close_matches

def translate(word):
    word = word.lower();
    if word in content:
        return content[word]
    elif len(get_close_matches(word, content.keys())) > 0:
        user_choice = get_close_matches(word, content.keys());
        choice = input("Did you mean %s instead? Y for yes, N for no: " % user_choice[0])
        if (choice == "Y" or choice == "y"):
            return content[user_choice[0]]
        elif (choice == "N" or choice == "n"):
            if (len(user_choice) > 1):
                for x in user_choice:
                    choice = input("Did you mean %s instead? Y for yes, N for no: " % x)
                    if (choice == "Y" or choice == "y"):
                        return content[x]
                    elif (choice == "N" or choice == "n"):
                        continue
                    else:
                        return "Not There!!"
            else:
                return "Not There!"
        else:
            return "Wrong Key Pressed"
    else:
        return "Not There!!"


userInput = input("Enter a word: ")
content = json.load(open("data.json"))

output = translate(userInput)

if type(output == list):
    for items in output:
        print(items)
else:
    print(output)
