import pandas as pd
from config import DATA_PATH


def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH, parse_dates=["report_date"])
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["balance"] >= 0]
    df["is_npl"] = (df["dpd"] > 90).astype(int)
    return df


if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)
    print(df.head())
