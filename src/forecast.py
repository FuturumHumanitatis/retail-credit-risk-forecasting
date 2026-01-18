import pandas as pd
from etl import load_data, clean_data
from features import build_features
from model import train_pd_model


LGD = 0.45  #наглядно


def run_forecast():
    df = load_data()
    df = clean_data(df)
    df = build_features(df)

    model = train_pd_model(df)

    df["pd"] = model.predict_proba(
        df[["dpd", "balance_scaled", "interest_rate"]].fillna(0)
    )[:, 1]

    df["ecl"] = df["pd"] * LGD * df["balance"]

    result = df.groupby("report_date")["ecl"].sum().reset_index()

    print("ECL forecast:")
    print(result)


if __name__ == "__main__":
    run_forecast()
