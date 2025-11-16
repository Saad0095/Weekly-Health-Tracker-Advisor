import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ----------------------------
# 1️⃣ Page Config and Background
# ----------------------------
st.set_page_config(page_title="🌿 Weekly Health Tracker", layout="wide")

# Background image & custom container style
st.markdown(
    """
    <style>
    /* Full-page background image */
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Semi-transparent container for content readability */
    .container {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
    }

    /* Headings style */
    h1, h2, h3, h4 {
        color: #0B3D91;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# 2️⃣ Initialize Session State
# ----------------------------
if "water" not in st.session_state:
    st.session_state.water = [0.0] * 7
    st.session_state.sleep = [0.0] * 7
    st.session_state.workout = [0.0] * 7

# ----------------------------
# 3️⃣ Sidebar Menu
# ----------------------------
menu = ["Enter/Update Weekly Data", "View Summary & Advice"]
choice = st.sidebar.selectbox("Menu", menu)

# ----------------------------
# 4️⃣ Helper Functions
# ----------------------------
def calculate_averages():
    avg_water = sum(st.session_state.water) / 7
    avg_sleep = sum(st.session_state.sleep) / 7
    avg_workout = sum(st.session_state.workout) / 7
    return avg_water, avg_sleep, avg_workout

def get_advice(avg_water, avg_sleep, avg_workout):
    advice = []
    advice.append("💧 " + ("Water intake is good!" if avg_water >= 2.0 else "Increase daily water intake to ~2 liters/day."))
    advice.append("🛌 " + ("Sleep hours are sufficient!" if avg_sleep >= 8.0 else "Try to get at least 8 hours of sleep daily."))
    advice.append("🏋️ " + ("Workout routine is good!" if avg_workout >= 0.5 else "Increase workout to at least 30 minutes/day."))
    return advice

def has_data():
    return any(v > 0 for v in st.session_state.water + st.session_state.sleep + st.session_state.workout)

def get_color(value, goal):
    if value < 0.5 * goal:
        return "red"
    elif value < goal:
        return "orange"
    else:
        return "green"

# ----------------------------
# 5️⃣ Main Container Start
# ----------------------------
st.markdown('<div class="container">', unsafe_allow_html=True)
st.title("🌿 Weekly Health Tracker & Dashboard")

# ----------------------------
# 6️⃣ Option 1: Enter/Update Data
# ----------------------------
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

# ----------------------------
# 7️⃣ Option 2: View Summary & Advice
# ----------------------------
elif choice == "View Summary & Advice":
    if not has_data():
        st.warning("⚠️ No data found. Please enter your weekly data first!")
    else:
        st.header("📊 Weekly Summary Table")
        # Table
        data = {
            "Water (L/day)": st.session_state.water,
            "Sleep (hrs/day)": st.session_state.sleep,
            "Workout (hrs/day)": st.session_state.workout
        }
        df = pd.DataFrame(data, index=[f"Day {i+1}" for i in range(7)])
        st.table(df)

        # Averages
        avg_water, avg_sleep, avg_workout = calculate_averages()
        st.subheader("📈 Averages")
        st.write(f"💧 Water: {avg_water:.2f} L/day | 🛌 Sleep: {avg_sleep:.2f} hrs/day | 🏋️ Workout: {avg_workout:.2f} hrs/day")

        # Advice
        st.subheader("💡 Health Advice")
        advice = get_advice(avg_water, avg_sleep, avg_workout)
        for a in advice:
            st.write(a)

        # Dashboard: Day-by-Day Bar Chart
        st.subheader("📊 Daily Performance Dashboard")
        fig = go.Figure()
        days = [f"Day {i+1}" for i in range(7)]

        fig.add_trace(go.Bar(
            x=days,
            y=st.session_state.water,
            name='Water (L)',
            marker_color=[get_color(v, 2.0) for v in st.session_state.water],
            text=[f"{v:.1f} L" for v in st.session_state.water],
            textposition='auto'
        ))

        fig.add_trace(go.Bar(
            x=days,
            y=st.session_state.sleep,
            name='Sleep (hrs)',
            marker_color=[get_color(v, 8.0) for v in st.session_state.sleep],
            text=[f"{v:.1f} h" for v in st.session_state.sleep],
            textposition='auto'
        ))

        fig.add_trace(go.Bar(
            x=days,
            y=st.session_state.workout,
            name='Workout (hrs)',
            marker_color=[get_color(v, 0.5) for v in st.session_state.workout],
            text=[f"{v:.2f} h" for v in st.session_state.workout],
            textposition='auto'
        ))

        fig.update_layout(
            barmode='group',
            title="Daily Performance vs Goals",
            yaxis_title="Hours / Liters",
            xaxis_title="Days",
            legend_title="Metrics",
            height=500,
            plot_bgcolor='rgba(0,0,0,0)',  # transparent background
            paper_bgcolor='rgba(0,0,0,0)'  # transparent container
        )

        st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# 8️⃣ Close container
# ----------------------------
st.markdown('</div>', unsafe_allow_html=True)
