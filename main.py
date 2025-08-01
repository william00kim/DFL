from fastapi import FastAPI
from typing import Union
import sys
import os

sys.path.append("/HDD1/rlawhdgus1212/work/DFL")
from model import Langchain as LM
from controller import RequestToAI as Req

data = Req.RequestToAI
model = Req.Model
text = ""
app = FastAPI()

@app.post("/model/{model_name}")
async def AIrequset_gemma(Data : data, model_name:model):
    llm = LM.Langchain(model_name.value)

    print(Data.prompt)
    
    model = llm.get_LLM_name()

    prompt = llm.create_prompt(Data.prompt)

    res = llm.call_ollama(model, prompt)

    return res