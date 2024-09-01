import streamlit as st
import time
import random

st.set_page_config(
    page_title="Autobiography - Cold Case",
    page_icon=":mag:",
    layout="centered",
)

# Apply custom CSS for background and margins
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');

    .title {
        margin-bottom: 5%; 
        max-width: 80%; 
        margin-left: auto;
        margin-right: auto;
        text-align: center;
            
    }
    
    .content { 
        max-width: 100%;
        font-size: 18px;
        margin-left: auto;
        margin-right: auto;
    }
            
    h1, h2, h3, h4, h5, h6, *{
        font-family: 'Special Elite', cursive;
    }
    

    
    p {
        margin: 2%;
        max-width: 100%; 
        font-size: 18px;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>The Curious Case of Reina Empleo 🔎</h1>", unsafe_allow_html=True)

# Autobiography text
autobiography_text = (
"My name is Reina Luz B. Empleo. I was born on November 12, 1999, in a house on Tres de Abril Street, Punta Princesa, located in Cebu City. I grew up in a sheltered environment, as I was often sick and the only daughter in my family."

"\n\nI have always been a curious-minded person who loves puzzle, simulation, educational, and investigation games, which fueled my curiosity about computers. I would mess with flash games or various software on my old family PC. Ever since then, I’ve always had an easier time learning applications and different software. This interest led me to take the STEM strand in SHS."

"\n\nI attended Cebu Institute of Technology - University, where I grew to be more knowledgeable in science and technology. I learned a lot during that time, such as leadership skills and how to deal with people. My hard work and dedication paid off, earning me a 'with Honors' medal and a slight one-semester tuition discount when I went to college."

"\n\nStill attending the same university, I initially pursued a degree in Computer Science. However, it was during the height of COVID-19, and the online setting greatly affected my mental health. Personally, I did my worst in school during those years. So at the end of the 2nd year, I shifted to Information Technology. My years in IT have been the most transformative for me—personally, mentally, and academically. I’ve worked on projects and group seatworks with innovative people under the supervision of esteemed professors, developing lifelong friendships with some of them."

"\n\nCurrently, I'm a 4th-year IT student in my last semester before graduation. I'm looking for an internship that will build a solid foundation for the start of my career. I've grown to be a better person than I was when I started college, having grown out of my comfort zone. I'm actively pursuing a career in Cybersecurity, hoping to become a SOC Analyst or a Digital Forensics Examiner. \n\nI never really thought I'd reach this far :>"


)

# Session state to track if text is typed
if "typed_text" not in st.session_state:
    st.session_state.typed_text = ""

if "typing" not in st.session_state:
    st.session_state.typing = True

# Buttons for reset and skip functionality
_, one, _, two = st.columns([.5, 1, 1, 1], vertical_alignment="bottom")
if one.button("Reset", type="primary"):
    st.session_state.typed_text = ""
    st.session_state.typing = True

if two.button("Skip", type="primary"):
    st.session_state.typing = False
    st.session_state.typed_text = autobiography_text

st.divider()

# Typewriter effect for the autobiography
placeholder = st.empty()

if st.session_state.typing:
    typed_text = ""
    for char in autobiography_text:
        if not st.session_state.typing:
            break
        typed_text += char
        placeholder.markdown(f"<p class='content'>{typed_text}</p>", unsafe_allow_html=True)
        
        # Simulate typing speed with random stops
        if random.random() < 0.03:  
            time.sleep(random.uniform(0.3, 0.4))  # Random stop duration between 0.3 to 0.4 seconds
        else:
            time.sleep(0.03)  # Normal typing speed
    
    st.session_state.typing = False
    st.session_state.typed_text = typed_text
else:
    placeholder.markdown(f"<p class='content'>{st.session_state.typed_text}</p>", unsafe_allow_html=True)

st.divider()

# Feedback section
left, middle, right = st.columns(3, vertical_alignment="bottom")

left.link_button("My Portfolio", "https://hyper-elbow-836.notion.site/Hey-I-m-Reina-2461f8a60c064998b77c16e2b92684f2?pvs=25")

middle.write("What do you think? Leave a reaction :>")

with right:
    sentiment_mapping = ["Disappointed", "Sad", "Neutral", "Happy", "Ecstatic"]
    selected = st.feedback("faces")
    
    if selected is not None:
        if selected == 0:
            st.markdown("😞 Oh... you seem disappointed. Let me know how I can improve!")
        elif selected == 1:
            st.markdown("😢 I'm sorry you're feeling sad. Let me know why!")
        elif selected == 2:
            st.markdown("😐 You're feeling neutral. Got any suggestions to make things better?")
        elif selected == 3:
            st.markdown("😊 Glad to see you're happy! Your feedback is appreciated!")
        elif selected == 4:
            st.markdown("🎉 Ecstatic! That's awesome to hear. Thanks for the great feedback!")

st.divider()

# Video section
st.caption("Start at 0:10 with captions")
VIDEO_URL = "https://www.youtube.com/watch?v=NDU-IZkRoKc"
st.video(VIDEO_URL)
