def construct_prompt(question: str, context: str) -> str:
    """
    Add header and formulate a good prompt
    """
    
    header = """Answer the question as truthfully as possible using the provided context, and if the answer is not contained within the text below, say "I don't know.". \n\nContext:\n"""
    
    return header + "".join(context) + "\n\n Q: " + question + "\n A:"

