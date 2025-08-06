import os
import pandas as pd
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    send_file,
)
from .data_utils import detect_anomalies
from .llm_engine import generate_ai_summary
from .log_utils import analyze_logs
from .log_utils import analyze_logs, login_time_distribution
import io

main = Blueprint("main", __name__)
UPLOAD_FOLDER = "data"


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".csv"):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            return redirect(url_for("main.view_data", filename=file.filename))
        else:
            flash("Only CSV files are supported.")
    return render_template("upload.html")


@main.route("/view/<filename>")
def view_data(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    df = pd.read_csv(filepath)

    # Run anomaly detection
    df = detect_anomalies(df)

    # Create prompt from flagged rows only
    flagged_df = df[df["RiskFlags"] != "None"]
    prompt = "You are a banking risk analyst AI. Summarize the following flagged transactions:\n\n"
    prompt += flagged_df[
        ["Sender", "Receiver", "Amount", "Time", "RiskFlags"]
    ].to_string(index=False)
    prompt += "\n\nGive a short summary of risks and suggest follow-up actions."

    # Generate LLM insight
    insight = generate_ai_summary(prompt)

    # Style table
    def highlight(row):
        return [
            "background-color: #f8d7da" if row["RiskFlags"] != "None" else ""
            for _ in row
        ]

    styled = df.head(100).style.apply(highlight, axis=1)
    table = styled.to_html()

    return render_template("view.html", table=table, filename=filename, insight=insight)


@main.route("/upload-log", methods=["GET", "POST"])
def upload_log():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".csv"):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            return redirect(url_for("main.view_log", filename=file.filename))
    return render_template("upload_log.html")


@main.route("/view-log/<filename>")
def view_log(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    df = pd.read_csv(filepath)
    df = analyze_logs(df)
    chart_html = login_time_distribution(df)

    # Prepare prompt for LLM summarization of flagged logs
    flagged_df = df[df["LogFlags"] != "None"]
    if not flagged_df.empty:
        prompt = (
            "You are a cybersecurity analyst AI. Analyze the following suspicious access logs:\n\n"
            + flagged_df[["Username", "IP", "Date", "Time", "LogFlags"]].to_string(
                index=False
            )
            + "\n\nProvide a brief summary of risks and recommended actions."
        )
        insight = generate_ai_summary(prompt)
    else:
        insight = "No suspicious activities detected."

    # Highlight flagged rows
    def highlight(row):
        return [
            "background-color: #fff3cd" if row["LogFlags"] != "None" else ""
            for _ in row
        ]

    styled = df.head(100).style.apply(highlight, axis=1)
    table = styled.to_html()

    return render_template(
        "view_log.html",
        table=table,
        filename=filename,
        insight=insight,
        chart=chart_html,
    )


@main.route("/export-log/<filename>")
def export_log(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    df = pd.read_csv(filepath)
    df = analyze_logs(df)

    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    return send_file(
        io.BytesIO(csv_buffer.getvalue().encode()),
        mimetype="text/csv",
        download_name=f"flagged_{filename}",
        as_attachment=True,
    )
