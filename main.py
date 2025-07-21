import model.Langchain as L
import model.Langchain_memory as LM

class Main:
    # lang = L.Langchain("exaone3.5:32b")

    # lang.setword("""
    #              class project:
    #             model = "abc"

    #             def printData(self):
    #                 return 'model'
    #             """)
    # print(lang.printllm())
    # print(lang.getword())
    # print(lang.LangchainStart())

    lang_mem = LM.Langchain_memory("exaone3.5:32b")

    question = ["안녕하세요", "오늘의 날씨는?", "한림대학교에 대해서 알려주세요"]

    for question in question:
        result = lang_mem.LangchainMemoryStart.invoke(
            {"input" : question}
        )
        print(result)
        
