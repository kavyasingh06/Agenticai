import streamlit as st
from agents import researcher_agent, ideator_agent, evaluator_agent, pitch_generator_agent

st.set_page_config(page_title="AI Startup Ideation Agent")
st.title("🤖 AI-Powered Startup Ideation Agent")

industry = st.text_input("Enter an industry or trend:", "")

if st.button("Generate Startup Ideas") and industry:
    with st.spinner("🧠 Researching market trends..."):
        research = researcher_agent(industry)
        st.subheader("📊 Market Research Findings")
        st.write(research)

    with st.spinner("💡 Generating startup ideas..."):
        ideas = ideator_agent(research)
        st.subheader("🚀 Generated Startup Ideas")
        st.write(ideas)

    with st.spinner("✅ Evaluating ideas..."):
        top_ideas = evaluator_agent(ideas)
        st.subheader("🏆 Top Startup Ideas")
        st.write(top_ideas)

    with st.spinner("🎨 Generating pitch deck..."):
        pitch = pitch_generator_agent(top_ideas)
        st.subheader("📄 Pitch Deck & UI/UX Ideas")
        st.write(pitch)
