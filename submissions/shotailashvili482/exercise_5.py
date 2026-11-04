def read_scores():
    scores = []
    while True:
        print("Score (or done):\n")
        user_input = input()
        if user_input.lower() == "done":
            break
        scores.append(int(user_input))
    return scores

def report(scores):
    if not scores:
        print("No scores.")
        return
    
    print(f"Scores: {scores}")
    print(f"Sorted: {sorted(scores)}")

    lowest = min(scores)
    highest = max(scores)
    average = sum(scores) / len(scores)

    print(f"Lowest {lowest}, highest {highest}, average {average}")


scores = read_scores()
report(scores)