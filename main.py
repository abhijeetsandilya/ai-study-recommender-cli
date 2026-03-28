from src.model import StudyModel
from src.recommend import get_recommendation
import pandas as pd

def main():
    model = StudyModel()

    # Load and train
    X, y = model.load_data("data/dataset.csv")
    model.train(X, y)

    print("\n--- AI Study Recommender ---")

    try:
        math = float(input("Enter Math score:  "))
        physics = float(input("Enter Physics score:  "))
        dsa = float(input("Enter DSA score:  "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return
    input_data = pd.DataFrame([[math, physics, dsa]],
                          columns=["math", "physics", "dsa"])
    prediction = model.predict(input_data)
    recommendation = get_recommendation(prediction)

    print(f"\nPredicted Level:  {prediction.upper()}")
    print(f"Recommendation:  {recommendation}")

if __name__ == "__main__":
    main()
