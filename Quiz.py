# ============================================
#       PYTHON PROGRAMMING QUIZ GAME
#           True / False Edition
# ============================================

import random
import time

# ── Question Bank ────────────────────────────────────────────────────────────
QUESTIONS = [
    # Basics
    {"question": "Python is a compiled language.",                                          "answer": False},
    {"question": "Python uses indentation to define code blocks.",                          "answer": True},
    {"question": "In Python, you must declare a variable's type before using it.",          "answer": False},
    {"question": "Python is case-sensitive, so 'name' and 'Name' are different variables.", "answer": True},
    {"question": "The '#' symbol is used to write comments in Python.",                     "answer": True},
    {"question": "Python indexes start at 1.",                                              "answer": False},
    {"question": "A Python tuple is mutable (can be changed after creation).",              "answer": False},
    {"question": "Python lists can store different data types at the same time.",           "answer": True},
    {"question": "The len() function returns the length of a string or list.",              "answer": True},
    {"question": "In Python, '==' checks assignment, not equality.",                        "answer": False},

    # Functions & OOP
    {"question": "A function defined with 'def' can return multiple values.",               "answer": True},
    {"question": "Lambda functions can contain multiple statements.",                       "answer": False},
    {"question": "The 'self' keyword in a class method refers to the class itself.",        "answer": False},
    {"question": "Python supports multiple inheritance.",                                   "answer": True},
    {"question": "A constructor method in Python is named __init__.",                       "answer": True},
    {"question": "Decorators in Python are used to modify the behavior of functions.",      "answer": True},
    {"question": "Global variables can be changed inside a function without 'global'.",     "answer": False},
    {"question": "Default arguments in a function must come before required arguments.",    "answer": False},

    # Data Structures
    {"question": "Dictionary keys in Python must be unique.",                               "answer": True},
    {"question": "Python sets allow duplicate values.",                                     "answer": False},
    {"question": "You can use a list as a dictionary key in Python.",                       "answer": False},
    {"question": "The pop() method removes the last item from a list by default.",         "answer": True},
    {"question": "Strings in Python are immutable.",                                        "answer": True},
    {"question": "A frozenset is a mutable version of a set.",                              "answer": False},

    # Modules & Files
    {"question": "The 'import' statement is used to include external modules in Python.",   "answer": True},
    {"question": "Python's 'os' module is used for interacting with the operating system.", "answer": True},
    {"question": "You need to install the 'random' module separately using pip.",           "answer": False},
    {"question": "The 'with' statement is used for file handling and resource management.", "answer": True},

    # Error Handling
    {"question": "A 'try' block must always be followed by an 'except' block.",             "answer": True},
    {"question": "The 'finally' block runs only if no exception occurs.",                   "answer": False},

    # 🟢 Easy — Added by user
    {"question": "print('Hello') is used to display output in Python.",                     "answer": True},
    {"question": "Variables in Python must be declared before use.",                        "answer": False},

    # 🟡 Medium — Added by user
    {"question": "Lists in Python are immutable.",                                          "answer": False},
    {"question": "Tuples in Python cannot be changed after creation.",                      "answer": True},
    {"question": "A dictionary stores data in key-value pairs.",                            "answer": True},
    {"question": "None is the same as 0 in Python.",                                        "answer": False},
    {"question": "Functions in Python must always return a value.",                         "answer": False},

    # 🔴 Hard — Added by user
    {"question": "'is' and '==' are the same in Python.",                                   "answer": False},
    {"question": "Default arguments in functions are evaluated only once.",                 "answer": True},
    {"question": "*args is used to pass a variable number of arguments to a function.",     "answer": True},
    {"question": "**kwargs is used to pass keyword arguments to a function.",               "answer": True},
    {"question": "A generator function uses 'yield' instead of 'return'.",                  "answer": True},
    {"question": "Python automatically frees unused memory through garbage collection.",    "answer": True},
    {"question": "Lambda functions can have multiple expressions.",                         "answer": False},
]


# ── Difficulty settings ───────────────────────────────────────────────────────
LEVELS = {
    "1": {"name": "Easy",   "questions": 5,  "time_limit": None},
    "2": {"name": "Medium", "questions": 10, "time_limit": None},
    "3": {"name": "Hard",   "questions": 15, "time_limit": None},
}


# ── Get valid T/F answer from user ────────────────────────────────────────────
def get_answer():
    while True:
        ans = input("  Your answer (T / F): ").strip().lower()
        if ans in ("t", "true"):
            return True
        elif ans in ("f", "false"):
            return False
        else:
            print("  ⚠  Please type T for True or F for False.\n")


# ── Choose difficulty ─────────────────────────────────────────────────────────
def choose_difficulty():
    print("\n  Select Difficulty:")
    print("  [1] Easy   —  5 questions")
    print("  [2] Medium — 10 questions")
    print("  [3] Hard   — 15 questions")
    while True:
        choice = input("\n  Enter choice (1/2/3): ").strip()
        if choice in LEVELS:
            return LEVELS[choice]
        print("  ⚠  Invalid choice. Enter 1, 2, or 3.")


# ── Display result feedback ───────────────────────────────────────────────────
def feedback(correct, right_answer):
    if correct:
        print("  ✅  Correct!\n")
    else:
        label = "True" if right_answer else "False"
        print(f"  ❌  Wrong! The correct answer was: {label}\n")


# ── Grade the player ──────────────────────────────────────────────────────────
def get_grade(score, total):
    pct = (score / total) * 100
    if pct == 100:
        return "🏆 Perfect!", pct
    elif pct >= 80:
        return "🥇 Excellent!", pct
    elif pct >= 60:
        return "🥈 Good Job!", pct
    elif pct >= 40:
        return "🥉 Keep Practicing!", pct
    else:
        return "📚 Needs Improvement", pct


# ── Play one quiz round ───────────────────────────────────────────────────────
def play_quiz(level):
    total_q   = level["questions"]
    pool      = random.sample(QUESTIONS, min(total_q, len(QUESTIONS)))

    score     = 0
    wrong     = []

    print(f"\n  📋  {total_q} questions | Answer with T (True) or F (False)")
    print("  " + "-" * 42 + "\n")
    time.sleep(0.5)

    for i, item in enumerate(pool, 1):
        print(f"  Q{i}) {item['question']}")
        user_ans = get_answer()
        correct  = (user_ans == item["answer"])

        feedback(correct, item["answer"])

        if correct:
            score += 1
        else:
            wrong.append(item)

    # ── Results ──────────────────────────────────────────────────────────────
    grade_label, pct = get_grade(score, total_q)

    print("=" * 45)
    print("            📊  QUIZ RESULTS")
    print("=" * 45)
    print(f"  Score      : {score} / {total_q}")
    print(f"  Percentage : {pct:.1f}%")
    print(f"  Grade      : {grade_label}")
    print("=" * 45)

    # ── Review wrong answers ──────────────────────────────────────────────────
    if wrong:
        print(f"\n  📝  Review — Questions you got wrong ({len(wrong)}):\n")
        for j, item in enumerate(wrong, 1):
            label = "True" if item["answer"] else "False"
            print(f"  {j}. {item['question']}")
            print(f"     ✔ Answer: {label}\n")

    return score, total_q


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("=" * 45)
    print("    🐍  PYTHON PROGRAMMING QUIZ GAME")
    print("         True / False Edition")
    print("=" * 45)
    print("  Test your Python knowledge!")

    session_score = 0
    session_total = 0
    rounds        = 0

    while True:
        level = choose_difficulty()

        print(f"\n  🚀  Starting {level['name']} Quiz...", end="", flush=True)
        time.sleep(0.8)
        print(" BEGIN!\n")

        score, total   = play_quiz(level)
        session_score += score
        session_total += total
        rounds        += 1

        print(f"\n  🗂  Session → Rounds: {rounds}  |  "
              f"Total Score: {session_score}/{session_total}")

        print()
        again = input("  🔁  Play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print(f"\n  Thanks for playing! 🐍")
            print(f"  Final Score: {session_score}/{session_total} — Keep learning Python! 💪\n")
            break
        print("\n" + "-" * 45 + "\n")


if __name__ == "__main__":
    main()