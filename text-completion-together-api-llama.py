import os
import together
from dotenv import load_dotenv
load_dotenv()

prompt: str = "Write an introductory paragraph to explain Generative AI to the reader of this content."
together.api_key = os.getenv("TOGETHER_API_KEY")

model: str = "togethercomputer/llama-2-70b-chat"
output = together.Complete.create(prompt, model=model,temperature=0.7)
text = output['output']['choices'][0]['text']
print(text)
