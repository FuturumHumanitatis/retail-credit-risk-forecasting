import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from config import RANDOM_STATE


def train_pd_model(df: pd.DataFrame):
    features = ["dpd", "balance_scaled", "interest_rate"]
    X = df[features].fillna(0)
    y = df["is_default"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=RANDOM_STATE
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    preds = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, preds)

    print(f"ROC-AUC: {auc:.3f}")
    return model
