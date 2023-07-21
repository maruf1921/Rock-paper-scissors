import random

your_point = 0
computer_point = 0
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
x = 0
images = [x,Rock, Paper, Scissors]
while(True):
    player_input = int(input("What do you choose? 1 = Rock, 2 = Paper , 3 = Scissors:\n"))
    if (player_input >3 or player_input<1):
        print("wrong input")
        break
    computer_input = random.randint(1, 3)

    dic = {1 : 'Rock', 2 : 'Paper' , 3 : 'Scissors'}
    
    print("You choose : ", dic[player_input],images[player_input] ,"\nComputer Choose : ", dic[computer_input],images[computer_input])

    if(player_input == computer_input):
        print("Tie","\nYour point :",your_point,"Computer point :",computer_point)
    elif(player_input ==1 and computer_input == 2):
        computer_point +=1
        print("You loose","\nYour point :",your_point,"Computer point :",computer_point)
        
    elif(player_input ==1 and computer_input == 3):
        your_point +=1
        
        print("You Win","\nYour point :",your_point,"Computer point :",computer_point)
    elif(player_input ==2 and computer_input == 1):
        your_point +=1
        
        print("You Win","\nYour point :",your_point,"Computer point :",computer_point)
    elif(player_input ==2 and computer_input == 3):
        computer_point +=1
        
        print("You loose","\nYour point :",your_point,"Computer point :",computer_point)
    elif(player_input ==3 and computer_input == 1):
        computer_point +=1
        
        print("You loose","\nYour point :",your_point,"Computer point :",computer_point)
    elif(player_input ==3 and computer_input == 2):
        your_point +=1
        
        print("You WIn","\nYour point :",your_point,"Computer point :",computer_point)
    
    print("\n")
    
    

