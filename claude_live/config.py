import os

# api keys
os.environ["ANTHROPIC_API_KEY"] = (
    "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"
)
os.environ["TAVILY_API_KEY"] = "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"

# model selection
model = "claude-3-haiku-20240307"
# model = "claude-3-sonnet-20240229"
# model = "claude-3-opus-20240229"

max_tokens = 1024
temperature = None
