# %% 
import os
from huggingface_hub import InferenceClient
from smolagents import LiteLLMModel #type: ignore
from litellm import completion #type: ignore
from dotenv import load_dotenv
load_dotenv()

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
HF_TOKEN = os.environ.get("HF_TOKEN")

model="claude-3-sonnet-20240229",

messages=[
    {"role": "system", "content": "You are Claude, a helpful AI assistant created by Anthropic."},
    {"role": "user", "content": "Tell me about yourself in three sentences."}
]

client = InferenceClient(
    base_url="https://api.anthropic.com/v1",
    api_key=ANTHROPIC_API_KEY  # Your Anthropic API key
)

response = client.chat.completions.create(
    model="claude-3-sonnet-20240229",  # Specify the Claude model version
    messages=messages,
    max_tokens=1000,
    temperature=0.7,
)

# Print the response
print(response.choices[0].message.content)


# %% [markdown]
# ## Using Ollama local model

messages=[
    {"role": "system", "content": "You are an Ollama local model, a helpful AI assistant."},
    {"role": "user", "content": "Tell me about yourself in three sentences."}
]

# %% [markdown]
# ### Using the `smolagents` library to connect to Ollama
# %%
model_id = "ollama_chat/deepseek-r1:32b"
model = LiteLLMModel(
    model_id=model_id,  # Or try other Ollama-supported models
    api_base="http://127.0.0.1:11434",  # Default Ollama local server
    num_ctx=8192,
)
response = model.chat(
    messages=messages,
    max_tokens=1000,
    temperature=0.7,
)
# Print the response
print(response.choices[0].message.content)

# %% [markdown]
# ### Using the `litellm` library to connect to Ollama
# %%
response = completion(
    model=model_id,
    messages=messages,
    api_base="http://localhost:11434"
)

# %%
# Print the response
print(response.choices[0].message.content)