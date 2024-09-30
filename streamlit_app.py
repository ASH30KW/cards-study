import streamlit as st
import pandas as pd

# Initialize or load card data
if 'cards' not in st.session_state:
    st.session_state.cards = []

def add_card(question, answer):
    st.session_state.cards.append({'Question': question, 'Answer': answer})

def show_cards():
    if st.session_state.cards:
        for idx, card in enumerate(st.session_state.cards):
            st.write(f"**{idx+1}.** Question: {card['Question']}")
            st.write(f"Answer: {card['Answer']}")
    else:
        st.write("No cards available.")

def quiz_mode():
    if st.session_state.cards:
        for idx, card in enumerate(st.session_state.cards):
            st.write(f"Question {idx+1}: {card['Question']}")
            if st.button(f"Show Answer {idx+1}"):
                st.write(f"Answer: {card['Answer']}")
    else:
        st.write("No cards available.")

# Main interface
st.title("Study Card App")

# Sidebar for navigation
menu = ["Add Card", "View Cards", "Quiz Mode"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Card":
    st.subheader("Add New Study Card")
    question = st.text_input("Enter the Question")
    answer = st.text_input("Enter the Answer")
    if st.button("Add Card"):
        add_card(question, answer)
        st.success("Card added successfully!")

elif choice == "View Cards":
    st.subheader("Your Study Cards")
    show_cards()

elif choice == "Quiz Mode":
    st.subheader("Quiz Mode")
    quiz_mode()
