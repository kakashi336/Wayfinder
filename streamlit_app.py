import streamlit as st
from logic import (create_prompt_user_response_matrix, get_openai_response, read_csv, get_top_locations,
                   filter_csv_region)

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
        st.session_state.questions = [
            "May I ask how many adults, children, and pets will be joining you in your new home?",
            "Would you like to narrow down your search to a specific city or county, or are you open to exploring different areas?",
            "What type of area are you most interested in? Are you looking for an urban environment, a metropolitan area, a semi-urban setting, a small town, a village, or perhaps a micropolitan area?",
            "What would be your ideal monthly budget for living expenses, including housing, utilities, and transportation?",
            "How important is it for you to have essential services like hospitals, schools, and grocery stores nearby?",
            "How significant is safety for you when choosing a neighborhood, particularly in terms of low crime rates and a strong community atmosphere?",
            "How often do you participate in community events or local meetings? Is this something you'd like to continue in your new area?",
            "How frequently do you plan to visit parks, recreational facilities, or engage in outdoor activities in your new neighborhood?",
            "How much do cultural events, such as festivals or museum visits, play a role in your lifestyle? How many would you like to attend each year?",
            "How important is it for you to live in a community with thriving local businesses, job opportunities, and a strong sense of belonging?",
            "How often would you like to spend time in green spaces, parks, or near natural water bodies in your new area?",
            "Do you plan to use a car for commuting? If so, how much time are you comfortable spending in the car each day?",
            "How often do you anticipate using public transport, and how important is it for you to have convenient access to it?",
            "How important is it for you to live in an area that is pedestrian-friendly and has good biking infrastructure? How often do you plan to walk or bike for your daily activities?",
            "How important is it to you to live in a place with good air and water quality, as well as minimal noise and light pollution?",
            "Is access to healthy food options and nearby grocery stores a significant factor in your decision-making process?",
            "How crucial is it for you to live in an area with high housing standards, including well-maintained properties and infrastructure?",
            "Do you or any family members have allergies (such as pollen) or specific health conditions that should be considered?",
            "Is there anything specific that’s especially important to you in a new home, something that would be non-negotiable or a deal-breaker?"
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

    user_response_dict = {
        "demographics": {
            "number_of_family_members": {
                "question": st.session_state.questions[0],
                "response": st.session_state.responses[0]
            },
            "city_or_county_preference": {
                "question": st.session_state.questions[1],
                "response": st.session_state.responses[1]
            },
            "urban_or_rural_preference": {
                "question": st.session_state.questions[2],
                "response": st.session_state.responses[2]
            },
        },
        "a_sense_of_control": {
            "cost_of_living": {
                "question": st.session_state.questions[3],
                "response": st.session_state.responses[3]
            },
            "essential_services": {
                "question": st.session_state.questions[4],
                "response": st.session_state.responses[4]
            },
            "safety": {
                "question": st.session_state.questions[5],
                "response": st.session_state.responses[5]
            },
            "influence_and_contribution": {
                "question": st.session_state.questions[6],
                "response": st.session_state.responses[6]
            }
        },
        "a_sense_of_wonder": {
            "play_and_recreation": {
                "question": st.session_state.questions[7],
                "response": st.session_state.responses[7]
            },
            "distinctive_design_and_culture": {
                "question": st.session_state.questions[8],
                "response": st.session_state.responses[8]
            }
        },
        "connected_communities": {
            "local_business_and_jobs": {
                "question": st.session_state.questions[9],
                "response": st.session_state.responses[9]
            }
        },
        "connection_to_nature": {
            "biodiversity": {
                "question": st.session_state.questions[10],
                "response": st.session_state.responses[10]
            }
        },
        "getting_around": {
            "car": {
                "question": st.session_state.questions[11],
                "response": st.session_state.responses[11]
            },
            "public_transport": {
                "question": st.session_state.questions[12],
                "response": st.session_state.responses[12]
            },
            "walking_cycling": {
                "question": st.session_state.questions[13],
                "response": st.session_state.responses[13]
            }
        },
        "health_equity": {
            "air_noise_light": {
                "question": st.session_state.questions[14],
                "response": st.session_state.responses[14]
            },
            "food_choice": {
                "question": st.session_state.questions[15],
                "response": st.session_state.responses[15]
            },
            "housing_standard": {
                "question": st.session_state.questions[16],
                "response": st.session_state.responses[16]
            },
            "allergies": {
                "question": st.session_state.questions[17],
                "response": st.session_state.responses[17]
            }
        },
        "additional_context": {
            "must_have": {
                "question": st.session_state.questions[18],
                "response": st.session_state.responses[18]
            }
        }
    }
    df_qol = read_csv()
    df_qol = filter_csv_region(df_qol, st.session_state.responses[1], st.session_state.questions[2])
    prompt = create_prompt_user_response_matrix(user_response_dict)
    parsed_response = get_openai_response(prompt)
    df_top_locations = get_top_locations(df_qol, parsed_response)
    print(df_top_locations)


if __name__ == "__main__":
    main()
