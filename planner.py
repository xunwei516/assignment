from openai import OpenAI

client = OpenAI(
    api_key="sk-6ef30002fc2f43059fa889390bb9cf69",
    base_url="https://api.deepseek.com"
)


def generate_plan(goal):
    unsafe_keywords = ["hack", "steal", "attack", "virus"]

    for word in unsafe_keywords:
        if word in goal.lower():
            return "Unsafe goal detected. Request blocked."
    prompt = f"""
    You are an intelligent planning agent.

    Break this goal into prioritized actionable steps.
Label each step as:
- High Priority
- Medium Priority
- Low Priority

    Goal:
    {goal}
    """

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content