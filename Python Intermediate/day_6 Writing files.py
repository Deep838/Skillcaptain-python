import random

# List of syllables for creating character names
syllables = [
    "abe", "bar", "cio", "dan", "er", "fi", "ga", "har", "il", "jo", "kar", "lo",
    "mi", "na", "o", "pi", "qua", "ri", "si", "tu", "ve", "wil", "xi", "yo", "za"
]

# Function to generate a random character name with 3 syllables
def generate_character_name(used_names):
    while True:
        name = random.choice(syllables) + random.choice(syllables) + random.choice(syllables)
        capitalized_name = name.capitalize()
        if capitalized_name not in used_names:
            used_names.add(capitalized_name)
            return capitalized_name

# Ask the user for the number of character names to generate
num_names = int(input("Enter the number of character names to generate: "))

# Generate unique character names
used_names = set()
character_names = [generate_character_name(used_names) for _ in range(num_names)]

# Save the generated character names in a text file
with open("character_names.txt", "w") as file:
    for name in character_names:
        file.write(name + "\n")

print(f"{num_names} character names have been generated and saved to 'character_names.txt'.")
