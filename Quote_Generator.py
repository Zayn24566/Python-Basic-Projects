import random

# Quotes database
quotes = {
    "motivation": [
        "Push yourself, because no one else is going to do it for you.",
        "Don’t stop until you’re proud.",
        "Dream it. Wish it. Do it.",
        "Stay hungry, stay foolish."
    ],
    "life": [
        "Life is what happens when you're busy making other plans.",
        "In the end, we only regret the chances we didn’t take.",
        "Happiness depends upon ourselves.",
        "Turn your wounds into wisdom."
    ],
    "success": [
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "Don’t be afraid to give up the good to go for the great.",
        "Success usually comes to those who are too busy to be looking for it.",
        "Opportunities don’t happen. You create them."
    ]
}


quotes.update({
    "tech": [
        "First, solve the problem. Then, write the code.",
        "Code is like humor. When you have to explain it, it’s bad.",
        "Simplicity is the soul of efficiency.",
        "Talk is cheap. Show me the code."
    ],
    "adventure": [
        "Not all those who wander are lost.",
        "Adventure is worthwhile in itself.",
        "Collect moments, not things.",
        "Travel far enough, you meet yourself."
    ],
    "discipline": [
        "Discipline is choosing between what you want now and what you want most.",
        "Small steps every day add up to big results.",
        "We are what we repeatedly do.",
        "Hard work beats talent when talent doesn’t work hard."
    ]
})


# Get random quote
def get_quote(category=None):
    if category and category in quotes:
        return random.choice(quotes[category])
    else:
        all_quotes = sum(quotes.values(), [])
        return random.choice(all_quotes)


#  New: show categories dynamically
def show_categories():
    print("\n📂 Available Categories:")
    for key in quotes.keys():
        print(f"- {key}")
    print("- all")


# Main program
def main():
    print("💬 Advanced Quote Generator\n")

    while True:
        show_categories()

        choice = input("\nChoose category: ").lower()

        if choice == "all":
            category = None
        elif choice in quotes:
            category = choice
        else:
            print("❌ Invalid category, using random.\n")
            category = None

        try:
            count = int(input("How many quotes? "))
        except:
            count = 1

        print("\n✨ Your Quotes:\n")

        for i in range(count):
            print(f"{i+1}. {get_quote(category)}\n")

        again = input("Generate again? (y/n): ").lower()
        if again != "y":
            print("\n👋 Goodbye!")
            break


if __name__ == "__main__":
    main()