import streamlit as st

# Page Configuration
st.set_page_config(page_title="Growth Mindset Project", page_icon="🌟", layout="centered")

# Custom CSS for Styling
st.markdown(
    """
    <style>
        .main {background-color: #f5f7fa;}
        h1 {color: #4CAF50; text-align: center; font-size: 2.5em;}
        h2 {color: #2196F3;}
        .stTextInput, .stTextArea {background-color: #ffffff; border-radius: 10px;}
        .stAlert {background-color: #e8f5e9; border-left: 5px solid #4CAF50;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and Introduction
st.title("🌱 Growth Mindset Challenges: Web App with Streamlit")
st.markdown("""
    ### 🚀 Welcome to Your Growth Journey!
    Embrace challenges, learn from mistakes, and unlock your full potential. 
    This AI-powered app helps you build a **growth mindset** through reflection, challenges, and achievements! ✨
""")

# Growth Mindset Quote
st.subheader("💡 Today's Growth Mindset Quote")
st.markdown(
    """ _"Success is not final, failure is not fatal: it is the courage to continue that counts."_
    
    — **Winston Churchill**
    """
)

# Challenge Input
st.subheader("🔧 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"💪 You're facing: **{user_input}**. Keep pushing forward towards your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started! 💡")

# Reflection Section
st.subheader("🧠 Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"🏆 Great insight! Your reflection: **{reflection}**")
else:
    st.info("Reflecting on past experiences helps you grow! Share your thoughts. 📝")

# Achievements Section
st.subheader("🎉 Celebrate Your Wins!")
achievements = st.text_input("Share something you've recently accomplished:")

if achievements:
    st.success(f"🎊 Amazing! Your achievement: **{achievements}**")
else:
    st.info("Big or small, every achievement counts! Share one now. 😊")

# Footer
st.markdown("---")
st.markdown("🚀 **Keep believing in yourself. Growth is a journey, not a destination! 🌟**")
st.markdown("**🔷 Created by Nazia Siraj**")
