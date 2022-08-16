''' CORRECT THE WORD '''
'''SIMPLE WORD GAME'''
k=0   
def Forcheck(a,*args1):
    global k
    t=1
    for i in args1:
         if (a==i):
             print("\t\t*YOU WON**\t\t","NEXT:")
             k+=1
             break
         else:
             t=t+1
             if t>len(args1):
                 print("TRY AGAIN::-",end="")
                 ans=str(input())
                 if (ans=='1'):
                     Hints(*Hint_words)
                 else:
                     Forcheck(ans.lower(),*listOfWords)

def Hints(*args2):
    for i in args2:
        global k
        print(args2[k])
        print("LETS DO IT NOW::-",end="")
        ans=str(input())
        Forcheck(ans,*listOfWords)
        break
        
listOfWords=["bubble","kite","snake","queen","language","elephant","beautiful","water","dengerous","train","amazing"]
listOfRandom_W=["itek","fulbeutia","eblbub","ansek","nqeeu","langeuag","telphnae","tware","gerdenuso","raint","ingimza"]
Hint_words=["a bird","oposite to 'UGLY'","a circular smooth thing","one of poisonus","wife of king","language","a animal","a life","harmful to health","a vehicle","compliment to nice"]
print("\t::::::::::: PLAY ::::::::::")
print("\n\t______::For Hint:CLICK 1::_______\t\t")
for i in range (len(listOfRandom_W)): 
    print("\n"+listOfRandom_W[i])
    print("SOLVE::",end="")
    ans=str(input())
    if (ans=='1'):
        Hints(*Hint_words)
    else:
        Forcheck(ans.lower(),*listOfWords)

print("***YOU WON***")