## anspy
anspy is a terminal version of ChatGPT developed using openai's api and python.<br>

Please download the python file from above and actually use it by following the procedure explained below.<br>

The purpose of anspy is to solve questions while writing a program on the terminal without having to jump to the ChatGPT site.<br>

By using anspy, you can efficiently solve questions that come up when you are learning programming or writing a program.<br>

## How to use anspy

<br>Enter your openai API-key in the API-key section.

```
import openai

openai.api_key = "API-key"

question = input("Enter your question : ")

res = openai.Completion.create(
	engine = "text-davinci-003",
	prompt = question,
	max_tokens = 1024,
	temperature = 1.0
)

print(res.choices[0].text)
```

## How to run anspy

```
~/anspy.py $ python anspy.py
```

<br>English Versions

<br>
<img src="https://github.com/i-inose/anspy/blob/main/anspy-img.png?raw=true"><br>

<br>Japanese Versions

<br>
<img src="https://github.com/i-inose/anspy/blob/main/anspy-img2.png?raw=true"><br>

Written by Izuru Inose / 伊野瀬出<br>
-At the Takefuji Lab-
