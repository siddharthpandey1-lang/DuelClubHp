print("Lets get you sorted into a house!")
# Assuming a variable 'house' is defined based on some criteria
print("there are four houses in Hogwarts School of Witchcraft and Wizardry:")
print("1. Gryffindor - known for bravery and courage.")
print("2. Hufflepuff - known for loyalty and hard work.")
print("3. Ravenclaw - known for intelligence and wisdom.")
print("4. Slytherin - known for ambition and cunning.")
house = input("Please enter your Qualities (Gryffindor, Hufflepuff, Ravenclaw, Slytherin): ")
print("Based on your qualities, you have been sorted into Gryffindor!")
print("Welcome to Gryffindor, the house of bravery and courage!")
if house == 'Hufflepuff':
    print("Based on your qualities, you have been sorted into Hufflepuff!")
    print("Welcome to Hufflepuff, the house of loyalty and hard work!")
elif house == 'Ravenclaw':
    print("Based on your qualities, you have been sorted into Ravenclaw!")
    print("Welcome to Ravenclaw, the house of intelligence and wisdom!")
else:
    print("Based on your qualities, you have been sorted into Slytherin!")
    print("Welcome to Slytherin, the house of ambition and cunning!")