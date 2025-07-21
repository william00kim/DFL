from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

class Langchain:

    model = OllamaLLM(model = "")
    word = ""

    def __init__(self, modelchoose):
        self.model = OllamaLLM(model = modelchoose)
    
    def printllm(self):
        return self.model

    def setword(self, word):
        self.word = word

    def getword(self):
        return self.word

    def LangchainStart(self):
        template = f"""
            You are develper and korean. You are really good at coding. 
            Here's the input:

            Word: {self.word}

            Output format:
            1. Definition: [explain code]
            2. Example Sentence: [다음과 같은 코드는 이렇게 해석됩니다. ....]"""

        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | self.model
        # chain.invoke('chain')
        return chain.invoke({"word": prompt})