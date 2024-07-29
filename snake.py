import random
'''
 1 for snake 
-1 for water 
 0 for gun 

'''
values = [-1, 0, 1]
computer =random.choice(values)
youstr=(input("Enter your choice "))
youDict={"s":1,"w":-1,"g":0}
reversedic={1:"snake",-1:"Water",0:"gun"}
you=youDict[youstr]

print(f" You choose {reversedic[you]}\n computer choose {reversedic[computer]}")
if(computer==you):
    print("MAtch has been drawn ")

elif (computer==-1 and you==1):
    print("you won  ")
elif (computer==-1 and you==0):
    print(" you lose ") 
elif (computer==1 and you ==-1 ):
    print("You lose ")
elif (computer==1 and you ==0):
    print("you won ")
elif (computer==0 and you ==1):
    print("you won ")
elif (computer==1 and you ==-1):
    print("you lose ")        
else :
    print("something went wrong ")        
       
       

    

















