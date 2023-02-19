from openai import Embedding

class OpenAIClient():
    EMBEDDING_MODEL = "text-embedding-ada-002"

    def get_embedding(text: str, model: str=EMBEDDING_MODEL) -> list[float]:
        result = Embedding.create(
                model=model,
                input=text
            )
        return result["data"][0]["embedding"]




