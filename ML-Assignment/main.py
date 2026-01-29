from data.load_data import load_dataset
from features.feature_engineering import add_features
from models.train import train_model
from models.evaluate import evaluate_model


def main():
    X, y = load_dataset()
    X = add_features(X)

    model, X_test, y_test = train_model(X, y)
    evaluate_model(model, X_test, y_test)


if __name__ == "__main__":
    main()
