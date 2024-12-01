from openai import OpenAI

# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
    api_key="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",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named cyber jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "what is coding"}
]
)

print(completion.choices[0].message.content)