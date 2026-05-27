# Intelligent Task Planning Agent

## Project Overview

This project is a prototype intelligent software agent developed for the course assignment.

The agent can:
- Perceive user goals
- Generate task plans
- Prioritize actions
- Adapt plans based on user feedback
- Store memory of previous tasks
- Apply basic safety filtering

The system demonstrates core intelligent agent concepts including reasoning, planning, memory, decision-making, and adaptive behavior.

---

# Features

## Goal Understanding
The agent accepts user goals through a web interface and interprets task objectives.

## Task Planning
The agent uses LLM reasoning to break goals into actionable steps.

## Priority Reasoning
Tasks are categorized into:
- High Priority
- Medium Priority
- Low Priority

## Feedback Loop
Users can provide progress updates and the agent dynamically updates the plan.

Example:
- User Goal: "Finish assignment"
- Feedback: "I already completed research"

The agent replans remaining steps accordingly.

## Memory System
Previous goals and generated plans are stored in `memory.json`.

## Safety Mechanism
Unsafe requests containing harmful keywords are blocked.

---

# System Architecture

User Input
↓
Perception Module
↓
LLM Reasoning Engine
↓
Planning Module
↓
Priority Decision Module
↓
Safety Filter
↓
Memory System
↓
Action Output

---

# Technologies Used

- Python
- Streamlit
- DeepSeek API
- JSON Memory Storage

---

# Project Structure

```bash
task-planning-agent/
│
├── app.py
├── planner.py
├── memory.py
├── memory.json
├── requirements.txt
├── README.md

Clone Repository
git clone https://github.com/yourusername/task-planning-agent.git

Install Dependencies
pip install -r requirements.txt

Add Your DeepSeek API Key
Open planner.py and replace:sk-6ef30002fc2f43059fa889390bb9cf69

Running the Application
Run the following command:streamlit run app.py
Then open:http://localhost:8501

Example Usage
Goal:Finish my assignment in 3 days
Feedback:I already completed research
Agent Output:1. High Priority - Create assignment outline
2. High Priority - Write first draft
3. Medium Priority - Revise content
4. Low Priority - Final formatting

Design Evolution
Version 1
Basic task planning agent
User goal input
LLM-generated plans
Version 2
Added persistent memory system
Stored previous goals and plans
Version 3
Added priority reasoning
Added feedback loop
Version 4
Added safety filtering
Improved UI and error handling










