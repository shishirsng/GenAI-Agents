This is the Oracle course of Agentic AI

_**this readme is not AI **_

**L1:**

In the lesson L1 I have learned tool calling, API key, Langchain and its some components

API key used of : OPENROUTER , Currently model is set to auto (so it would pick any free model available with openrouter - probably the deepseek one)

Finally comes the part where I create agent invoke it and it takes input of questions and model calls the tool accordingly

another we have loop_context_chat where we have made a list named history where we store user and assistant history and it is how the LLM can know the context (ofc there would be much better solutions)


**L2**

This is L2 and here MCP is the boss so MCP acts a communication source of tool calling it has mainly three components i would say HOST , CLIENT , SERVER

MCP is more or less a tool-calling protocol; it helps the LLM choose the tool most relevant to the use case without requiring individual custom integrations for each source/API,

MCP uses JSON RPC 2.0 which means it can communicate locally and as well as on remote servers
