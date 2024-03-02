file=open("sygnaly.txt","r")
temp_word=""
result=""
temp=file.readlines()
for i in range(1,len(temp)+1):
    temp_word=temp[i-1].rstrip()
    if i>=40 and i%40==0:
        result+=temp_word[9]
file.close()
print(result)