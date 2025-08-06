from llama_cpp import Llama
import os

# Load model only once
llm_model = None


def load_model():
    global llm_model
    if llm_model is None:
        llm_model = Llama(
            model_path=os.path.join("models", "Llama-3.2-3B-Instruct-Q4_0.gguf"),
            n_ctx=4096,
            n_threads=6,
            n_batch=512,
            verbose=False,
        )
    return llm_model


def generate_ai_summary(prompt):
    try:
        llm = load_model()
        output = llm(prompt, max_tokens=300, stop=["</s>"])
        return output["choices"][0]["text"].strip()
    except Exception as e:
        return f"[LLM Error] {str(e)}"
