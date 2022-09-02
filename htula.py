import random


def draw():
    numbers=[]
    for i in range (0,5):
        if len(numbers) < 5:
            numbers.append(random.randint(1,91))
    return numbers
print("Welcome to HTU-LA, licensed and approved by the national lottery authority,Fear is a disease,NO RISK,NO REWARD!!")
SHORT_CODE=input("enter our shortcode to begin process  ")
if SHORT_CODE=='419':
    option=int(input(" Choose an event \n 1. Monday Special \n 2. Lucky Tuesday \n 3. Wednesday Mid-week\n 4. Fortune Thursday \n 5. Friday Bonanza\n 6. National Saturday\n 7.Draw Results\n option : "))
    if option in range(1,7):
        option_f=int(input(" \n  1. One-Direct \n  2. Two-sure \n 3. Three-Direct \n 4. Four-Direct \n 5. Five-Direct \n Option : "))
        if option_f==1:
            amount=int(input("Enter Amount \n :"))
            
            x=int(input("Enter your stake"))
            if x<91:
                print(x)
                list=[x]
                print(draw())
                if list not in draw():
                    print("Unfortunately,your numbers are not in our winning group today. ")
                else:
                    print("Good luck" , x , " is your winning numbers")
            else:
                print("you can only stake between 1-90")
                
        elif  option_f==2:
            amount=int(input("Enter Amount \n :"))
            x=int(input("Enter your stake: "))
            y=int(input("Enter your stake: "))
            list=[x,y]
            if x<91 and y<91:
               print(list)
               print(draw())
               win_lose=[]
               for number in list:
                   if number in draw():
                       if  number not in win_lose:
                           win_lose.append(number)
               if win_lose ==[]:
                   print("Unfortunately your numbers are not in our winning group today. ")
               else:
                   print("Good luck" , win_lose, " are your winning numbers")
            else:
                print("choose numbers only between range 1-90")
                
        elif option_f==3:
            amount=int(input("Enter Amount \n :"))
            x=int(input("Enter your stake:  "))
            y=int(input("Enter your stake:  "))
            z=int(input("Enter your stake:  "))
            list=[x,y,z]
            if x<91 and y<91 and z<91:
               print(list)
               print(draw())
               win_lose=[]
               for number in list:
                   if number in draw():
                       if number in win_lose:
                           win_lose.append(number)
               if win_lose ==[]:
                   print("You lost")
               else:
                   print("Good luck ", win_lose )
            else:
                print("choose numbers only between range 1-90")
                
        elif option_f==4:
            amount= int(input("Enter Amount \n :"))
            x=int(input("Enter your stake:  "))
            y=int(input("Enter your stake:  "))
            z=int(input("Enter your stake:  "))
            v=int(input("Enter your stake:  "))
            list=[x,y,z,v]
            if x<91 and y<91 and z<91 and v<91:
               print(list)
               print(draw())
               win_lose=[]
               for number in list:
                   if number in draw():
                       if number not in win_lose:
                           win_lose.append(number)
               if win_lose ==[]:
                   print("Unfortunately,your numbers are not in our winning group today. ")
               else :
                   print("congratulation", win_lose, "are your winning numbers")
            else:
                print("choose numbers only between range 1-90 , Try again ")
        elif option_f==5:
            amount=int(input("Enter Amount \n :"))
            x=int(input("Enter your stake:  "))
            y=int(input("Enter your stake:  "))
            z=int(input("Enter your stake:  "))
            v=int(input("Enter your stake:  "))
            q=int(input("Enter your stake:  "))
            list=[x,y,z,v,q]
            if x<91 and y<91 and z<91 and v<91 and q<91:
               print(list)
               print(draw())
               win_lose=[]
               for number in list:
                   if number in draw():
                       if number not in win_lose:
                           win_lose.append(number)
               if win_loose ==[]:
                   print("Unfortunately,your numbers are not in our winning group today. ")
               else:
                   print("congratulation", win_lose, "are your winning numbers")
            else:
                print("choose numbers only between range 1-90 , Try again ")
            
        else:
            print("invalid input")
        
    elif option==7:
        print ("Our latest draw results are:\n",draw())
    else:
            print("invalid input")  
else:
    print("invalid pin")
