from nltk import word_tokenize
import sys

SIMPLEFILE = "words.txt"

def main():
    verifyArgCount()
    userFile = sys.argv[1]
    userWords = getWords(userFile)
    simpleWords = getWords(SIMPLEFILE)
    matches = [ word for word in userWords if(word.isalpha() and word.lower() not in simpleWords) ]
    matches = uniq(matches)
    if(notEmpty(matches)):
        print("The following words aren't simple: ")
        print(sorted(matches))
    else:
        print("Text is simple!")

def getWords(filepath):
    with open(filepath) as infile:
        return word_tokenize(infile.read())

def verifyArgCount():
    if(len(sys.argv) != 2):
        print("Invalid number of arguments. Provide a file to check.")
        exit()

def uniq(l):
    result = []
    for item in l:
        if(item not in result):
            result.append(item)
    return result

def notEmpty(l):
    return len(l) > 0

if __name__ == "__main__":
    main()
