def judge_debate(memory):
    scientist_points = sum([1 for arg in memory["Scientist"] if "regulat" in arg.lower()])
    philosopher_points = sum([1 for arg in memory["Philosopher"] if "freedom" in arg.lower() or "autonomy" in arg.lower()])

    summary = f"Scientist arguments: {len(memory['Scientist'])}, Philosopher arguments: {len(memory['Philosopher'])}\n"
    summary += f"Key themes: \n- Scientist: Regulation focus\n- Philosopher: Freedom focus"

    if scientist_points >= philosopher_points:
        winner = "Scientist"
        reason = "Presented more grounded, risk-based arguments aligned with public safety principles."
    else:
        winner = "Philosopher"
        reason = "Advocated for autonomy and historical caution against overregulation."

    return summary, winner, reason
