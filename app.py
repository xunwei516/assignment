
import streamlit as st
from planner import generate_plan
from memory import save_memory, load_memory
st.sidebar.title("Agent Features")

st.sidebar.write("✅ Goal Understanding")
st.sidebar.write("✅ Planning")
st.sidebar.write("✅ Memory")
st.sidebar.write("✅ Priority Reasoning")
st.sidebar.write("✅ Safety Filter")
st.sidebar.write("✅ Feedback Loop")
st.title("AI Task Planning Agent")
st.caption("An intelligent agent that plans, prioritizes, and adapts tasks.")

goal = st.text_input("Enter your goal:")
feedback = st.text_input("Provide feedback or progress update:")
if st.button("Generate Plan"):

    if goal.strip() == "":
        st.warning("Please enter a goal.")
    else:
        combined_input = goal + " " + feedback

        plan = generate_plan(combined_input)

        st.subheader("Generated Plan")
        st.write(plan)

        save_memory(goal, plan)
st.success("Plan generated successfully!")
st.subheader("Memory")

memory = load_memory()

for item in memory:
    st.write("Goal:", item["goal"])
    st.write("Plan:", item["plan"])
    st.write("---")