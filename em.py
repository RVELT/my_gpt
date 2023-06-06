openai.api_key = ""

while True:
    model_engine = "text-davinci-003"
    prompt = input("Bir şeyler giriniz: ")

    if 'exit' in prompt or 'quit' in prompt:
        break

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None
    )

    response = completion.choices[0].text.strip()

    print(response)