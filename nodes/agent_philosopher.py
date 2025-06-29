import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def agent_b_response(round_num, memory_summary, topic):
    prompt = f"You are a Philosopher debating the topic: '{topic}'. You must argue against strict AI regulation, supporting freedom and autonomy. Your opponent said: {memory_summary}. Provide a thoughtful counter-argument."

    chat = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    return chat.choices[0].message.content.strip()
