from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_ollama.llms import OllamaLLM

class Langchain_memory:

    llm = OllamaLLM(model = "")
    word = ""
    store = {}

    def __init__(self, modelchoose):
        self.llm = OllamaLLM(model = modelchoose)
    
    def printllm(self):
        return self.llm

    def setword(self, word):
        self.word = word

    def getword(self):
        return self.word
    
    def get_session_histroy(self, session_id:str) -> BaseChatMessageHistory:
        if session_id not in self.store:
            self.store[session_id]
        return self.store[session_id]

    def LangchainMemoryStart(self):
        return RunnableWithMessageHistory(
            runnable,
            get_session_histroy,
            input_messages_key="input",
            history_messages_key="history"
        )