import random

# Word lists (you can expand these)
adjectives = [
    "Radioactive", "Galactic", "Arcane", "Mythic", "Stealthy", 
    "Invincible", "Cybernetic", "Lethal", "Cosmic", "Legendary",
    "Crimson", "Golden", "Misty", "Fierce", "Ethereal", 
    "Neon", "Ancient", "Swift", "Frosty", "Vibrant",
    "Noir", "Debonair", "Unhinged", "High-octane", "Dystopian",
    "Grizzled", "Stoic", "Galvanizing", "Cinematic", "Renegade"
]
nouns = [
    "Sentinel", "Titan", "Wraith", "Avatar", "Slayer", 
    "Guardian", "Android", "Raider", "Phoenix", "Knight","Captain","Python"
    ,"Phoenix", "Wolf", "Canyon", "Summit", "Falcon", 
    "Nebula", "Obsidian", "Thunder", "Willow", "Panther",
    "Protagonist", "Outlaw", "Flashback", "Odyssey", "Montage",
    "Sidekick", "Spectacle", "Heist", "Drifter", "Paradox"
]

symbols = ["!", "@", "#", "$", "%", "&"]

# Generate readable password
def generate_password(num_words=2, add_number=True, add_symbol=True):
    words = random.sample(adjectives + nouns, num_words)
    password = "".join(words)

    if add_number:
        password += str(random.randint(10, 999))

    if add_symbol:
        password += random.choice(symbols)

    return password


# Password strength checker
def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in symbols for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1

    if score == 4:
        return "Strong 💪"
    elif score == 3:
        return "Medium ⚡"
    else:
        return "Weak ⚠️"


# Main program
def main():
    print("🔐 Readable Password Generator\n")

    while True:
        try:
            count = int(input("How many passwords you want? "))
            words = int(input("How many words per password (2-4 recommended)? "))
        except ValueError:
            print("❌ Please enter valid numbers.\n")
            continue

        add_number = input("Add numbers? (y/n): ").lower() == "y"
        add_symbol = input("Add symbols? (y/n): ").lower() == "y"

        print("\nGenerated Passwords:\n")

        for i in range(count):
            pwd = generate_password(words, add_number, add_symbol)
            strength = check_strength(pwd)
            print(f"{i+1}. {pwd}  --> {strength}")

        again = input("\nGenerate again? (y/n): ").lower()
        if again != "y":
            print("\n👋 Goodbye!")
            break


if __name__ == "__main__":
    main()