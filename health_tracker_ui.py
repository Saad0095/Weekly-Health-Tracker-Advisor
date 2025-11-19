import streamlit as st
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

# Initialization
if "water" not in st.session_state:
    st.session_state.water = [0.0] * 7
    st.session_state.sleep = [0.0] * 7
    st.session_state.workout = [0.0] * 7

st.set_page_config(page_title="Weekly Health Tracker", layout="wide")
st.title("🌿 Weekly Health Tracker & Advisor")

menu = ["Enter/Update Weekly Data", "View Summary & Advice"]
choice = st.sidebar.selectbox("Menu", menu)

# Calculate averages
def calculate_averages():
    avg_water = sum(st.session_state.water) / 7
    avg_sleep = sum(st.session_state.sleep) / 7
    avg_workout = sum(st.session_state.workout) / 7
    return avg_water, avg_sleep, avg_workout

# Generate advice 
def get_advice(avg_water, avg_sleep, avg_workout):
    advice = []
    if avg_water < 2.0:
        advice.append("💧 Try to drink around 2 liters of water daily.")
    else:
        advice.append("💧 Good job! Your water intake is on track.")

    if avg_sleep < 8.0:
        advice.append("🛌 Aim for at least 8 hours of sleep per day.")
    else:
        advice.append("🛌 Your sleep routine looks healthy.")

    if avg_workout < 0.5:
        advice.append("🏋️ Try adding around 30 minutes of daily workout.")
    else:
        advice.append("🏋️ Your workout routine looks good.")

    return advice

# Charts
def progress_bar(value, goal, label):
    pct = min(value / goal, 1.0)
    st.progress(pct)
    st.write(f"{label}: {value:.2f} / {goal}")

def has_data():
    return any(v > 0 for v in st.session_state.water +
                         st.session_state.sleep +
                         st.session_state.workout)

# PDF Report
def create_pdf(df, avg_water, avg_sleep, avg_workout, advice):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Weekly Health Report", styles["Title"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Daily Summary", styles["Heading2"]))
    table_data = [["Day", "Water (L)", "Sleep (hrs)", "Workout (hrs)"]]

    for i in range(7):
        table_data.append([
            f"Day {i+1}",
            f"{st.session_state.water[i]:.2f}",
            f"{st.session_state.sleep[i]:.2f}",
            f"{st.session_state.workout[i]:.2f}"
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


if choice == "Enter/Update Weekly Data":
    st.header("📝 Enter Your Weekly Data")

    for i in range(7):
        st.subheader(f"Day {i+1}")

        st.session_state.water[i] = st.number_input(
            "Water intake (L)",
            min_value=0.0,
            max_value=6.0,
            value=st.session_state.water[i],
            step=0.1,
            key=f"water{i}"
        )

        st.session_state.sleep[i] = st.number_input(
            "Sleep hours",
            min_value=0.0,
            max_value=24.0,
            value=st.session_state.sleep[i],
            step=0.5,
            key=f"sleep{i}"
        )

        max_workout = 24 - st.session_state.sleep[i]

        st.session_state.workout[i] = st.number_input(
            f"Workout hours (max {max_workout:.1f}h)",
            min_value=0.0,
            max_value=float(max_workout),
            value=st.session_state.workout[i]
            if st.session_state.workout[i] <= max_workout else 0.0,
            step=0.25,
            key=f"workout{i}"
        )

    st.success("✅ Weekly data updated!")


elif choice == "View Summary & Advice":

    if not has_data():
        st.warning("⚠️ No data found. Please enter your weekly data first!")
    else:
        st.header("📊 Weekly Summary")

        df = pd.DataFrame({
            "Water (L/day)": st.session_state.water,
            "Sleep (hrs/day)": st.session_state.sleep,
            "Workout (hrs/day)": st.session_state.workout
        }, index=[f"Day {i+1}" for i in range(7)])

        st.table(df)

        avg_water, avg_sleep, avg_workout = calculate_averages()

        st.subheader("📈 Averages")
        col1, col2, col3 = st.columns(3)

        with col1:
            progress_bar(avg_water, 2.0, "Water")

        with col2:
            progress_bar(avg_sleep, 8.0, "Sleep")

        with col3:
            progress_bar(avg_workout, 0.5, "Workout")

        st.subheader("💡 Health Advice")
        advice = get_advice(avg_water, avg_sleep, avg_workout)
        for line in advice:
            st.write(line)

        st.subheader("📊 Weekly Trends")
        st.line_chart(df)

        st.subheader("📄 Export Report")
        pdf_buffer = create_pdf(df, avg_water, avg_sleep, avg_workout, advice)

        st.download_button(
            label="⬇️ Download Weekly Report (PDF)",
            data=pdf_buffer,
            file_name="Weekly_Report.pdf",
            mime="application/pdf"
        )
