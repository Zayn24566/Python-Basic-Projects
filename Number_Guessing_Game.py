# ============================================
#          NUMBER GUESSING GAME
# ============================================
# The computer picks a random number.
# The player tries to guess it within limited attempts.

import random
import time


# ── Difficulty settings ──────────────────────────────────────────────────────
LEVELS = {
    "1": {"name": "Easy",   "range": (1, 50),  "attempts": 10},
    "2": {"name": "Medium", "range": (1, 100), "attempts": 7},
    "3": {"name": "Hard",   "range": (1, 200), "attempts": 5},
}


# ── Helper: get a valid integer input ────────────────────────────────────────
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  ⚠  Please enter a whole number.\n")


# ── Helper: choose difficulty ────────────────────────────────────────────────
def choose_difficulty():
    print("\n  Select Difficulty:")
    print("  [1] Easy   — 1 to 50,  10 attempts")
    print("  [2] Medium — 1 to 100,  7 attempts")
    print("  [3] Hard   — 1 to 200,  5 attempts")

    while True:
        choice = input("\n  Enter choice (1/2/3): ").strip()
        if choice in LEVELS:
            return LEVELS[choice]
        print("  ⚠  Invalid choice. Please enter 1, 2, or 3.")


# ── Helper: give a directional hint ─────────────────────────────────────────
def give_hint(guess, secret, low, high):
    if guess < secret:
        print(f"  📈  Too LOW!  (hint: the number is between {guess + 1} and {high})")
    else:
        print(f"  📉  Too HIGH! (hint: the number is between {low} and {guess - 1})")


# ── Calculate score based on attempts used ───────────────────────────────────
def calculate_score(attempts_used, max_attempts):
    base = 1000
    penalty = (attempts_used - 1) * (base // max_attempts)
    return max(base - penalty, 50)   # minimum score is 50


# ── Single round of the game ─────────────────────────────────────────────────
def play_round(level):
    low, high    = level["range"]
    max_attempts = level["attempts"]
    secret       = random.randint(low, high)

    print(f"\n  🎯  Guess the number between {low} and {high}.")
    print(f"  🔢  You have {max_attempts} attempts.\n")

    attempts_used = 0
    low_bound, high_bound = low, high   # shrinking hint range

    for attempt in range(1, max_attempts + 1):
        print(f"  Attempt {attempt}/{max_attempts}")
        guess = get_integer("  Your guess: ")
        attempts_used += 1

        if guess < low or guess > high:
            print(f"  ⚠  Out of range! Enter a number between {low} and {high}.\n")
            attempts_used -= 1   # don't count invalid range guesses
            continue

        if guess == secret:
            score = calculate_score(attempts_used, max_attempts)
            print(f"\n  🎉  CORRECT! The number was {secret}.")
            print(f"  ✅  You got it in {attempts_used} attempt(s).")
            print(f"  ⭐  Your Score: {score} points")
            return True, score

        # Update shrinking bounds for hints
        if guess < secret:
            low_bound = max(low_bound, guess + 1)
        else:
            high_bound = min(high_bound, guess - 1)

        give_hint(guess, secret, low_bound, high_bound)
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"  ⏳  {remaining} attempt(s) remaining.\n")

    # Out of attempts
    print(f"\n  ❌  GAME OVER! The number was {secret}.")
    print(f"  Better luck next time!")
    return False, 0


# ── Scoreboard (session only) ────────────────────────────────────────────────
scoreboard = []

def show_scoreboard():
    if not scoreboard:
        print("\n  No scores recorded yet.")
        return
    print("\n" + "=" * 40)
    print("          🏆  SCOREBOARD")
    print("=" * 40)
    ranked = sorted(scoreboard, key=lambda x: x["score"], reverse=True)
    for i, entry in enumerate(ranked, 1):
        print(f"  #{i}  {entry['level']:<8}  "
              f"Attempts: {entry['attempts']}   Score: {entry['score']}")
    print("=" * 40)


# ── Main program ─────────────────────────────────────────────────────────────
def main():
    print("=" * 45)
    print("       🎮  NUMBER GUESSING GAME")
    print("=" * 45)
    print("  Can you guess the secret number?")

    total_score = 0
    games_played = 0
    wins = 0

    while True:
        level = choose_difficulty()
        print(f"\n  🚀  Starting {level['name']} mode...", end="", flush=True)
        time.sleep(0.8)
        print(" GO!\n")

        won, score = play_round(level)
        games_played += 1
        total_score  += score

        if won:
            wins += 1
            scoreboard.append({
                "level":    level["name"],
                "attempts": level["attempts"],
                "score":    score,
            })

        # Session summary
        print(f"\n  📊  Session Stats → "
              f"Played: {games_played}  |  "
              f"Wins: {wins}  |  "
              f"Total Score: {total_score}")

        show_scoreboard()

        print()
        again = input("  🔁  Play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print(f"\n  Thanks for playing! Final Score: {total_score} 🏅")
            print("  Goodbye! 👋\n")
            break
        print("\n" + "-" * 45 + "\n")


if __name__ == "__main__":
    main()