file=open("sygnaly.txt","r")
words=[]
for line in file:
    words.append(line.rstrip())
file.close()
good_words=[]
for w in words:
    is_good=True
    prev_word=ord(w[0])
    for i in range(1,len(w)):
        curr_word=ord(w[i])
        if prev_word-curr_word>10 or curr_word-prev_word>10:
            is_good=False
            break
        #print(curr_word,prev_word)
        prev_word=curr_word
    if is_good:
        good_words.append(w)

for word in good_words:
    print(word)