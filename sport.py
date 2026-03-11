import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Sports Dashboard", layout="wide")

st.title("🏆 Student Sports Management System")

# Games list
games_list = ["Cricket", "Football", "Badminton", "Basketball", "Volleyball", "Kabaddi", "Chess"]

# Store students data
if "students" not in st.session_state:
    st.session_state.students = []

st.header("➕ Add Student")

name = st.text_input("Enter Student Name")

games = st.multiselect(
    "Select Games Student Can Play",
    games_list
)

if st.button("Add Student"):
    if name and games:
        st.session_state.students.append({
            "Name": name,
            "Games": ", ".join(games)
        })
        st.success("Student added successfully ✅")
    else:
        st.warning("Enter name and select games")

st.divider()

st.header("📋 Students List")

if st.session_state.students:
    df = pd.DataFrame(st.session_state.students)
    st.dataframe(df)
else:
    st.info("No students added yet")

st.divider()

st.header("📊 Games Summary")

if st.session_state.students:

    game_count = {}

    for student in st.session_state.students:
        student_games = student["Games"].split(", ")
        for g in student_games:
            if g in game_count:
                game_count[g] += 1
            else:
                game_count[g] = 1

    summary = pd.DataFrame({
        "Game": game_count.keys(),
        "Number of Students": game_count.values()
    })

    st.bar_chart(summary.set_index("Game"))
    st.table(summary)

else:
    st.info("Add students to see summary")