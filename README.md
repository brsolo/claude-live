# Claude Live

One shortcoming of Anthropic's Claude AI assistant is it only has knowledge up until August 2023.

For example:

>User: Who did the commanders draft?
>
>Claude: Unfortunately, I don't have any specific information about who the Commanders drafted, since my knowledge cutoff is from August 2023 and the NFL draft likely happened after that in April 2024. As an AI assistant without updated >>data past August 2023, I can't provide details on events like the 2024 NFL draft that occurred after my training period. My role is to have natural conversations based on the information I was provided during training up until August 2023.

With ClaudeLive, this is fixed!

>User: Who did the commanders draft?
>
>ClaudeLive: Based on the context provided, the Washington Commanders made the following selections in the 2024 NFL Draft:
>
>1st Round, 2nd Overall Pick: Jayden Daniels, QB, LSU
>
>4th Round, 118th Overall Pick: Braeden Daniels, T, Utah
>
>The key details are:
>
>- The Commanders had the 2nd overall pick in the 2024 NFL Draft.
>
>- With that pick, they selected quarterback Jayden Daniels from LSU. Daniels had won the Heisman Trophy the previous season.
>
>- In the 4th round, with the 118th overall pick, the Commanders drafted offensive tackle Braeden Daniels from Utah.
>
>So in summary, the Commanders' top two draft picks in 2024 were quarterback Jayden Daniels and offensive tackle Braeden Daniels.

## Installation and usage

Download the repo using:

```
git clone https://github.com/brsolo/claude-live
```

Then, enter your Anthropic and Tavily API keys in [config.py](/claude-live/config.py) and select which model you'd like to use. To ask a question, use the command line. For example:

```
python claude-live.py "Who did the commanders darft?"
```
That's it! Let me know if you have any ideas around this project.

## Details of implementation

ClaudeLive uses LangChain and Tavily to build a retrieval augmented (RAG) pipeline.

Tavily provides a search API optimized for working with LLMs. The user's question is fed to Tavily via a retriever which returns with ten related documents.

Those documents along with the user's question is then fed to the LLM to produce a response.