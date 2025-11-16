import streamlit as st
import pandas as pd

if "water" not in st.session_state:
    st.session_state.water = [0.0] * 7
    st.session_state.sleep = [0.0] * 7
    st.session_state.workout = [0.0] * 7

st.set_page_config(page_title="Weekly Health Tracker", layout="wide")
st.title("🌿 Weekly Health Tracker & Advisor")

# Sidebar menu
menu = ["Enter/Update Weekly Data", "View Summary & Advice"]
choice = st.sidebar.selectbox("Menu", menu)

# Functions
def calculate_averages():
    avg_water = sum(st.session_state.water) / 7
    avg_sleep = sum(st.session_state.sleep) / 7
    avg_workout = sum(st.session_state.workout) / 7
    return avg_water, avg_sleep, avg_workout

def get_advice(avg_water, avg_sleep, avg_workout):
    advice = []
    if avg_water < 2.0:
        advice.append("💧 Increase daily water intake to ~2 liters/day.")
    else:
        advice.append("💧 Water intake is good!")

    if avg_sleep < 8.0:
        advice.append("🛌 Try to get at least 8 hours of sleep daily.")
    else:
        advice.append("🛌 Sleep hours are sufficient!")

    if avg_workout < 0.5:
        advice.append("🏋️ Increase workout to at least 30 minutes/day.")
    else:
        advice.append("🏋️ Workout routine is good!")
    return advice

def progress_bar(value, goal, label):
    pct = min(value / goal, 1.0)  
    if pct < 0.5:
        color = "🔴"
    elif pct < 1.0:
        color = "🟡"
    else:
        color = "🟢"
    st.progress(pct)
    st.write(f"{label}: {value:.2f} / {goal} {color}")

def has_data():
    return any(v > 0 for v in st.session_state.water + st.session_state.sleep + st.session_state.workout)

# Option 1: Enter/Update Data
if choice == "Enter/Update Weekly Data":
    st.header("📝 Enter Your Weekly Data")
    for i in range(7):
        st.subheader(f"Day {i+1}")
        st.session_state.water[i] = st.number_input(
            f"Water intake (L)", min_value=0.0, value=st.session_state.water[i], step=0.1, key=f"water{i}"
        )
        st.session_state.sleep[i] = st.number_input(
            f"Sleep hours", min_value=0.0, max_value=24.0, value=st.session_state.sleep[i], step=0.5, key=f"sleep{i}"
        )
        st.session_state.workout[i] = st.number_input(
            f"Workout hours", min_value=0.0, max_value=24.0, value=st.session_state.workout[i], step=0.25, key=f"workout{i}"
        )
    st.success("✅ Weekly data updated!")

# Option 2: View Summary & Advice
elif choice == "View Summary & Advice":
    if not has_data():
        st.warning("⚠️ No data found. Please enter your weekly data first!")
    else:
        st.header("📊 Weekly Summary")
        data = {
            "Water (L/day)": st.session_state.water,
            "Sleep (hrs/day)": st.session_state.sleep,
            "Workout (hrs/day)": st.session_state.workout
        }
        df = pd.DataFrame(data, index=[f"Day {i+1}" for i in range(7)])
        st.table(df)

        # Calculate averages
        avg_water, avg_sleep, avg_workout = calculate_averages()
        st.subheader("📈 Averages")
        col1, col2, col3 = st.columns(3)
        with col1:
            progress_bar(avg_water, 2.0, "Water")
        with col2:
            progress_bar(avg_sleep, 8.0, "Sleep")
        with col3:
            progress_bar(avg_workout, 0.5, "Workout")

        # Display advice
        st.subheader("💡 Health Advice")
        advice = get_advice(avg_water, avg_sleep, avg_workout)
        for a in advice:
            st.write(a)

        # Weekly trends chart
        st.subheader("📊 Weekly Trends")
        st.line_chart(df)
        