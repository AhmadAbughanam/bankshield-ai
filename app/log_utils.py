import pandas as pd
import plotly.express as px


def analyze_logs(df):
    df["LogFlags"] = ""

    # Convert to datetime
    df["Datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"])

    # Rule 1: Off-hours (00:00 – 06:00)
    df["Hour"] = df["Datetime"].dt.hour
    df.loc[(df["Hour"] >= 0) & (df["Hour"] < 6), "LogFlags"] += "OffHours; "

    # Rule 2: Foreign/unknown IPs (mocked here)
    blacklisted_ips = ["203.0.113.5", "185.66.10.1"]
    df.loc[df["IP"].isin(blacklisted_ips), "LogFlags"] += "BlacklistedIP; "

    # Rule 3: Repeated login attempts per user (mocked pattern)
    freq_users = df["Username"].value_counts()
    suspicious = freq_users[freq_users > 5].index.tolist()
    df.loc[df["Username"].isin(suspicious), "LogFlags"] += "BruteForceSuspect; "

    # Clean empty flags
    df["LogFlags"] = df["LogFlags"].replace("", "None")
    return df


def login_time_distribution(df):
    df["Hour"] = pd.to_datetime(df["Time"], format="%H:%M").dt.hour
    fig = px.histogram(
        df,
        x="Hour",
        nbins=24,
        title="Login Attempts by Hour",
        labels={"Hour": "Hour of Day"},
        template="plotly_white",
    )
    return fig.to_html(full_html=False)
