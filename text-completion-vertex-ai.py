from dotenv import load_dotenv
load_dotenv()

import os
from google.oauth2 import service_account
import vertexai
from vertexai.language_models import TextGenerationModel

google_project_id = os.getenv("GOOGLE_PROJECT_ID")
model:str = "text-bison@001"
location:str = "us-central1"
temperature:float = 0.7
prompt: str = "Write an introductory paragraph to explain Generative AI to the reader of this content." 
parameters = {
        "temperature": temperature}


cred_file = 'gcp-cred.json'
if os.path.isfile(cred_file):
   credentials = service_account.Credentials.from_service_account_file(cred_file)
   vertexai.init(
	project=google_project_id,
	location = location,
	credentials = credentials)
   model = TextGenerationModel.from_pretrained(model)
   response = model.predict(prompt, **parameters)
   print(response.text)
else:
   print("Error: unable to find GCP Vertex AI credential file!")
