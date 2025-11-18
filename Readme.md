# Weekly Health Tracker & Advisor

**NED University of Engineering & Technology, Karachi**

---

## Course Information

- **Department:** Computer Science & Information Technology
- **Course:** CT-175 Programming Fundamentals
- **Project Type:** Complex Computing Problem (CCP) Report
- **Submitted To:** Miss Amna
- **Repository:** [GitHub](https://github.com/Saad0095/Weekly-Health-Tracker-Advisor)

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

## Algorithm

**Start**

1. **Initialize Arrays and Constants:**
   - Define constant `DAYS = 7` (for a week)
   - Declare arrays:
     - `water[DAYS]` stores daily water intake
     - `sleep[DAYS]` stores daily sleep hours
     - `workout[DAYS]` stores daily workout hours

2. **Call Main Menu Function:**
   - Pass water, sleep, and workout arrays to `mainMenu()`

**Main Menu Function:**

3. **Display Menu Options:**
   - Option 1: Enter/Update Weekly Data
   - Option 2: View Summary & Advice
   - Option 3: Exit Program

4. **Input User Choice** (choice)

5. **Decision Based on Choice:**
   - **If choice = 1:**
     - Call `inputData()` to take daily inputs
     - Call `calculateAverages()` to compute weekly averages
     - Display confirmation message: "Data input completed"
   - **If choice = 2:**
     - Check if data exists
     - If averages are 0, prompt user to enter data first
     - Else:
       - Call `displaySummary()` to show daily and average data
       - Call `getAdvice()` to provide health recommendations
   - **If choice = 3:**
     - Exit program with message "Program Exited successfully"
   - **Else:**
     - Display "Invalid choice" and prompt again

6. **Repeat Menu** until user chooses option 3

**Input Data Function (inputData):**

7. **For Each Day (1 to 7):**
   - **Water Intake:**
     - Input water in liters
     - Validate: 0 ≤ water ≤ 6
     - If invalid, prompt again
   - **Sleep Hours:**
     - Input sleep hours
     - Validate: 0 ≤ sleep ≤ 24
     - If invalid, prompt again
   - **Workout Hours:**
     - Input workout hours
     - Validate: 0 ≤ workout ≤ (24 - sleep)
     - If invalid, prompt again

**Calculate Averages Function (calculateAverages):**

8. **For Each Day (1 to 7):**
   - Sum up water, sleep, and workout arrays

9. **Compute Weekly Average:**
   - `avgWater = totalWater / DAYS`
   - `avgSleep = totalSleep / DAYS`
   - `avgWorkout = totalWorkout / DAYS`

**Display Summary Function:**

10. **Print Table:**
    - Day | Water (L/day) | Sleep (hrs/day) | Workout (hrs/day)

11. **For Each Day:**
    - Print values of `water[i]`, `sleep[i]`, `workout[i]`

12. **Print Weekly Averages:**
    - `avgWater`, `avgSleep`, `avgWorkout`

**Get Advice Function (getAdvice):**

13. **Compare Averages and Provide Suggestions:**
    - **Water:**
      - If `avgWater < 2.0`, suggest increasing water intake
      - Else, print "Water intake is good!"
    - **Sleep:**
      - If `avgSleep < 8.0`, suggest more sleep
      - Else, print "Sleep hours sufficient!"
    - **Workout:**
      - If `avgWorkout < 0.5`, suggest increasing workout
      - Else, print "Workout routine is good!"

**End**

---

## How This Health Tracker Works

The app has two main parts:

### 1. C Program (The Brain)
- Handles all the calculations
- Stores your daily health data
- Gives basic health advice
- Works like a simple menu system

### 2. Streamlit Web App (The Display)
- Shows your data in pretty tables and graphs
- Lets you input data easily with sliders and buttons
- Makes it easy to see your weekly patterns at a glance

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
