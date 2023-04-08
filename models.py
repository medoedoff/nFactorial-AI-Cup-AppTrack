import os
import cohere

class Cohere:
    API_KEY = os.getenv("COHERE_API_KEY")
    MODEL_ID = os.getenv("COHERE_MODEL_ID")

class CohereClassification(Cohere):
    def __init__(self, message):
        self.message = message
    
    def get(self):
        co = cohere.Client(self.API_KEY)
        response = co.classify(model=self.MODEL_ID, inputs=self.message)
        return response.classifications
