from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.schema import AIMessage

model = OllamaLLM(model = "gemma3:27b")

memory = ConversationBufferMemory()


user_input = ""

while(user_input != "bye" and user_input != "안녕히계세요" ):
    
    user_input = input("입력해주세요. > ")

    if user_input == "" :

        print("빈 공간은 입력할 수 없습니다.")

    else:
        
        history = memory.load_memory_variables({})["history"]

        print("")

        prompt_template = ChatPromptTemplate.from_template(
            "당신은 개발자입니다. 개발에 특화되어있으며 원론적인 컴퓨터 구조, 운영체제 등 " \
            "모든 컴퓨터 이론은 빠삭하게 알고 있습니다. " \
            "컴퓨터에 관한 질문이 아닌 질문에 대해서는 회피해주세요" \
            "또힌 인사말이 나오면 그냥 '감사합니다.'와 같은 인사말로 가볍게 인사해 주세요" \
            "지금까지 대화 내역은 다음과 같습니다: {history} 이를 기반으로 다음 질문에 대해 답변해주세요{text}"
        )

        prompt = prompt_template.invoke({
            "text" : str(user_input), 
            "history" : str(history)
        })

        response = model.invoke(prompt)

        print(response)

        memory.save_context(
            inputs={"input": user_input},
            outputs={"output" : response}
        )
        

        # ai_messages = [m for m in memory.chat_memory.messages if isinstance(m, AIMessage)]
        # if ai_messages:
        #     print(ai_messages[-1].content)
        # else:
        #     print(response)
        # print("")