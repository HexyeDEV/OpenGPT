import requests

class Model:
    def __init__(self):
        self.messages = [{"role": "system", "content": "<p><b>I'm sorry, but sometimes I may provide inaccurate information since I'm still a work in progress.</b></p>"}]

    def GetAnswer(self, prompt):
        url = "https://www.kato.to/advancedApi/ai/chat"
        headers = {
            "content-type": "application/json"
        }
        self.messages.append({"role": "user", "content": prompt})
        r = requests.post(url, headers=headers, json=self.messages)
        self.messages.append({"role": "assistant", "content": r.text})
        return r.text