import os
import cohere

class Cohere:
    API_KEY = os.getenv("COHERE_API_KEY")
    MODEL_ID = os.getenv("COHERE_MODEL_ID")

class CohereClassification(Cohere):
    def __init__(self, message):
        self.message = message
    
    def get(self):
        response = {}
        co = cohere.Client(self.API_KEY)
        response = co.classify(model=self.MODEL_ID, inputs=[self.message])
        label = response[0].prediction
        confidence = response[0].confidence
        if label != "0":
            return f"This message seems dangerous, be carefull, the system gives {confidence}% of confidence"
        else:
            return f"This message seems good, the system gives {confidence}% of confidence"
