import random
# Expanded list of spells
spells = [
    "Expelliarmus",      # Disarming
    "Stupefy",           # Stunning
    "Rictusempra",       # Tickling
    "Expecto Patronum",  # Patronus charm
    "Avada Kedavra",     # Killing curse
    "Crucio",            # Torture curse
    "Imperio",           # Control curse
    "Protego",           # Shield charm
    "Lumos",             # Wand light
    "Nox",               # Wand extinguish
    "Accio",             # Summoning
    "Wingardium Leviosa",# Levitation
    "Sectumsempra",      # Dark cutting curse
    "Obliviate",         # Memory charm
    "Petrificus Totalus",# Full body bind
    "Reducto",           # Blasting curse
    "Incendio",          # Fire spell
    "Alohomora"          # Unlocking charm
]

# Points system
spell_points = {spell: 100 for spell in spells}
spell_points["Avada Kedavra"] = 300  # Special case

# Scores
player_score = 0
computer_score = 0

print("⚡ Welcome to the Harry Potter Duel Club! ⚡")
print("Spells available:", ", ".join(spells))
print("Each spell win = 100 points, Avada Kedavra = 300 points.\n")

# Game loop
while True:
    # Player chooses spell
    player_spell = input("Choose your spell (or type 'quit' to exit): ").strip().title()
    
    if player_spell.lower() == "quit":
        break
    
    if player_spell not in spells:
        print("Invalid spell! Try again.\n")
        continue
    
    # Computer chooses spell
    computer_spell = random.choice(spells)
    print(f"Computer casts: {computer_spell}")
    
    # Decide winner (simple random outcome)
    winner = random.choice(["player", "computer", "draw"])
    
    if winner == "player":
        player_score += spell_points[player_spell]
        print(f"You won this round! +{spell_points[player_spell]} points.\n")
    elif winner == "computer":
        computer_score += spell_points[computer_spell]
        print(f"Computer won this round! +{spell_points[computer_spell]} points.\n")
    else:
        print("It's a draw! No points awarded.\n")
    
    # Show scores
    print(f"Scores → You: {player_score} | Computer: {computer_score}\n")

print("Thanks for playing the Harry Potter Duel Club!")