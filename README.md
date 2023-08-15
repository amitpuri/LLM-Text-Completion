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
  - LLaMA-2 Together API
    - TOGETHER_API_KEY from https://api.together.xyz/playground,
    - Start LLaMA-2 Chat (70B)
- for running individual Python programs, use this

  Installation 

      pip install -r requirements.txt
  
  [OpenAI Python API](https://platform.openai.com/docs/api-reference)
 
      python text-completion.py
  
  [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai)
  
      python text-completion-azure.py

  [LLaMA-2 Chat (70B)](https://api.together.xyz/playground)
  
      python text-completion-together-api-llama.py

or use these notebooks

- [Gradio App](https://nbviewer.org/github/amitpuri/LLM-Text-Completion/blob/main/gradio-app.ipynb)
- [OpenAI text-completion](https://nbviewer.org/github/amitpuri/LLM-Text-Completion/blob/main/text-completion-azure.ipynb)
- [Azure OpenAI text-completion](https://nbviewer.org/github/amitpuri/LLM-Text-Completion/blob/main/text-completion.ipynb)

Further, simplify using LangChain or Semantic Kernel
- [Text Completion via LangChain](https://github.com/amitpuri/LLM-Text-Completion-langchain)
- [Text Completion via Semantic Kernel](https://github.com/amitpuri/LLM-Text-Completion-Semantic-Kernel)

ChatGPT Plugin
- [Plugins/examples](https://platform.openai.com/docs/plugins/examples/example-plugins)
- [ChatGPT plugins quickstart](https://github.com/openai/plugins-quickstart)
- [ChatGPT Retrieval Plugin](https://github.com/openai/chatgpt-retrieval-plugin)

More comprehensive demos are available on [LLM Scenarios, Use cases on the Gradio app](https://github.com/amitpuri/ask-picturize-it)

**Vertex AI API usage is yet to be implemented.
