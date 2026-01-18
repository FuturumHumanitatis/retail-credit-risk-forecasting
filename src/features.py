import polars as pl


def build_features(df):
    pl_df = pl.from_pandas(df)

    pl_df = pl_df.with_columns([
        pl.col("dpd").rolling_mean(2).alias("dpd_roll_2m"),
        (pl.col("balance") / 100000).alias("balance_scaled")
    ])

    return pl_df.to_pandas()
