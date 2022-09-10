#Write file 
fp=open("vipul.txt","a")
Name=str(input("name:"))
fp.write(Name+"\n")
std=str(input("Std:"))
fp.write(std+"\n")
Id=str(input("ID:"))
fp.write(Id+"\n\n")
fp.close()
print("click 1 to read or click enter")
a=int(input())
if(a==1):
    #Read file
    fp=open("vipul.txt","r")
    print(fp.read())
    fp.close()
else:
    exit(1)
