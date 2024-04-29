import os

# api keys
os.environ["ANTHROPIC_API_KEY"] = ""
os.environ["TAVILY_API_KEY"] = ""

# model selection
model = "claude-3-haiku-20240307"
# model = "claude-3-sonnet-20240229"
# model = "claude-3-opus-20240229"

max_tokens = 1024
temperature = None
