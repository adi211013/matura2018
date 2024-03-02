file=open("sygnaly.txt","r")
dict={}
max_word=[]
max_counter=0
for line in file:
    dict={}
    line=line.rstrip()
    for x in line:
        if x in dict:
            dict[x]+=1
        else:
            dict[x]=1
    if len(dict)>max_counter:
        max_counter=len(dict)
        max_word=line

file.close()
print(max_word,max_counter)