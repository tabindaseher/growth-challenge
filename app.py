import streamlit as st
import random
import datetime

# Growth mindset challenges
challenges = [
    "Write down 3 things you learned today.",
    "Try something new that makes you uncomfortable.",
    "Replace a negative thought with a positive one.",
    "Ask for feedback and act on it.",
    "Spend 10 minutes visualizing your success.",
    "Set one small goal for the day and accomplish it.",
    "Spend 5 minutes meditating and clearing your mind.",
    "Learn something new for 10 minutes."
]

# Motivational quotes
quotes = [
    "Failure is the opportunity to begin again more intelligently. - Henry Ford",
    "Your only limit is your mind.",
    "Growth and comfort do not coexist. - Ginni Rometty",
    "Mistakes are proof that you are trying.",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Your future is created by what you do today, not tomorrow. - Robert Kiyosaki",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
    "Success is the sum of small efforts, repeated day in and day out. - Robert Collier",
    "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis"
]

# Streamlit UI with personalization
st.title("Growth Mindset Challenge 🚀")

# Personalized Greeting
username = st.text_input("What’s your name?", "")
if username:
    st.write(f"Hello, {username}! Welcome to your growth journey. 🌱")

# Avatar Selection
avatars = ["😊", "💪", "🌟", "🔥"]
avatar = st.selectbox("Choose an avatar for your journey!", avatars)
st.write(f"Your avatar: {avatar}")

# Show current date
today = datetime.date.today()
st.write(f"Today’s Date: {today}")

st.header("Today's Challenge")
challenge = random.choice(challenges)
st.write(challenge)

# Input for user response
user_response = st.text_area("Write your thoughts or how you're planning to complete the challenge:")

# Mood Tracking
mood = st.radio("How do you feel about today's challenge?", ["😊", "😐", "😓", "💪"])

st.header("Motivational Quote 🌞")
st.write(random.choice(quotes))

# User Progress Tracking (using chart)
st.sidebar.header("Track Your Progress")
progress = st.sidebar.slider("How much did you complete today's challenge?", 0, 100, 50)
st.sidebar.write(f"Your progress: {progress}%")

# Streak Tracker
if 'streak' not in st.session_state:
    st.session_state.streak = 0  # Initialize streak if it's the first time

# Increment streak if progress is 100%
if progress == 100:
    st.session_state.streak += 1
    st.sidebar.write(f"Your current streak: {st.session_state.streak} day(s)!")
else:
    st.session_state.streak = 0  # Reset streak if not completed

# Save and display user feedback
if st.button("Submit Feedback"):
    if user_response:
        st.success(f"Thank you for sharing your thoughts! Keep up the good work.")
        st.write("Here's what you wrote:")
        st.write(user_response)
        st.write(f"You feel: {mood}")
    else:
        st.warning("Please share your thoughts or plan to complete the challenge!")

# Encourage user with personalized feedback
if progress == 100:
    st.success(f"Awesome, {username}! You've completed the challenge. Keep it up!")
elif progress >= 50:
    st.info(f"Great progress, {username}! Keep going, you're on the right track.")
else:
    st.warning(f"Don't give up, {username}! You can do it, just keep moving forward!")

# Display past challenges if user wants to review them
st.sidebar.header("Review Past Challenges")
if st.sidebar.button("Show Past Challenges"):
    if 'history' not in st.session_state:
        st.session_state.history = []
    st.session_state.history.append((today, challenge, progress))
    
    st.sidebar.write("Past Challenges:")
    for record in st.session_state.history:
        st.sidebar.write(f"Date: {record[0]}, Challenge: {record[1]}, Progress: {record[2]}%")

# Random challenge mode (to encourage users to try different challenges)
st.sidebar.header("Random Challenge Mode")
if st.sidebar.button("Get a Random Challenge"):
    random_challenge = random.choice(challenges)
    st.sidebar.write(f"Here's a random challenge for you: {random_challenge}")
