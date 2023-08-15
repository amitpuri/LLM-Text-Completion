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
  - Vertex AI
      - GOOGLE_PROJECT_ID from Google Cloud console, refer to this https://cloud.google.com/vertex-ai/docs/start/cloud-environment
      - In the Google Cloud console, on the project selector page, select or create a Google Cloud project.
      - Go to [project selector](https://console.cloud.google.com/projectselector2/home/dashboard)
      - Make sure that billing is [enabled for your Google Cloud project](https://console.cloud.google.com/billing).
      - Enable the Vertex AI API
          -  [Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com).
      - Add GCP Credential file as gcp-cred.json for Vertex AI, IAM -> Service accounts -> An account -> Keys from [https://console.cloud.google.com/iam-admin/serviceaccounts](https://console.cloud.google.com/iam-admin/serviceaccounts).
- for running individual Python programs, use this

  Installation 

      pip install -r requirements.txt
  
  [OpenAI Python API](https://platform.openai.com/docs/api-reference)
 
      python text-completion.py
  
  [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai)
  
      python text-completion-azure.py

  [LLaMA-2 Chat (70B)](https://api.together.xyz/playground)
  
      python text-completion-together-api-llama.py

  [Vertex AI](https://cloud.google.com/vertex-ai)
  
      python text-completion-vertex-ai.py

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

