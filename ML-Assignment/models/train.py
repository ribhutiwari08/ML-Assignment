from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import joblib

from utils.config import RANDOM_STATE, TEST_SIZE, CV_FOLDS, MODEL_PATH


def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=RANDOM_STATE
    )

    cv_scores = cross_val_score(
        model, X_train, y_train, cv=CV_FOLDS, scoring="accuracy"
    )

    print("Cross-validation accuracy:", cv_scores.mean())

    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)

    return model, X_test, y_test
