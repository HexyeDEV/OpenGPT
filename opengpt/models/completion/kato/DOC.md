# How to Use

To use this model is very simple.
To make a ChatBot with kato you can:
```py
from opengpt.models.completion.kato.model import Model # first, we import it

kato = Model() # here we initialize the model.

while True:
    prompt = input("Your Prompt: ") # here we get your prompt
    print(kato.GetAnswer(prompt)) # here we print the answer.
```

Note: Conversations are kept by default.