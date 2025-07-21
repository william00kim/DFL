import ollama
import os
import subprocess

class chatting:
    
    model = "exaone3.5:32b"

    def __init__(self):
        os.system("ollama run " + str(self.model))
        
    def chatToOllama(self, chat):
        os.system(str(chat))
    

