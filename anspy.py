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