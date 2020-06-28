def spin_words(sentence):
    # Your code goes here
    lst = list(sentence.split(" "))
    spinlst = []
    spinsentence = ""
    for i in lst:
        if len(i)>=5:
            rev = i[len(i): :-1]
        else:
            rev = i
        spinlst.append(rev)
    spinsentence = spinsentence.join(spinlst)
    return spinsentence



print(spin_words("Welcome"))

