import requests

url = "http://localhost:11434/api/chat"

payload = {
    "model": "exaone3.5:32b",
    "messages": [
        {"role": "user", "content": "안녕하세요. 한국어로 맗해줘요"}
    ],
    "stream": False
}

response = requests.post(url, json=payload, verify=False)

print(response.json()['message']['content'])
