import pandas as pd


def detect_anomalies(df):
    df["RiskFlags"] = ""

    # Rule 1: High amount
    df.loc[df["Amount"] > 10000, "RiskFlags"] += "HighAmount; "

    # Rule 2: Late night transactions
    def is_late(time_str):
        hour = int(time_str.split(":")[0])
        return 0 <= hour < 5

    df.loc[df["Time"].apply(is_late), "RiskFlags"] += "LateNight; "

    # Rule 3: Frequent sender (appears more than X times)
    frequent_senders = df["Sender"].value_counts()
    frequent_senders = frequent_senders[frequent_senders > 3].index.tolist()
    df.loc[df["Sender"].isin(frequent_senders), "RiskFlags"] += "FrequentSender; "

    # Rule 4: Same sender and receiver
    df.loc[df["Sender"] == df["Receiver"], "RiskFlags"] += "SelfTransfer; "

    # Clean empty flags
    df["RiskFlags"] = df["RiskFlags"].replace("", "None")
    return df
