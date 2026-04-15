import os
import time
from groq import Groq

def get_api_key():
    return os.getenv("GROQ_API_KEY")

client = Groq(api_key=get_api_key())

def query_groq(system_prompt, user_prompt, temperature, top_p):
    start = time.time()

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=temperature,
        top_p=top_p
    )

    end = time.time()

    response = completion.choices[0].message.content

    total_tokens = completion.usage.total_tokens
    time_taken = end - start

    metrics = {
        "Total Tokens": total_tokens,
        "Tiempo total (s)": round(time_taken, 3),
        "Throughput (tokens/s)": round(total_tokens / time_taken, 2) if time_taken > 0 else 0,
        "Time per token (ms)": round((time_taken / total_tokens) * 1000, 2) if total_tokens > 0 else 0
    }

    return response, metrics
