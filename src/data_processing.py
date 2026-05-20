def clean_data(df):
    """
    Removes null values from dataframe
    """
    return df.dropna()


def add_total_column(df):
    """
    Adds a total column by summing numeric columns
    """
    df["total"] = df.sum(axis=1)
    return df 