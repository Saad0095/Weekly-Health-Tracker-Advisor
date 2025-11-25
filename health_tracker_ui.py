import streamlit as st
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
import json
import os
import copy

# -----------------------
# Constants
# -----------------------
DATA_FILE = "weekly_records.json"
DAYS = 7

# -----------------------
# Initialization
# -----------------------
if "current_week" not in st.session_state:
    st.session_state.current_week = {
        "water": [0.0] * DAYS,
        "sleep": [0.0] * DAYS,
        "workout": [0.0] * DAYS
    }

# Load records from JSON file
if "weekly_records" not in st.session_state:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            st.session_state.weekly_records = json.load(f)
    else:
        st.session_state.weekly_records = []

st.set_page_config(page_title="Weekly Health Tracker", layout="wide")
st.title("🌿 Weekly Health Tracker & Advisor")

menu = ["Enter/Update Weekly Data", "View Summary & Advice", "Compare Multiple Weeks"]
choice = st.sidebar.selectbox("Menu", menu)

# -----------------------
# Helper Functions
# -----------------------
def calculate_averages(week):
    avg_water = sum(week["water"]) / DAYS
    avg_sleep = sum(week["sleep"]) / DAYS
    avg_workout = sum(week["workout"]) / DAYS
    return avg_water, avg_sleep, avg_workout

def get_advice(avg_water, avg_sleep, avg_workout):
    advice = []
    advice.append("💧 Drink ~2L water/day." if avg_water < 2 else "💧 Water intake is good.")
    advice.append("🛌 Sleep ≥8 hrs/day." if avg_sleep < 8 else "🛌 Sleep routine is healthy.")
    advice.append("🏋️ Workout ≥30 min/day." if avg_workout < 0.5 else "🏋️ Workout routine is good.")
    return advice

def progress_bar(value, goal, label):
    pct = min(value / goal, 1.0)
    st.progress(pct)
    st.write(f"{label}: {value:.2f} / {goal}")

def create_pdf(week, avg_water, avg_sleep, avg_workout, advice):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Weekly Health Report", styles["Title"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Daily Summary", styles["Heading2"]))
    table_data = [["Day", "Water (L)", "Sleep (hrs)", "Workout (hrs)"]]
    for i in range(DAYS):
        table_data.append([
            f"Day {i+1}",
            f"{week['water'][i]:.2f}",
            f"{week['sleep'][i]:.2f}",
            f"{week['workout'][i]:.2f}"
        ])
    story.append(Table(table_data))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Averages", styles["Heading2"]))
    story.append(Paragraph(f"Water: {avg_water:.2f} L/day", styles["BodyText"]))
    story.append(Paragraph(f"Sleep: {avg_sleep:.2f} hrs/day", styles["BodyText"]))
    story.append(Paragraph(f"Workout: {avg_workout:.2f} hrs/day", styles["BodyText"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Health Advice", styles["Heading2"]))
    for line in advice:
        story.append(Paragraph(line, styles["BodyText"]))

    doc.build(story)
    buffer.seek(0)
    return buffer

def has_data(week):
    return any(v > 0 for v in week["water"] + week["sleep"] + week["workout"])

def save_week():
    """Save current week to JSON and session state using deepcopy"""
    st.session_state.weekly_records.append(copy.deepcopy(st.session_state.current_week))
    with open(DATA_FILE, "w") as f:
        json.dump(st.session_state.weekly_records, f)
    st.success(f"✅ Week saved! Total weeks: {len(st.session_state.weekly_records)}")

# -----------------------
# Enter / Update Weekly Data
# -----------------------
if choice == "Enter/Update Weekly Data":
    st.header("📝 Enter Your Weekly Data")
    for i in range(DAYS):
        st.subheader(f"Day {i+1}")
        st.session_state.current_week["water"][i] = st.number_input(
            "Water intake (L)", min_value=0.0, max_value=6.0,
            value=st.session_state.current_week["water"][i], step=0.1, key=f"water{i}"
        )
        st.session_state.current_week["sleep"][i] = st.number_input(
            "Sleep hours", min_value=0.0, max_value=24.0,
            value=st.session_state.current_week["sleep"][i], step=0.5, key=f"sleep{i}"
        )
        max_workout = 24 - st.session_state.current_week["sleep"][i]
        st.session_state.current_week["workout"][i] = st.number_input(
            f"Workout hours (max {max_workout:.1f}h)", min_value=0.0,
            max_value=float(max_workout),
            value=st.session_state.current_week["workout"][i] if st.session_state.current_week["workout"][i] <= max_workout else 0.0,
            step=0.25, key=f"workout{i}"
        )
    if st.button("💾 Save This Week"):
        save_week()

# -----------------------
# View Summary & Advice
# -----------------------
elif choice == "View Summary & Advice":
    if not st.session_state.weekly_records:
        st.warning("⚠️ No weeks recorded yet!")
    else:
        st.header("📊 Select Week to View")
        week_index = st.selectbox(
            "Choose a week", options=list(range(len(st.session_state.weekly_records))),
            format_func=lambda x: f"Week {x+1}"
        )
        week = st.session_state.weekly_records[week_index]

        # Show week data
        st.subheader(f"Week {week_index+1} Summary")
        df = pd.DataFrame({
            "Water (L/day)": week["water"],
            "Sleep (hrs/day)": week["sleep"],
            "Workout (hrs/day)": week["workout"]
        }, index=[f"Day {i+1}" for i in range(DAYS)])
        st.table(df)

        # Calculate averages and show advice
        avg_water, avg_sleep, avg_workout = calculate_averages(week)
        st.subheader("📈 Averages")
        col1, col2, col3 = st.columns(3)
        with col1: progress_bar(avg_water, 2.0, "Water")
        with col2: progress_bar(avg_sleep, 8.0, "Sleep")
        with col3: progress_bar(avg_workout, 0.5, "Workout")

        st.subheader("💡 Health Advice")
        advice = get_advice(avg_water, avg_sleep, avg_workout)
        for line in advice: st.write(line)

        st.subheader("📊 Weekly Trends")
        st.line_chart(df)

        st.subheader("📄 Export Report")
        pdf_buffer = create_pdf(week, avg_water, avg_sleep, avg_workout, advice)
        st.download_button(
            label="⬇️ Download Weekly Report (PDF)", data=pdf_buffer,
            file_name=f"Weekly_Report_Week{week_index+1}.pdf", mime="application/pdf"
        )

        if st.button("🗑️ Delete This Week"):
            if st.session_state.weekly_records:
                deleted_week = st.session_state.weekly_records.pop(week_index)
                with open(DATA_FILE, "w") as f:
                    json.dump(st.session_state.weekly_records, f)
                st.info(f"Week {week_index+1} deleted! Please reselect a week.")

# ** Compare Multiple Weeks **

elif choice == "Compare Multiple Weeks":
    if not st.session_state.weekly_records:
        st.warning("⚠️ No records to compare yet!")
    else:
        st.header("📊 Multi-Week Comparison")
        weeks = st.session_state.weekly_records
        week_labels = [f"Week {i+1}" for i in range(len(weeks))]
        days_labels = [f"Day {i+1}" for i in range(DAYS)]

        # Water chart
        water_df = pd.DataFrame({week_labels[i]: weeks[i]["water"] for i in range(len(weeks))}, index=days_labels)
        st.subheader("💧 Water Intake Comparison")
        st.line_chart(water_df)

        # Sleep chart
        sleep_df = pd.DataFrame({week_labels[i]: weeks[i]["sleep"] for i in range(len(weeks))}, index=days_labels)
        st.subheader("🛌 Sleep Hours Comparison")
        st.line_chart(sleep_df)

        # Workout chart
        workout_df = pd.DataFrame({week_labels[i]: weeks[i]["workout"] for i in range(len(weeks))}, index=days_labels)
        st.subheader("🏋️ Workout Hours Comparison")
        st.line_chart(workout_df)

        # ----------------- Total Health Score -----------------
        st.subheader("🌟 Total Health Score per Week")
        scores = []
        for week in weeks:
            week_score = 0
            for w, s, e in zip(week["water"], week["sleep"], week["workout"]):
                # Calculate score as ratio to goal (capped at 1)
                w_score = min(w / 2.0, 1.0)
                s_score = min(s / 8.0, 1.0)
                e_score = min(e / 0.5, 1.0)
                day_score = (w_score + s_score + e_score) / 3
                week_score += day_score
            week_score = (week_score / DAYS) * 100  # convert to percentage
            scores.append(round(week_score, 1))

        score_df = pd.DataFrame({"Week": week_labels, "Health Score (%)": scores}).set_index("Week")
        st.bar_chart(score_df)

        # Textual advice
        st.subheader("💡 Health Score Advice")
        for i, score in enumerate(scores):
            if score >= 90:
                text = "Excellent! 🎉 Keep it up."
            elif score >= 70:
                text = "Good. 👍 Try to improve slightly."
            elif score >= 50:
                text = "Average. ⚠️ Focus on missing areas."
            else:
                text = "Poor. ❌ Significant improvement needed."
            st.write(f"{week_labels[i]}: {score}% — {text}")
