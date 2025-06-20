import os
from llama_cpp import Llama

# Set the path to the GGUF model file
MODEL_PATH = os.path.join("models", "Q4_K_M-00001-of-00001.gguf")

# Load the model
llm = Llama(model_path=MODEL_PATH, n_ctx=2048)

def generate_code_from_prompt(prompt):
    full_prompt = f"### Python code to do the following task:\n{prompt}\n### Code:\n"
    response = llm(full_prompt, max_tokens=512, stop=["###", "```"])
    return response["choices"][0]["text"]

def save_code(prompt, code):
    filename = prompt[:30].replace(" ", "_").replace("?", "") + ".py"
    path = os.path.join("output", filename)
    with open(path, "w") as f:
        f.write(code)
    print(f"\n✅ Code saved to {path}")
