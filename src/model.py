import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class StudyModel:
  def __init__(self):
    self.model = DecisionTreeClassifier()

  def load_data(self, path):
    data = pd.read_csv(path)
    X = data[['math', 'physics', 'dsa']]
    y = data['label']
    return X, y

  def train(self, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    self.model.fit(X_train, y_train)
    y_pred = self.model.predict(X_test)
    print("\nModel Evaluation:")
    print(classification_report(y_test, y_pred))

  def predict(self, input_data):
    return self.model.predict(input_data)[0]
