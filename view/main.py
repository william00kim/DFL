from fastapi import FastAPI
from typing import Union
import sys

from model import Langchain_memory as LM
from controller import RequestToAI as Req

app = FastAPI()

data = Req.RequestToAI

@app.get("/")
def read_root():
    return {"Hello" : "World!"}

@app.get("/gemma")
def AIrequset_gemma():
    llm1 = LM.Langchain_memory("gemma3:27b")

    return {"LLM" : llm1.LangchainMemoryStart("엄엄 은 if 문이고 엄 = 엄엄 과 같은  방식으로 변수를 지정해 줄 수 있습니다. 엄1하면 integer, 엄2 하면  double 엄3은 float 형식의 언어입니다. 배열은 엄[] =  엄준 []과 같은 방식으로 선언할 수 있습니다. 이를 기반으로 3*3 기반 배열을 만들어주세요")}

@app.post("/exaone3")
async def AIrequset_exaone(Data : data):
    llm2 = LM.Langchain_memory("exaone3.5:32b")
    return {"LLM" : llm2.LangchainMemoryStart(Data.text)}
