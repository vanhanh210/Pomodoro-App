import streamlit as st
import time

# Custom CSS
def custom_css():
    st.markdown(
        """
        <style>
            .theme-switch { display: flex; justify-content: center; align-items: center; }
            button { margin: 5px; }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Toggle Dark/Light Mode
def toggle_mode():
    if st.session_state.theme == "dark":
        st.write("🌙 Dark Mode")
    else:
        st.write("☀️ Light Mode")

@st.cache
def load_theme():
    return "light"

st.set_page_config(page_title="Pomodoro Timer", layout="wide")
custom_css()

if "theme" not in st.session_state:
    st.session_state.theme = load_theme()

if st.sidebar.button("Toggle Theme"):
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

toggle_mode()

st.title("Pomodoro Timer")

work_duration = st.sidebar.number_input(
    "Work session duration (minutes):",
    min_value=1,
    max_value=90,
    value=25,
    step=1,
)
break_duration = st.sidebar.number_input(
    "Break session duration (minutes):",
    min_value=1,
    max_value=30,
    value=5,
    step=1,
)

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    st.subheader("Tags")
    tags = st.multiselect(
        "Add tags to categorize your tasks:",
        options=["Work", "Study", "Exercise", "Meditation", "Reading", "Writing"],
    )

def pomodoro_timer(work_duration, break_duration):
    st.write("Work session duration: **{} minutes**".format(work_duration))
    st.write("Break session duration: **{} minutes**".format(break_duration))

    timer = st.empty()
    progress_bar = st.progress(0)

    st.write("Start working!")
    for i in range(work_duration * 60):
        time.sleep(1)
        timer.markdown(f"**{int((work_duration * 60 - i) / 60)}:{(work_duration * 60 - i) % 60:02d}**")
        progress_bar.progress(i / (work_duration * 60))
    st.write("Time for a break!")

    timer.empty()
    progress_bar.empty()
    timer = st.empty()
    progress_bar = st.progress(0)

    for i in range(break_duration * 60):
        time.sleep(1)
        timer.markdown(f"**{int((break_duration * 60 - i) / 60)}:{(break_duration * 60 - i) % 60:02d}**")
        progress_bar.progress(i / (break_duration * 60))
    st.write("Break is over! Start your next session or take a longer break.")

if st.button("🍅 Start Pomodoro"):
    pomodoro_timer(work_duration, break_duration)