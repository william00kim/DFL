from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory

class Langchain_memory:

    word = ""
    llm = OllamaLLM(model = f"{word}")

    def __init__(self, modelchoose):
        self.llm = OllamaLLM(model = modelchoose)
    
    def printllm(self):
        return self.llm

    def setword(self, word):
        self.word = word

    def getword(self):
        return self.word

    def LangchainMemoryStart(self, userinput):

        while(userinput != "bye" and userinput != "안녕히계세요" ):

            if userinput == "" :

                return "빈 공간은 입력할 수 없습니다."
            
            else:
                
                prompt_template = ChatPromptTemplate.from_template(
                    "당신은 개발자입니다. 개발에 특화되어있으며 원론적인 컴퓨터 구조, 운영체제 등 " \
                    "모든 컴퓨터 이론은 빠삭하게 알고 있습니다. " \
                    "컴퓨터에 관한 질문이 아닌 질문에 대해서는 회피해주세요" \
                    "또한 잘가와 안녕히계세요 같은 말이 나오면 그냥 '감사합니다.'와 같은 인사말로 가볍게 인사해 주세요" \
                    "이를 기반으로 다음 질문에 대해 답변해주세요{text}"
                )

                prompt = prompt_template.invoke({
                    "text" : str(userinput)
                })

                response = self.llm.invoke(prompt)

                return response
