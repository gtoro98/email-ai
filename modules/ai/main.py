import requests
from env import aiApiKey
import google.generativeai as genai
from modules.email.outgoing import sendEmail

genai.configure(api_key=aiApiKey)

def respondMessage(senderEmail, prompt):
  model = genai.GenerativeModel("gemini-1.5-flash")
  response = model.generate_content(prompt)
  print(response.text)
  sendEmail(senderEmail, response.text)


