def get_recommendation(label):
    if label == "weak":
        return "Focus heavily: Study 2-3 hours/day, revise basics, solve easy problems"
    elif label == "medium":
        return "Practice regularly: 1-2 hours/day, focus on problem solving"
    elif label == "strong":
        return "Maintain level: Revise and solve advanced problems"
    else:
        return "Invalid prediction"
