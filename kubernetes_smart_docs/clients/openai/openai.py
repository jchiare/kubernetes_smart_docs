from openai import Completion, Embedding

class OpenAIClient():
    COMPLETIONS_MODEL = "text-davinci-003"
    TESTING_COMPLETIONS_MODEL = "text-curie-001"
    EMBEDDING_MODEL = "text-embedding-ada-002"
    
    def get_completion(prompt: str, model: str=TESTING_COMPLETIONS_MODEL) -> list[float]:
        response = Completion.create(
                prompt=prompt,
                temperature=0.0,
                max_tokens=300,
                model=model,
            )
        return response["choices"][0]["text"].strip(" \n")

    def get_embedding(text: str, model: str=EMBEDDING_MODEL) -> list[float]:
        result = Embedding.create(
            model=model,
            input=text
            )
        return result["data"][0]["embedding"]




