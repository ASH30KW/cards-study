import streamlit as st
import pandas as pd

# Initialize or load lecture data
if 'lectures' not in st.session_state:
    st.session_state.lectures = {}  # Stores cards for each lecture

def add_card(lecture, question, answer):
    # Ensure there's a list for this lecture
    if lecture not in st.session_state.lectures:
        st.session_state.lectures[lecture] = []
    st.session_state.lectures[lecture].append({'Question': question, 'Answer': answer})

def show_cards(lecture):
    if lecture in st.session_state.lectures and st.session_state.lectures[lecture]:
        for idx, card in enumerate(st.session_state.lectures[lecture]):
            st.write(f"**{idx+1}.** Question: {card['Question']}")
            st.write(f"Answer: {card['Answer']}")
    else:
        st.write("No cards available for this lecture.")

def quiz_mode(lecture):
    if lecture in st.session_state.lectures and st.session_state.lectures[lecture]:
        for idx, card in enumerate(st.session_state.lectures[lecture]):
            st.write(f"Question {idx+1}: {card['Question']}")
            if st.button(f"Show Answer {idx+1}"):
                st.write(f"Answer: {card['Answer']}")
    else:
        st.write("No cards available for this lecture.")

# Main interface
st.title("Study Card App by Lecture")

# Sidebar for navigation
menu = ["Add Card", "View Cards", "Quiz Mode"]
choice = st.sidebar.selectbox("Menu", menu)

# Get the lecture name
st.sidebar.subheader("Select or Add a Lecture")
lecture = st.sidebar.text_input("Lecture Name")

if lecture:
    if choice == "Add Card":
        st.subheader(f"Add New Study Card for {lecture}")
        question = st.text_input("Enter the Question")
        answer = st.text_input("Enter the Answer")
        if st.button("Add Card"):
            add_card(lecture, question, answer)
            st.success(f"Card added successfully to {lecture}!")

    elif choice == "View Cards":
        st.subheader(f"Your Study Cards for {lecture}")
        show_cards(lecture)

    elif choice == "Quiz Mode":
        st.subheader(f"Quiz Mode for {lecture}")
        quiz_mode(lecture)

else:
    st.sidebar.warning("Please enter a lecture name to continue.")
