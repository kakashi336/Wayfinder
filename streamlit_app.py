import streamlit as st

# Function to handle user input change
def on_input_change():
    if st.session_state.user_input:
        st.session_state.responses.append(st.session_state.user_input)
        st.session_state.user_input = ''
        if st.session_state.questions:
            st.session_state.questions.pop(0)
        st.session_state.progress = len(st.session_state.responses) / st.session_state.total_questions

# Function to clear the conversation and restart
def on_btn_click():
    st.session_state.questions = ['How many adults, children and pets are in your household?', 
                                      'What is your ideal monthly budget for living expenses, including housing, utilities, and transportation?', 
                                      'How critical is access to essential services like healthcare, schools, and grocery stores in your decision-making process?',
                                      'How much do you value safety, including low crime rates and a strong community sense, in your neighborhood?',
                                      'How many community events or local governance meetings do you typically participate in each year?',
                                      'How many cultural events (e.g., festivals, museum visits, theater performances) do you attend in a typical year?',
                                      'Do you interact with recreational or sports facilities, parks, or other outdoor spaces? If yes, how many times per month?',
                                      'How important is it to you that your community has thriving local businesses, job opportunities, and fosters a strong sense of belonging?',
                                      'How many times per month do you visit green spaces, parks, or natural water bodies?',
                                      'How do you prioritize transportation options, including access to public transport, car usage, and pedestrian-friendly infrastructure?',
                                      'How much do you value living in a place with good air and water quality, minimal noise pollution, and proper lighting?',
                                      'How significant is the availability of healthy food options and grocery stores in your choice of living area?',
                                      'How important is it for you to live in an area where housing standards are high, with well-maintained properties and infrastructure?',
                                 ]
    st.session_state.responses = []
    st.session_state.progress = 0
    st.session_state.started = False

# Function to load external CSS file
def load_css(css_file):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Main function to organize code execution
def main():
    load_css('style.css')  # Ensure 'style.css' is in the same directory

    # Display logo at the top with styling
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    st.image('logo.jpg', width=720)
    st.markdown('</div>', unsafe_allow_html=True)

    # Initialize session state
    if 'questions' not in st.session_state:
        st.session_state.questions = ['How many adults, children and pets are in your household?', 
                                      'What is your ideal monthly budget for living expenses, including housing, utilities, and transportation?', 
                                      'How critical is access to essential services like healthcare, schools, and grocery stores in your decision-making process?',
                                      'How much do you value safety, including low crime rates and a strong community sense, in your neighborhood?',
                                      'How many community events or local governance meetings do you typically participate in each year?',
                                      'How many cultural events (e.g., festivals, museum visits, theater performances) do you attend in a typical year?',
                                      'Do you interact with recreational or sports facilities, parks, or other outdoor spaces? If yes, how many times per month?',
                                      'How important is it to you that your community has thriving local businesses, job opportunities, and fosters a strong sense of belonging?',
                                      'How many times per month do you visit green spaces, parks, or natural water bodies?',
                                      'How do you prioritize transportation options, including access to public transport, car usage, and pedestrian-friendly infrastructure?',
                                      'How much do you value living in a place with good air and water quality, minimal noise pollution, and proper lighting?',
                                      'How significant is the availability of healthy food options and grocery stores in your choice of living area?',
                                      'How important is it for you to live in an area where housing standards are high, with well-maintained properties and infrastructure?',
                                     ]
    if 'responses' not in st.session_state:
        st.session_state.responses = []
    if 'progress' not in st.session_state:
        st.session_state.progress = 0
    if 'total_questions' not in st.session_state:
        st.session_state.total_questions = len(st.session_state.questions)
    if 'started' not in st.session_state:
        st.session_state.started = False

    if not st.session_state.started:
        st.markdown('<h1 class="title">🎉 Congratulations on taking the first step to finding your dream home!</h1>', unsafe_allow_html=True)
        st.write("Welcome! We're here to help you with a few quick questions to understand your preferences.")
        
        if st.button("Begin"):
            st.session_state.started = True
    else:
        st.title("Atlantic WayFinder's Chat Assistant")
        st.progress(st.session_state.progress)

        if st.button("Clear and Restart", on_click=on_btn_click):
            st.session_state.started = False

        if st.session_state.questions:
            st.markdown(f'<div class="question-card">{st.session_state.questions[0]}</div>', unsafe_allow_html=True)
            st.text_input("Your response:", on_change=on_input_change, key="user_input")

        else:
            st.success("Thank you for your responses.")

if __name__ == "__main__":
    main()
