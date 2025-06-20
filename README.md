# Scriptly 🧠🐍

Scriptly is a Python AI assistant that writes Python code based on your voice or text commands.

## Features:
- Voice or text-based prompts
- Code generation using OpenAI
- Code auto-saved to output folder



🔗 Download the Model (Required)
Scriptly uses a local .gguf model file to generate code. To run it:

Go to:
👉 https://huggingface.co/bartowski/codegemma-2b-GGUF/blob/main/codegemma-2b-Q4_K_M.gguf

Download this file:
codegemma-1.1-2b.Q4_K_M.gguf

Create a folder named models/ in your Scriptly directory (if not already there)

Place the downloaded .gguf file inside the models/ folder

Then run:

bash
Copy code
python main.py
