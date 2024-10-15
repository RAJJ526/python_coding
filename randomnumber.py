import random
winning_number = random.randint(1,100)
for i in range(1,4):
    guess_number = input('enter your guessing number')
    int_guess_number = int(guess_number)
    if int_guess_number == winning_number:
        print('you win', winning_number)
        break
    else:
        print('your number is wrong please enter again')
        if i == 3:
            print('game over', winning_number)


# import random
# winning_number = random.randint(1,100)
# for i in range(1,4):
#     guess_number = input('enter your guessing number')
#     int_guess_number = int(guess_number)
#     if int_guess_number == winning_number:
#         print('you win', winning_number)
#         break
#     else:
#         print('your number is wrong please enter again')
#         if i == 3:
#             print('game over', winning_number)

# winning_number = 54
# for i in range(1,8):
#     guess_number = input('enter your number')
#     int_guess_number = int(guess_number)
#     if int_guess_number == winning_number:
#         print('you win', winning_number)
#         break
#     else:
#         print('your number is wron please enter again ')
#         if i == 7:
#             print('game over', winning_number)

# import random
# lucky_number=random.randint(1,50)
# for i in range(1,6):
#     user_number = input('enter your number')
#     user_number = int(user_number)
#     if user_number == lucky_number:
#         print('your win', lucky_number)
#         break
#     else:
#         print('your number is wrong please enter again')
#         if i == 5:
#             print('better luck next time', lucky_number)

# winning_number = 54
# for i in range(1,8):
#     guess_number = input('enter your number')
#     int_guess_number = int(guess_number)
#     if int_guess_number == winning_number:
#         print('you win', winning_number)
#         break
#     else:
#         print(' your number is wrong please enter again ')
#         if i == 7:
#             print('game over', winning_number)


# lottrey_number=76
# for i in range(1,6):
#     your_number=input("enter your number:")
#     lucky_number=int(your_number)
#     if lucky_number==lottrey_number:
#         print("you win", lottrey_number)
#         break
#     else:
#         print("you lose", lottrey_number)
#         if i==3:
#             print("game over", lottrey_number)

# import random
# lucky_number=random.randint(1,50)

# import random
# winning_number=random.randint(1,50)
# for i in range(1,9):
#     guessing_number=input("enter your number")
#     int_guessing_number=int(guessing_number)
#     if int_guessing_number==winning_number:
#         print("you win", winning_number)
#         break
#     else:
#         print("try again")
#         if i==4:
#             print("game over")



    
       





    
   
    


            


    