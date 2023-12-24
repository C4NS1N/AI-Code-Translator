from openai import OpenAI

client = OpenAI(
    api_key="CHATGPT-API-KEY",
)


def translate_code(input_code, source_language, target_language):
    prompt = f"Translate the '{source_language}' code to '{target_language}':\n{input_code}\n"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that translates code.",
            },
            {"role": "user", "content": prompt},
        ],
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0,
    )

    translation = response.choices[0].message.content.strip()
    return translation
