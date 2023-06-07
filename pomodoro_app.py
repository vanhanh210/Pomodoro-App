import streamlit as st
import time

st.set_page_config(page_title="Pomodoro Timer", layout="wide")

# CSS for pixel-style design
st.markdown(
    """
    <style>
    .big-clock {
        font-family: 'Courier New', monospace;
        font-size: 100px;
        text-align: center;
        padding: 20px;
        color: #000;
        background-color: #fff;
        border: 2px solid #000;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.title("Pomodoro Timer")
st.markdown(
    """
    The Pomodoro Technique is a time management method that uses a timer 
    to break work into intervals, traditionally 25 minutes in length, 
    separated by short breaks. Customize the work and break durations, 
    then click the "Start Pomodoro" button to begin!
    """
)

# Sidebars
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

tags = st.sidebar.multiselect(
    "Add tags to categorize your tasks:",
    options=["Work", "Study", "Exercise", "Meditation", "Reading", "Writing"],
)

# Main app
def pomodoro_timer(work_duration, break_duration):
    st.subheader("Work session duration: **{} minutes**".format(work_duration))
    st.subheader("Break session duration: **{} minutes**".format(break_duration))

    timer = st.empty()
    progress_bar = st.progress(0)

    st.write("Start working!")

    for i in range(work_duration * 60):
        time.sleep(1)
        minutes = int((work_duration * 60 - i) / 60)
        seconds = (work_duration * 60 - i) % 60
        timer.markdown(
            f"<p class='big-clock'>{minutes:02d}:{seconds:02d}</p>",
            unsafe_allow_html=True
        )
        progress_bar.progress(i / (work_duration * 60))

    st.write("Time for a break!")

    timer.empty()
    progress_bar.empty()
    timer = st.empty()
    progress_bar = st.progress(0)

    for i in range(break_duration * 60):
        time.sleep(1)
        minutes = int((break_duration * 60 - i) / 60)
        seconds = (break_duration * 60 - i) % 60
        timer.markdown(
            f"<p class='big-clock'>{minutes:02d}:{seconds:02d}</p>",
            unsafe_allow_html=True
        )
        progress_bar.progress(i / (break_duration * 60))

    st.write("Break is over! Start your next session or take a longer break.")

if st.button("🍅 Start Pomodoro"):
    pomodoro_timer(work_duration, break_duration)
