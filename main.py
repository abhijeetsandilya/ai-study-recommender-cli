from src.model import StudyModel
from src.recommend import get_recommendation

def main():
    model = StudyModel()

    # Load and train
    X, y = model.load_data("data/dataset.csv")
    model.train(X, y)

    print("\n--- AI Study Recommender ---")

    try:
        math = int(input("Enter Math score:  "))
        physics = int(input("Enter Physics score:  "))
        dsa = int(input("Enter DSA score:  "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    prediction = model.predict(math, physics, dsa)
    recommendation = get_recommendation(prediction)

    print(f"\nPredicted Level:  {prediction.upper()}")
    print(f"Recommendation:  {recommendation}")

if __name__ == "__main__":
    main()
