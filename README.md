# ai-study-recommender-cli
A simple command-line based machine learning project that predicts a student’s performance level based on subject scores and provides study recommendations.

## Overview

This project uses a Decision Tree Classifier to analyze scores in:

Mathematics
Physics
Data Structures & Algorithms (DSA)

Based on the input, it classifies the student into one of three levels:

### Weak
### Medium
### Strong

It then provides a corresponding recommendation to help improve or maintain performance.

## Features
CLI-based interaction (lightweight and fast)
Machine learning model using scikit-learn
Supports floating-point inputs (e.g., 82.5)
Structured codebase (separation of model, logic, and interface)
Basic evaluation using train-test split
## Project Structure
ai-study-recommender-cli/
│
├── data/
│   └── dataset.csv
│
├── src/
│   ├── model.py
│   └── recommend.py
│
├── main.py
└── README.md
## How It Works
Dataset is loaded from data/dataset.csv
A Decision Tree model is trained using the data
User inputs scores via CLI
Model predicts performance level
Recommendation is generated based on prediction
## Installation & Setup
### 1. Clone the repository
git clone https://github.com/abhijeetsandilya/ai-study-recommender-cli.git
cd ai-study-recommender-cli
### 2. Create a virtual environment (recommended)
python -m venv .venv

Activate it:

Windows:
.venv\Scripts\activate
macOS/Linux:
source .venv/bin/activate
### 3. Install dependencies
pip install pandas scikit-learn
## Running the Project
python main.py
## Example Run
--- AI Study Recommender ---

Enter Math score: 82.5
Enter Physics score: 78
Enter DSA score: 65

Predicted Level: MEDIUM
Recommendation: Focus on improving weak areas and practice consistently
## Dataset

The dataset is a small manually created CSV file with the following format:

math,physics,dsa,label
45,70,30,weak
80,85,78,strong
...

Note: Due to the small dataset size, the model may overfit and show high accuracy.

## Limitations
Very small dataset (not representative of real-world data)
Model may overfit (accuracy can be misleading)
Recommendation system is rule-based, not learned
No model persistence (retraining happens on every run)
## Future Improvements
Increase dataset size (100+ samples)
Save and load trained model using joblib
Add input validation and error handling
Improve recommendation logic based on individual subject weaknesses
Add web interface (FastAPI or frontend)
## Tech Stack
Python
pandas
scikit-learn
## Author

Abhijeet Sandilya
