import streamlit as st

st.title("What Type of Athlete Are You?")

st.write("Answer these questions to find out what type of athlete you are.")

st.image("https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=800")

sport = st.radio("1. What type of sport do you prefer?", ["Individual sport", "Team sport", "I like both"])  #NEW

practice = st.slider("2. How many hours would you practice in a week?", 1, 20, 5)  #NEW

skills = st.multiselect("3. Which qualities describe you?", ["Competitive", "Calm", "Strategic", "Supportive", "Hardworking"])  #NEW

st.image("https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800")

pressure = st.selectbox("4. What do you usually do in a high-pressure situation?", ["Take control", "Think before acting", "Encourage my teammates"])  #NEW

teamSize = st.number_input("5. What is your ideal number of people on a team?", min_value=1, max_value=20, value=5)  #NEW

st.image("https://images.unsplash.com/photo-1526232761682-d26e03ac148e?w=800")

if st.button("See My Result"):  
    competitor = 0
    strategist = 0
    teamPlayer = 0

    if sport == "Individual sport":
        competitor = competitor + 1
    elif sport == "Team sport":
        teamPlayer = teamPlayer + 1
    else:
        strategist = strategist + 1

    if practice >= 10:
        competitor = competitor + 1
    else:
        strategist = strategist + 1

    if "Competitive" in skills:
        competitor = competitor + 1
    if "Strategic" in skills:
        strategist = strategist + 1
    if "Calm" in skills:
        strategist = strategist + 1
    if "Supportive" in skills:
        teamPlayer = teamPlayer + 1
    if "Hardworking" in skills:
        competitor = competitor + 1

    if pressure == "Take control":
        competitor = competitor + 1
    elif pressure == "Think before acting":
        strategist = strategist + 1
    else:
        teamPlayer = teamPlayer + 1

    if teamSize <= 2:
        competitor = competitor + 1
    elif teamSize <= 6:
        strategist = strategist + 1
    else:
        teamPlayer = teamPlayer + 1

    if competitor >= strategist and competitor >= teamPlayer:
        st.header("You are a Competitor!")
        st.write("You are motivated by competition and enjoy trying to perform at your best.")

    elif strategist >= competitor and strategist >= teamPlayer:
        st.header("You are a Strategist!")
        st.write("You usually focus on finding the smartest way to handle a situation.")

    else:
        st.header("You are a Team Player!")
        st.write("You value teamwork and communication.")

    st.balloons()  
