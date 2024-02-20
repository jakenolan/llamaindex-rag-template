# llamaindex-rag-template

<br />

A simple RAG chatbot template for starting a new LLM application. This template makes use of LlamaIndex and OpenAI. Specifically, this template is made using ReActAgent from LlamaIndex, which is an agent that you can create custom tools for to query or manipulate your data.

<br />

### Template Changes

First, fill the empty string below with your API key
```python
openai.api_key = ""
```

<br />

Next, replace all occurences of <topic> with whatever topic your application is about. See snips below.
```python
...
name="<topic>_data",
description="Provides information about <topic>. Use a detailed plain text question as input to the tool."
...

...
context = """\
You are an expert in all information that has to do with <topic>. \
You will answer questions about <topic> as in the persona of a very knowledgeable expert. \
"""
...
```
