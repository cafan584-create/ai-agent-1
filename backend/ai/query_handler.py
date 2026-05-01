from backend.ai.prompt_templates import USER_QUERY
from backend.ai.narrative_engine import call_groq

def answer_question(question: str, context: dict = None) -> str:
    context_str = ""
    if context:
        for k, v in context.items():
            context_str += f"- {k}: {v}\n"

    prompt = USER_QUERY.format(question=question, context=context_str or "No data available")
    return call_groq(prompt)
