def sentence_maker(phrase):
    questions=("How","When","Where","Who")
    capitalized=phrase.capitalize()
    if capitalized.startswith(questions):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

result=[]
while True:

    sentence=input("Say something:")
    if sentence=="\end":
        break
    else:
        result.append(sentence_maker(sentence))

def joinlist(result):
    sen=""
    for items in result:
        sen = sen + items

    return sen

#print(joinlist(result))
print(" ".join(result))