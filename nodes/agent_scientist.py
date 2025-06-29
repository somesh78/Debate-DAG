import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def agent_a_response(round_num, memory_summary, topic):
    prompt = f"You are a Scientist debating the topic: '{topic}'. You must argue in favor of regulating AI like medicine. Your opponent said: {memory_summary}. Give a logical argument supporting regulation."

    chat = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    return chat.choices[0].message.content.strip()
