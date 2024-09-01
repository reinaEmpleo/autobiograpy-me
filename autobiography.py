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
        margin: auto; 
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
    "My name is Reina Luz B. Empleo. I was born on November 12, 1999, in a house in Punta Princesa, Tres de Abril Street."
    " Located in Cebu City. I grew up in a sheltered environment, given that I was mostly sick and the only daughter in my family."
    
    "\n\nI have always been a curious-minded person who loves puzzle, simulation, educational and investigation games which fueled my curiosity in computers."
    " I would mess with flash games or with some softwares in my old family PC."
    " Ever since then, I always had an easier time to learn applications and various software. This interest led me to take STEM strand in SHS."
 
    "\n\nI attended Cebu Institute of Technology - University, where I grew to be a more knowledgeable person on science and technology. I learned a lot of things during that time, such as leadership and how to deal with people."
    " My hardwork and dedication paid off and earned me a 'with Honors' medal, also a slight one semester tuition discount when I went to college."
    
    "\n\nStill attending the same University, I pursued a degree in Computer Science first. However it was the height of COVID-19, and the online setting greatly effected my mental health."
    " Personally, I did my worse at school during those years. So in the end of 2nd year, I shifted to Information Technology. And my years in IT had the most transformative experiences for me."
    " Personally, mentally and academically. I had made projects and groupworks with such innovative people under the supervisory of esteemed professors, developing lifelong friendships with some of them."

    "\n\n Currently, I'm a 4th year IT student, in my last semester before I graduate. I'm looking for an internship that would build a solid foundation for the start of my career."
    " I've grown to be a better person than I was when I started college. That I grew out of my comfort zone and, I'm actively pursuing a career in Cybersecurity, hoping to be a SOC analyst or a Digital Forensics Examiner."
    "\n\nI never really thought I'd reach this far :>"
)

# Session state to track if text is typed
if "typed_text" not in st.session_state:
    st.session_state.typed_text = ""

if "typing" not in st.session_state:
    st.session_state.typing = True

# Buttons for reset and skip functionality
_, one, _, two = st.columns([1, 2, 1, 2], vertical_alignment="bottom")
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
