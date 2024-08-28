import streamlit as st

# Function to handle user input change
def on_input_change():
    if st.session_state.user_input:
        # Add the user's response to the session state
        st.session_state.responses.append(st.session_state.user_input)
        # Clear the input field after submission
        st.session_state.user_input = ''
        # Move to the next question by popping the first one
        if st.session_state.questions:
            st.session_state.questions.pop(0)

# Function to clear the chat 
def on_btn_click():
    # Reset questions and responses
    st.session_state.questions = ['What is your Budget', 
                                  'Briefly explain the locality you would love to live in.', 
                                  'What all facilities are you looking for']
    st.session_state.responses = []

# Initialize session state 
if 'questions' not in st.session_state:
    st.session_state.questions = ['What is your Budget', 
                                  'Briefly explain the locality you would love to live in.', 
                                  'What all facilities are you looking for']
if 'responses' not in st.session_state:
    st.session_state.responses = []

st.title("Atlantic WayFinder's QA")
st.button("Clear messages", on_click=on_btn_click)

# Chat logic to display the current question and clear after submission
if st.session_state.questions:
    # Display the current question
    st.write(f"**WayFinder Assistant**: {st.session_state.questions[0]}")  
    
    st.text_input("Your response:", on_change=on_input_change, key="user_input")
    
    # Clear previous user response after displaying next question
    if st.session_state.responses and len(st.session_state.responses) == len(st.session_state.questions) + 1:
        st.session_state.responses = []
else:
    st.write("Survey complete! Thanks for your responses.")

