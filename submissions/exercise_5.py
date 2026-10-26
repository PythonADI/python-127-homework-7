def read_scores():
    """Read scores until done is entered and return the list."""
    scores = []

    while True:
        print("Score (or done):")
        answer = input()
        if answer == "done":
            return scores
        scores.append(int(answer))

def report(scores):
    """Print the original scores, sorted scores, and summary."""
    if not scores:
        print("No scores.")
        return
    ordered = sorted(scores)
    average = sum(scores) / len(scores)

    print("Scores:", scores)
    print("Sorted:", ordered)
    print(
        f"Lowest {ordered[0]}, highest {ordered[-1]}, average {average}"
    )
scores = read_scores()
report(scores)
