from langchain_community.llms import Ollama

# Initialize Ollama LLaMA 3
llm = Ollama(model="llama3", temperature=0.7)

def run_llm(prompt: str) -> str:
    """Invoke LLM and return output"""
    return llm.invoke(prompt)

# -------------------------------
# 1️⃣ Researcher Agent
# -------------------------------
def researcher_agent(industry: str) -> str:
    prompt = f"""
    You are a startup market researcher.
    Industry/Trend: '{industry}'
    Collect:
    - Current market trends
    - Key competitors
    - User pain points
    Summarize concisely in 3-5 bullet points.
    """
    return run_llm(prompt)

# -------------------------------
# 2️⃣ Ideator Agent
# -------------------------------
def ideator_agent(research_text: str) -> str:
    prompt = f"""
    You are an AI startup ideator.
    Based on the following market research:
    {research_text}
    Generate 5 innovative startup ideas.
    Include a short description for each idea.
    """
    return run_llm(prompt)

# -------------------------------
# 3️⃣ Evaluator Agent
# -------------------------------
def evaluator_agent(ideas_text: str) -> str:
    prompt = f"""
    You are an AI startup evaluator.
    Rate each of the following startup ideas from 1 to 10 based on:
    - Feasibility
    - Market potential
    - Innovation
    Return the top 3 ideas with reasoning.
    {ideas_text}
    """
    return run_llm(prompt)

# -------------------------------
# 4️⃣ Pitch Generator Agent
# -------------------------------
def pitch_generator_agent(top_ideas_text: str) -> str:
    prompt = f"""
    You are an AI pitch deck creator.
    For the following top startup ideas:
    {top_ideas_text}
    Generate a structured pitch deck including:
    - Problem statement
    - Solution
    - Target market
    - Business model
    - Marketing strategy
    - UI/UX mockup ideas
    Format clearly in sections.
    """
    return run_llm(prompt)
