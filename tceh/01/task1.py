# Riddle game

answer = ""

while answer != "paper":
    answer = input("You can drop me from the tallest and I'll be fine, but if you drop me in water I die. What am I? ").lower()
    
    if answer == "paper":
        print("Congratulations! Your answer is correct.")
        