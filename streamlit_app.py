import streamlit as st
from logic import (create_prompt_user_response_matrix, get_openai_response, read_csv, get_top_locations, filter_csv_region)
from config import questions  # Import the questions list from config
import time  # Import time to simulate a loading process
import streamlit as st

def set_background(image_file):
    # Inject CSS for background image
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{image_file}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Function to simulate loading animation
def show_loading_animation():
    with st.spinner('Processing recommendations...'):
        time.sleep(1)  # Simulates the processing delay

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
    st.session_state.questions = questions.copy()
    st.session_state.responses = []
    st.session_state.progress = 0
    st.session_state.started = False

# Function to load external CSS file
def load_css(css_file):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Function to apply inline CSS for background and text color
def set_background_color():
    st.markdown(
        """
        <style>
        body {
            background-color: black;
            color: white;
        }
        .stButton > button {
            background-color: #2c418e;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Main function to organize code execution
def main():


        # Load the background image file (as base64)
    import base64
    with open("logo1.png", "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode()

    # Set the background
    set_background(image_base64)
    load_css('style.css')  # Ensure 'style.css' is in the same directory
    set_background_color()

    # Display logo at the top with styling
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    st.image('blacklogo1.png', width=720)
    st.markdown('</div>', unsafe_allow_html=True)

    # Initialize session state
    if 'questions' not in st.session_state:
        st.session_state.questions = questions.copy()
    if 'responses' not in st.session_state:
        st.session_state.responses = []
    if 'progress' not in st.session_state:
        st.session_state.progress = 0
    if 'total_questions' not in st.session_state:
        st.session_state.total_questions = len(st.session_state.questions)
    if 'started' not in st.session_state:
        st.session_state.started = False

    if not st.session_state.started:
        st.markdown('<h1 class="title1">Congratulations on taking the first step to finding your dream home!</h1>', unsafe_allow_html=True)
        #st.markdown('<h1 class="title1"> I am here to help you maximize your Quality of Life by finding the perfect home and community that aligns with your unique needs and preferences. Please respond to a few questions to get started.', unsafe_allow_html=True)
        #st.markdown('<h1 class="title1" style="color: orange;">I am here to help you maximize your Quality of Life by finding the perfect home and community that aligns with your unique needs and preferences. Please respond to a few questions to get started.</h1>', unsafe_allow_html=True)
        st.markdown(
        """
        <div style="
            background-color: rgba(12, 128, 110, 0.8); 
            padding: 20px; 
            border-radius: 10px; 
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;">
            <p style="font-size: 20px; color: #333;font-weight: bold">
                I am here to help you maximize your Quality of Life by finding the perfect home and community that aligns 
                with your unique needs and preferences. Please respond to a few questions to get started.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
        st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

        
        if st.button("Lets Go!"):
            st.session_state.started = True
    else:
        st.title("Quality of Life Guide")
        st.progress(st.session_state.progress)

        # Process only when all questions have been answered
        if st.session_state.questions:
            st.markdown(f'<div class="question-card">{st.session_state.questions[0]}</div>', unsafe_allow_html=True)

            # Use a text area for dynamic resizing
            st.text_area(
                "Your response:", 
                on_change=on_input_change, 
                key="user_input", 
                height=100,  # Initial height
                placeholder="Type your response here..."
            )

        else:
            # This is where we process the data and show final results
            st.success("Thank you for your responses. I have fount below areas for you to consider")
            process_responses(st.session_state.responses, questions)

def process_responses(responses, questions):
    user_response_dict = {
        "demographics": {
            "number_of_family_members": {
                "question": questions[0],
                "response": responses[0]
            },
            "city_or_county_preference": {
                "question": questions[1],
                "response": responses[1]
            },
            "urban_or_rural_preference": {
                "question": questions[2],
                "response": responses[2]
            },
        },
        "a_sense_of_control": {
            "cost_of_living": {
                "question": questions[3],
                "response": responses[3]
            },
            "essential_services": {
                "question": questions[4],
                "response": responses[4]
            },
            "safety": {
                "question": questions[5],
                "response": responses[5]
            },
            "influence_and_contribution": {
                "question": questions[6],
                "response": responses[6]
            }
        },
        "a_sense_of_wonder": {
            "play_and_recreation": {
                "question": questions[7],
                "response": responses[7]
            },
            "distinctive_design_and_culture": {
                "question": questions[8],
                "response": responses[8]
            }
        },
        "connected_communities": {
            "local_business_and_jobs": {
                "question": questions[9],
                "response": responses[9]
            }
        },
        "connection_to_nature": {
            "biodiversity": {
                "question": questions[10],
                "response": responses[10]
            }
        },
        "getting_around": {
            "car": {
                "question": questions[11],
                "response": responses[11]
            },
            "public_transport": {
                "question": questions[12],
                "response": responses[12]
            },
            "walking_cycling": {
                "question": questions[13],
                "response": responses[13]
            }
        },
        "health_equity": {
            "air_noise_light": {
                "question": questions[14],
                "response": responses[14]
            },
            "food_choice": {
                "question": questions[15],
                "response": responses[15]
            },
            "housing_standard": {
                "question": questions[16],
                "response": responses[16]
            },
            "allergies": {
                "question": questions[17],
                "response": responses[17]
            }
        },
        "additional_context": {
            "must_have": {
                "question": questions[18],
                "response": responses[18]
            }
        }
    }

    #show_loading_animation()
    df_qol = read_csv()
    df_qol = filter_csv_region(df_qol, responses[1], questions[2])
    prompt = create_prompt_user_response_matrix(user_response_dict)
    parsed_response = get_openai_response(prompt)
    df_top_locations = get_top_locations(df_qol, parsed_response)

    # Display the DataFrame
    df_top_locations = df_top_locations[['Electoral Divisions']].reset_index(drop=True)
    df_top_locations.index = df_top_locations.index + 1
    st.dataframe(df_top_locations[['Electoral Divisions']])
    show_loading_animation()
    # Center the detailed report button with added style
    st.markdown("""
        <div style="text-align: center;">
            <a href="https://lookerstudio.google.com/u/0/reporting/98608fea-03d8-4a56-8f91-1d54d397d4ce/page/p_1gn2gfzmkd?s=re98dP96R4s" target="_blank">
                <button style="
                    background-color: #2c418e; 
                    color: white; 
                    padding: 12px 30px; 
                    border: none; 
                    border-radius: 25px; 
                    font-size: 16px; 
                    font-weight: bold;
                    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
                    cursor: pointer;
                    transition: all 0.3s ease;
                " 
                onmouseover="this.style.backgroundColor='#425aa3'; this.style.transform='scale(1.05)';"
                onmouseout="this.style.backgroundColor='#2c418e'; this.style.transform='scale(1)';">
                    Detailed Report
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
