formatemyinput=""
questions = ["How","how","Where","where","When","when","What","what"]
def punctuation(getInput):
    isquestion = False
    if any(word in getInput for word in questions):
        isquestion= True
    if isquestion==True:
        punc = "?"
    else:
        punc = "."

    return punc

while True:
    getInput= input("Say something:")

    if getInput=="\end":
        break
    else:
        formatemyinput = formatemyinput + getInput.capitalize() +punctuation(getInput)



print(formatemyinput)