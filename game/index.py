import random
def game(comp,you):
    if comp == "s":
        if you == "p":
            print("YOU LOOSE")
        elif you =="r":
            print("YOU WIN")
        elif you =="s":
            print("TIE")

    elif comp == "p":
        if you == "r":
            print("YOU LOOSE")
        elif you =="s":
            print("YOU WIN")
        elif you =="p":
            print("TIE")

    elif comp == "r":
        if you == "s":
            print("YOU LOOSE")
        elif you =="p":
            print("YOU WIN")
        elif you =="r":
            print("TIE")
    
#users turn 
your=input("Your turn: Scissor(s) or Paper(p) or Rock(r)\n")

#computer turn 
print("Computer turn: Scissor(1) or Paper(2) or Rock(3)")
randNo = random.randint(1,3)
print(randNo)
if randNo==1:
    comp="s"
elif randNo==2:
    comp="p"
elif randNo==3:
    comp="r" 


game(comp,your)
