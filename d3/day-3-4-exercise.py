# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
if size == "S" and "s":
    print("You choose small pizza") 
    bill += 15 

elif size == "M" and "m":
    print("You choose medium pizza")
    bill += 20
    
elif size == "L" and "l":
    print("You choose large pizza")
    bill += 25

if add_pepperoni == "Y" and "y":
    if size == "S" and "s":
        print("With peperoni.")
        bill+=2
        
    else:
        bill+=3
if extra_cheese == "Y" and "y":
    print("And with extra cheese.")
    bill+=1
    

print(f"Your final bill is ${bill}")