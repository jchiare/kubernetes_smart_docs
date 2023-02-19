from openai.embeddings_utils import cosine_similarity
from kubernetes_smart_docs.clients.openai.openai import OpenAIClient

# search through the reviews for a specific product
def find_related_sections(df, text, n=2):
    text_embedding = OpenAIClient.get_embedding(
        text=text,
    )
    df["similarity"] = df['Content Embedding'].apply(lambda x: cosine_similarity(x, text_embedding))

    results = (
        df.sort_values("similarity", ascending=False)
        .head(n)
    )
    total_token_count = results['Content Token Count'].sum()

    print(results)
    # return the first result if there are a lot of tokens
    # .. to save $$ on the completions api endpoint
    if total_token_count > 2000:
        return results.head(1)

    return results


