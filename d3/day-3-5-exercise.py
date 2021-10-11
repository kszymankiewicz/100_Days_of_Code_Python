# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1 = name1.lower()
name1_count_t = int(name1.count("t"))
name1_count_r = int(name1.count("r"))
name1_count_u = int(name1.count("u"))
name1_count_e = int(name1.count("e"))
name1_count_l = int(name1.count("l"))
name1_count_o = int(name1.count("o"))
name1_count_v = int(name1.count("v"))  
name_1_sum = name1_count_t +name1_count_r + name1_count_u +name1_count_e +name1_count_l + name1_count_o + name1_count_v 

lower_name2 = name2.lower()
name2_count_t = int(name2.count("t"))

name2_count_r = int(name2.count("r"))
name2_count_u = int(name2.count("u"))
name2_count_e = int(name2.count("e"))
name2_count_l = int(name2.count("l"))
name2_count_o = int(name2.count("o"))
name2_count_v = int(name2.count("v"))  
name_2_sum = name2_count_t +name2_count_r + name2_count_u +name2_count_e +name2_count_l + name2_count_o + name2_count_v 

sum_count = name_2_sum + name_1_sum

print(f"T occurs {name1_count_t} times")
print(f"R occurs {name1_count_r} times")
print(f"U occurs {name1_count_u} times")
print(f"E occurs {name1_count_e} times")
print()
print(f"L occurs {name1_count_l} times")
print(f"O occurs {name1_count_o} times")
print(f"V occurs {name1_count_v} times")
print(f"TOTAL {name_1_sum}")
print()
print(f"T occurs {name2_count_t} times")
print(f"R occurs {name2_count_r} times")
print(f"U occurs {name2_count_u} times")
print(f"E occurs {name2_count_e} times")
print()
print(f"L occurs {name2_count_l} times")
print(f"O occurs {name2_count_o} times")
print(f"V occurs {name2_count_v} times")
print(f"TOTAL {name_2_sum}")

