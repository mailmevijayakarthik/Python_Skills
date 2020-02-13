import re
def reverseme(sentence):

    word = re.compile("\\s")
    mylist=word.split(sentence)
    print(mylist[::-1])
    for word in mylist:
        print(word[::-1])


reverseme("I am vijaykarthik")
