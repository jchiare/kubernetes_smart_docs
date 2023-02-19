from kubernetes_smart_docs.clients.openai.openai import OpenAIClient

def AI_response(prompt):
    response = OpenAIClient.get_completion(prompt)
    return response