import openai

openai.api_key = "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"

question = input("Enter your question : ")

res = openai.Completion.create(
	engine = "text-davinci-003",
	prompt = question,
	max_tokens = 1024,
	temperature = 1.0
)

print(res.choices[0].text)