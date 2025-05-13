import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or "mistral" if you're using a local/other model
        messages=[
            {"role": "system", "content": "Summarize this meeting transcript."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()

def generate_insights(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Provide business insights and action items from this text."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()
