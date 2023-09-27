from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Observer Class
class ModelObserver:
    def update(self, message):
        raise NotImplementedError


# Concrete Observer
class AccuracyObserver(ModelObserver):
    def update(self, message):
        print(f"AccuracyObserver received message: {message}")


# Subject Class
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


# Concrete Subject
class ObservableModel(Subject):
    def __init__(self):
        super().__init__()
        self.model = RandomForestClassifier()
        self.data = load_iris()
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.data.data, self.data.target, test_size=0.2, random_state=42
        )

    def train_and_evaluate(self):
        self.model.fit(self.X_train, self.y_train)
        self.notify("Training complete.")

        y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        self.notify(f"Evaluation complete. Accuracy: {accuracy}")


# Client code
observer = AccuracyObserver()
model = ObservableModel()
model.add_observer(observer)

model.train_and_evaluate()
