from flask import Blueprint, request
from kubernetes_smart_docs.services.prompt import construct_prompt
from kubernetes_smart_docs.services.semantic_search import find_related_sections
from kubernetes_smart_docs.services.get_dataframe import create_dataframe_with_embedding
from kubernetes_smart_docs.services.completions import AI_response

reply_blueprint = Blueprint('reply', __name__, url_prefix='/api/reply')

@reply_blueprint.route('/', methods=(['POST']))
def ai_response():
    data = request.get_json()
    
    file = "kubernetes_smart_docs/data/embedding_result.csv"
    df = create_dataframe_with_embedding(file, 'Content Embedding')
    
    related_articles_result = find_related_sections(df, data['text'])
    parsed_related_articles = related_articles_result.loc[:,"Content"].to_numpy()
    
    prompt = construct_prompt(data['text'],parsed_related_articles)
    response = AI_response(prompt)
    
    print(f"Response from openAI API: {response}")
    
    return {'response':response,'sources':parsed_related_articles.tolist()}