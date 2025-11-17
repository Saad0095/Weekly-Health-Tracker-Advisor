import streamlit as st
import pandas as pd

# Initialization
if "water" not in st.session_state:
    st.session_state.water = [0.0] * 7
    st.session_state.sleep = [0.0] * 7
    st.session_state.workout = [0.0] * 7

st.set_page_config(page_title="Weekly Health Tracker", layout="wide")
st.title("🌿 Weekly Health Tracker & Advisor")

menu = ["Enter/Update Weekly Data", "View Summary & Advice"]
choice = st.sidebar.selectbox("Menu", menu)

# calculates averages 
def calculate_averages():
    avg_water = sum(st.session_state.water) / 7
    avg_sleep = sum(st.session_state.sleep) / 7
    avg_workout = sum(st.session_state.workout) / 7
    return avg_water, avg_sleep, avg_workout

# generates advice
def get_advice(avg_water, avg_sleep, avg_workout):
    advice = []

    if avg_water < 2.0:
        advice.append("💧 try to drink around 2 liters of water daily.")
    else:
        advice.append("💧 good job! your water intake is on track.")

    if avg_sleep < 8.0:
        advice.append("🛌 aim for at least 8 hours of sleep per day.")
    else:
        advice.append("🛌 your sleep routine looks healthy.")

    if avg_workout < 0.5:
        advice.append("🏋️ try adding around 30 minutes of daily workout.")
    else:
        advice.append("🏋️ your workout routine looks good.")

    return advice

# Chart/Graphs
def progress_bar(value, goal, label):
    pct = min(value / goal, 1.0)
    st.progress(pct)
    st.write(f"{label}: {value:.2f} / {goal}")

# input validation
def has_data():
    return any(v > 0 for v in st.session_state.water + st.session_state.sleep + st.session_state.workout)


# ** UI **

if choice == "Enter/Update Weekly Data":

    st.header("📝 Enter Your Weekly Data")

    for i in range(7):
        st.subheader(f"Day {i+1}")

        water = st.number_input(
            "Water intake (L)",
            min_value=0.0,
            max_value=6.0,
            value=st.session_state.water[i],
            step=0.1,
            key=f"water{i}"
        )
        st.session_state.water[i] = water

        sleep = st.number_input(
            "Sleep hours",
            min_value=0.0,
            max_value=24.0,
            value=st.session_state.sleep[i],
            step=0.5,
            key=f"sleep{i}"
        )
        st.session_state.sleep[i] = sleep

        max_workout = 24 - sleep

        workout = st.number_input(
            f"Workout hours (max {max_workout:.1f}h)",
            min_value=0.0,
            max_value=float(max_workout),
            value=st.session_state.workout[i]
            if st.session_state.workout[i] <= max_workout else 0.0,
            step=0.25,
            key=f"workout{i}"
        )
        st.session_state.workout[i] = workout

    st.success("✅ weekly data updated!")


elif choice == "View Summary & Advice":

    if not has_data():
        st.warning("⚠️ no data found. please enter your weekly data first!")
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
        for line in get_advice(avg_water, avg_sleep, avg_workout):
            st.write(line)

        st.subheader("📊 Weekly Trends")
        st.line_chart(df)
