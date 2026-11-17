# Name: [Ihita] [Joshi] - Group A
#
# FEATURE CHOSEN: (c) High score.
# Why: it makes me read results.csv a second time (not just write it), and it
# gives players a reason to replay the game and beat the best budget.
# [Rewrite this "why" in your own words before you hand in.]
#
# ---------------------------------------------------------------------------
# 1. WHAT GOES IN?
#    scenarios_A.csv: separator is a comma, first line is a header, 14 columns:
#    ID, Scenario, OptionA/B/C (texts), BudgetA/B/C (budget changes),
#    ReputationA/B/C (reputation changes), FeedbackA/B/C (feedback lines).
#    One scenario per line; the three options sit side by side in columns.
#    Numbers are plain whole numbers, negative with a "-" (-2000, 15) and no
#    thousands separator. Texts with commas or quotes are wrapped in "..."
#    and the csv module handles that. Everything is read as text, so I turn
#    the 6 impact columns into int myself.
#
# 2. WHAT HAPPENS? (one day)
#    - show the day number, both gauges, the situation and options A, B, C
#    - ask A, B or C until the answer is valid (a, b, c accepted)
#    - apply the budget and reputation change (reputation capped at 100)
#    - show the feedback line and the changes
#    - save the move in the history
#    - if a gauge is 0 or less, stop the game at once
#
# 3. WHAT COMES OUT?
#    At the end: fired (and why) or "Quarter survived!", budget and reputation,
#    score and title, best and worst move, and whether I beat the best budget.
#    One line is added to results.csv, for example:
#    Lea,6350,100,CMO Material,2026-11-17
#
# 4. WHAT COULD GO WRONG?
#    - the scenario file is missing -> message and clean exit, no crash
#    - a bad line in the scenario file (missing column, text instead of a
#      number) -> that line is skipped with a warning, the rest still loads
#    - the player types something other than A, B or C (or "AB", or nothing)
#      -> ask again until valid
#    - the player types no name -> "Player" is used
#    - budget or reputation reaches 0 or less -> game stops, "Fired"
#    - reputation would go above 100 -> capped at 100
#    - results.csv does not exist yet or has a broken line -> created / skipped
#    - Ctrl+C or Ctrl+D during the game -> polite exit
# ---------------------------------------------------------------------------

import csv
import os
import random
from datetime import date

START_BUDGET = 10000
START_REPUTATION = 50
MAX_REPUTATION = 100
DAYS = 10
CHOICES = ("A", "B", "C")
SCENARIO_FILE = "scenarios_A.csv"
RESULTS_FILE = "results.csv"


def file_path(filename):
    """Return the path of a file that sits next to this script."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)


def load_scenarios(filename):
    """Read the scenario file. Each scenario is (situation, {"A": option, ...})
    and each option is a tuple (text, budget_change, reputation_change, feedback)."""
    scenarios = []
    try:
        with open(file_path(filename), newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    options = {}
                    for letter in CHOICES:
                        options[letter] = (
                            row["Option" + letter].strip(),
                            int(row["Budget" + letter]),
                            int(row["Reputation" + letter]),
                            row["Feedback" + letter].strip(),
                        )
                    scenarios.append((row["Scenario"].strip(), options))
                except (KeyError, ValueError, TypeError, AttributeError):
                    print("Skipping a broken line in the scenario file (ID " + str(row.get("ID", "?")) + ").")
    except (FileNotFoundError, OSError):
        print("Cannot open " + filename + ". Put it in the same folder as the game.")
    return scenarios


def ask_name():
    """Ask the player's name; use 'Player' if nothing is typed."""
    name = input("What is your name? ").strip()
    if name == "":
        name = "Player"
    return name


def signed(number):
    """Format a change: +20, -2000, 0."""
    if number == 0:
        return "0"
    return f"{number:+d}"


def show_day(day, budget, reputation, scenario):
    """Print the header of a day: gauges, situation and the three options."""
    situation, options = scenario
    print()
    print(f"--- Day {day} ---")
    print(f"[Budget: {budget} EUR | Reputation: {reputation}/{MAX_REPUTATION}]")
    print(situation)
    for letter in CHOICES:
        print(f"  {letter}: {options[letter][0]}")


def ask_choice():
    """Ask for A, B or C until the answer is valid. Lowercase is accepted."""
    answer = input("Your choice (A, B or C): ").strip().upper()
    while answer not in CHOICES:
        answer = input("Please type A, B or C: ").strip().upper()
    return answer


def apply_choice(budget, reputation, option):
    """Apply an option to the gauges and return the new (budget, reputation).
    Reputation can never go above 100."""
    text, budget_change, reputation_change, feedback = option
    new_budget = budget + budget_change
    new_reputation = min(MAX_REPUTATION, reputation + reputation_change)
    return new_budget, new_reputation


def check_game_over(budget, reputation):
    """Return the reason the player is fired, or None if the game goes on."""
    if budget <= 0 and reputation <= 0:
        return "Your budget and your reputation both hit zero. Nothing left, not even croissants."
    if budget <= 0:
        return "Your budget hit zero: the bank says no."
    if reputation <= 0:
        return "Your reputation hit zero: the internet hates you."
    return None


def compute_score(budget, reputation):
    """Final score, only used when the player survives."""
    return reputation + budget // 200


def get_title(score):
    """Turn a score into a title."""
    if score < 95:
        return "Eternal Intern"
    if score < 120:
        return "Growth Hacker"
    if score < 140:
        return "CMO Material"
    return "Viral Legend"


def play_game(scenarios):
    """Play the days. Return (budget, reputation, history, fired_reason).
    history holds one tuple per day: (reputation_change, day, option_text)."""
    budget = START_BUDGET
    reputation = START_REPUTATION
    history = []
    fired_reason = None

    deck = scenarios[:]          # copy, so the original list stays untouched
    random.shuffle(deck)

    for day in range(1, min(DAYS, len(deck)) + 1):
        scenario = deck[day - 1]
        show_day(day, budget, reputation, scenario)
        letter = ask_choice()
        option = scenario[1][letter]
        text, budget_change, reputation_change, feedback = option

        budget, reputation = apply_choice(budget, reputation, option)
        history.append((reputation_change, day, text))

        print(feedback)
        print(f"Budget {signed(budget_change)} EUR, Reputation {signed(reputation_change)}")

        fired_reason = check_game_over(budget, reputation)
        if fired_reason is not None:
            break               # game over: the game stops at once

    return budget, reputation, history, fired_reason


def find_best_and_worst(history):
    """Best and worst move = biggest and smallest reputation change.
    The reputation change is the first element of each tuple."""
    best = max(history, key=lambda move: move[0])
    worst = min(history, key=lambda move: move[0])
    return best, worst


def read_best_budget(filename):
    """Read results.csv and return (best_budget, name), or None if there is
    no usable line yet."""
    records = []
    try:
        with open(file_path(filename), newline="", encoding="utf-8") as f:
            for row in csv.reader(f):
                try:
                    records.append((int(row[1]), row[0]))
                except (IndexError, ValueError):
                    pass        # empty or broken line: skip it
    except (FileNotFoundError, OSError):
        return None
    if len(records) == 0:
        return None
    return max(records)         # tuples compare by budget first


def save_result(filename, name, budget, reputation, title):
    """Append one line to results.csv: name, budget, reputation, title, date."""
    try:
        with open(file_path(filename), "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([name, budget, reputation, title, date.today().isoformat()])
        print("Saved in " + filename)
    except OSError:
        print("Could not save the result in " + filename + ".")


def show_ending(name, budget, reputation, fired_reason):
    """Show the final result and return the title."""
    print()
    print("=" * 30)
    if fired_reason is not None:
        title = "Fired"
        print("You are FIRED!")
        print(fired_reason)
        print(f"Budget: {budget} EUR, reputation: {reputation}/{MAX_REPUTATION}")
        print(f"{name}, your title: {title}")
    else:
        score = compute_score(budget, reputation)
        title = get_title(score)
        print("Quarter survived!")
        print(f"Budget left: {budget} EUR, reputation: {reputation}/{MAX_REPUTATION}")
        print(f"Final score: {score}")
        print(f"{name}, your title: {title}")
    return title


def show_best_and_worst(history):
    """Print the best and the worst move of the game."""
    best, worst = find_best_and_worst(history)
    best_change, best_day, best_text = best
    worst_change, worst_day, worst_text = worst
    print(f'Best move: day {best_day}, "{best_text}" ({signed(best_change)})')
    print(f'Worst move: day {worst_day}, "{worst_text}" ({signed(worst_change)})')


def show_high_score(budget, previous_best):
    """Feature (c): say whether the player beat the best budget so far."""
    if previous_best is None:
        print("High score: first game on record. You set the bar!")
        return
    best_budget, best_name = previous_best
    if budget > best_budget:
        print(f"NEW HIGH SCORE! You beat the best budget so far ({best_budget} EUR by {best_name}).")
    else:
        print(f"The best budget so far is {best_budget} EUR by {best_name}. You did not beat it.")


def main():
    print("=== SURVIVE THE QUARTER ===")
    print("You are the new marketing manager of Croissant Rocket.")
    print("Do not let your budget or your reputation hit zero.")
    print()

    scenarios = load_scenarios(SCENARIO_FILE)
    if len(scenarios) == 0:
        print("No scenario to play. The game cannot start.")
        return

    name = ask_name()
    previous_best = read_best_budget(RESULTS_FILE)    # read BEFORE saving this game

    budget, reputation, history, fired_reason = play_game(scenarios)
    title = show_ending(name, budget, reputation, fired_reason)

    if len(history) > 0:
        show_best_and_worst(history)
    show_high_score(budget, previous_best)
    save_result(RESULTS_FILE, name, budget, reputation, title)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
        print("Game interrupted. See you next quarter!")