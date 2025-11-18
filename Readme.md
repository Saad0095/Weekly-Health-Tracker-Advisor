# Weekly Health Tracker & Advisor

**NED University of Engineering & Technology, Karachi**

---

## Course Information

- **Department:** Computer Science & Information Technology
- **Course:** CT-175 Programming Fundamentals
- **Project Type:** Complex Computing Problem (CCP) Report
- **Submitted To:** Miss Amna

---

## Team Members

| Name | Roll Number | Role |
|------|-------------|------|
| Muhammad Saad Bin Khalid | CT-25245 | Group Lead, Project Planning, UI & Documentation |
| Abdullah Bin Waqar | CT-25246 | Coding and Testing |
| Hassaan Ahmed Khan | CT-25248 | Coding and Upgradation |
| Muhammad Shiblee Shamim | CT-25233 | Module Coding and Documentation |
| Mujeeb-Ur-Rehman | CT-24200 | Module Coding |

---

## Problem Statement

The user is committed to tracking their overall health and wellness. To accomplish this, they want to track their core daily habits such as:
- Weekly water intake
- Sleep duration
- Workout time

By monitoring these habits, users intend to seek personalized, specialist-like advice and insights for their health improvement.

---

## Introduction & Scope

The **Weekly Health Tracker & Advisor** is an interactive console-based and web-based application designed to help students track their weekly health. The program collects input on daily water intake, sleep hours, and workout hours from the user, calculates averages, and provides advice based on their report.

### Core Programming Principles

Our project revolves around fundamental programming concepts:
- **Arrays:** Store daily data for each metric
- **Loops:** Iterate through days of the week
- **Functions:** Modular design for input, calculation, and output
- **Pointers:** Pass data between functions efficiently
- **Conditional Statements:** Provide logic for validation and advice

The project's modular design, along with core logical reasoning and structured programming, enhances overall efficiency.

### Scope

- Record daily water intake, sleep, and workout for a week
- Calculate weekly averages and provide health advice
- Display summary in console and UI using charts via Streamlit
- Give personalized advice based on tracking data

---

## How This Health Tracker Works

This application has two main parts that work together:

### 1. C Program - The Calculation Engine

The C program handles all the data processing using organized functions:

- **main()** - Starts the program and sets up data storage
- **mainMenu()** - Shows the main options in a continuous loop:
  - Option 1: Enter your daily health data
  - Option 2: View your weekly summary and get advice
  - Option 3: Exit the program
- **inputData()** - Collects your daily water intake, sleep hours, and workout time for 7 days with basic validation (no negative numbers, reasonable time ranges)
- **calculateAverages()** - Calculates weekly averages using pointers to efficiently return multiple values
- **displaySummary()** - Puts together a neat table so you can see your daily numbers and the weekly averages all in one place
- **getAdvice()** - Gives you simple tips by checking if your averages hit the healthy targets, like drinking enough water or getting sufficient sleep

### 2. Streamlit Web Interface - The Visual Dashboard

The web app enhances the experience with modern features:

- **Session State** - Remembers your data as you navigate between pages
- **Sidebar Navigation** - Easy menu access similar to the C program
- **Smart Input Forms** - Uses number inputs with built-in limits for easier data entry
- **Enhanced Display:**
  - Pandas Tables - Shows your data in professional, organized tables
  - Interactive Charts - Uses Plotly to create bar charts with color coding:
    - Green = Meeting goals
    - Orange = Getting close
    - Red = Needs improvement
  - Same Smart Advice - Provides the same personalized recommendations as the C version

**The Partnership:** The C program provides the reliable calculation core, while the Streamlit interface delivers a modern, visual experience that makes tracking your health data intuitive and engaging.

---

## Features

✅ **Console Application (C):**
- Main menu-driven interface
- Input validation for all metrics
- Weekly summary display
- Personalized health advice

✅ **Web UI (Streamlit/Python):**
- Interactive data entry interface
- Real-time session state management
- Visual progress bars
- Weekly trend charts
- Clean, user-friendly design

---

## Technologies Used

| Component | Technology |
|-----------|-----------|
| Backend (Core Logic) | C Programming |
| Frontend (Web UI) | Python with Streamlit |
| Data Handling | Arrays, Session State |
| Visualization | Charts, Progress Bars, Tables |

---

## Installation & Usage

### C Program (Console)

```bash
gcc main.c -o health_tracker
./health_tracker
```

**Menu Options:**
1. Enter/Update Weekly Data
2. View Summary & Advice
3. Exit Program

### Streamlit UI (Web Interface)

```bash
pip install streamlit pandas
streamlit run health_tracker_ui.py
```

**Live Demo:** https://healthtrackerui.streamlit.app/

---

## Input Validation

- **Water Intake:** 0-6 liters per day
- **Sleep Hours:** 0-24 hours per day
- **Workout Hours:** 0 to (24 - sleep hours) per day

---

## Health Advice Logic

### Water Intake
- ✅ **< 2.0 L/day:** Increase daily water intake to around 2 liters
- ✅ **≥ 2.0 L/day:** Water intake is good!

### Sleep Hours
- ✅ **< 8.0 hrs/day:** Try to get at least 8 hours of sleep daily
- ✅ **≥ 8.0 hrs/day:** Sleep hours are sufficient!

### Workout Time
- ✅ **< 0.5 hrs/day:** Increase workout time to at least 30 minutes
- ✅ **≥ 0.5 hrs/day:** Workout routine is good!

---

## Sample Output

### Console Application
The C program displays a menu-driven interface with formatted tables showing daily metrics and calculated averages.

### Web Interface
The Streamlit UI provides an interactive experience with:
- Input fields for all 7 days
- Real-time data visualization
- Progress bars showing goal achievement
- Trend charts for weekly analysis

**Live Demo:** https://healthtrackerui.streamlit.app/

---

## Future Enhancements

- 🔐 Multi-user support with personalized user accounts
- 🎮 BGMI tracking as an additional feature
- 💾 File storage to save weekly logs
- 📈 Multi-week health progress tracking
- 📄 Export weekly reports as PDF
- 🧮 Advanced calculations (sleep score, health rating scale based on age/gender)
- 📊 Statistical analysis and trend prediction

---

## Limitations

- ❌ No long-term memory or history tracking
- ❌ Does not perform advanced calculations (sleep score, health rating scale)
- ❌ Age and gender factors not considered in advice generation
- ❌ Single-week tracking only (no multi-week comparison)

---

## Project Structure

```
Weekly-Health-Tracker-Advisor/
├── main.c                    # C console application
├── health_tracker_ui.py      # Streamlit web application
└── README.md                 # Project documentation
```

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Saad0095/Weekly-Health-Tracker-Advisor.git
   cd Weekly-Health-Tracker-Advisor
   ```

2. For C program:
   ```bash
   gcc main.c -o health_tracker
   ./health_tracker
   ```

3. For Streamlit UI:
   ```bash
   pip install streamlit pandas
   streamlit run health_tracker_ui.py
   ```

---

## License

This project is created as part of the CT-175 Programming Fundamentals course at NED University of Engineering & Technology.

---

## Contact & Support

For questions or suggestions, please contact the project team through GitHub issues or reach out to the group lead: **Muhammad Saad Bin Khalid**

---

**Project Completed:** November 2025  
**Repository:** https://github.com/Saad0095/Weekly-Health-Tracker-Advisor
