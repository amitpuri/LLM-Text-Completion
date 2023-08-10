# LLM Text Completion - A Simplified Demo

- clone this repo
- rename example.env to .env
- set environment variables in .env file
  - OPENAI_API_KEY from https://platform.openai.com/account/api-keys
  - Azure OpenAI Service Settings from Azure OpenAI https://portal.azure.com
    - AZURE_OPENAI_KEY 
    - AZURE_OPENAI_ENDPOINT
    - AZURE_OPENAI_DEPLOYMENT_NAME
  - GOOGLE_PALM_AI_API_KEY from https://makersuite.google.com
- for running individual Python programs, use this

  Installation 

      pip install -r requirements.txt
  
  OpenAI Python API
 
      python text-completion.py
  
  Azure OpenAI Service
  
      python text-completion-azure.py

or use these notebooks

- [Gradio App](https://nbviewer.org/github/amitpuri/LLM-Text-Completion/blob/main/gradio-app.ipynb)
- [OpenAI text-completion](https://nbviewer.org/github/amitpuri/LLM-Text-Completion/blob/main/text-completion-azure.ipynb)
- [Azure OpenAI text-completion](https://nbviewer.org/github/amitpuri/LLM-Text-Completion/blob/main/text-completion.ipynb)


More comprehensive demo available on https://github.com/amitpuri/ask-picturize-it

Further, simplify using LangChain
- [LangChain Python](https://python.langchain.com/docs/get_started/quickstart)
