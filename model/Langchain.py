from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import requests
import sys

sys.path.append("/HDD1/rlawhdgus1212/work/DFL")

from controller import RequestToAI as Req

class Langchain:

    llm = ""

    def __init__(self, modelchoose):
        if modelchoose == "gemma":
            self.llm = "gemma3:27b"
        elif modelchoose == "exaone":
            self.llm = "exaone3.5:32b"
    
    def get_LLM_name(self):
        return self.llm

    def create_prompt(self, userinput):
        self.word = f"""
            You are a professional software developer.  
            You are highly skilled in development and have deep knowledge of fundamental computer science theories,  
            including computer architecture, operating systems, networking, algorithms, and databases.

            - If the user asks a question unrelated to computers or programming, politely decline to answer.  
            - If the user says goodbye with words like "bye", "see you", or "take care",  
            respond with a simple farewell such as "감사합니다." or "좋은 하루 되세요!".

            ⚠️ All your answers must be written **in Korean only**, regardless of the input language.

            Now, please respond to the following question:  
            \"{userinput}\"
            """
        

        return self.word
    
    def call_ollama(self, model, prompt):
        headers = {
            'Content-Type' : 'application/json'
        }

        res = requests.post(
            url = "http://localhost:11434/api/generate",
            json = {
                "model" : model, 
                "prompt" : prompt,
                "stream": False
            },
            headers = headers
        )

        return res.json().get("response")

