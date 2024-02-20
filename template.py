import os
import openai
from llama_index.llms import OpenAI
from llama_index.agent import ReActAgent
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

openai.api_key = ""

PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    try:
        documents = SimpleDirectoryReader(input_dir="data").load_data()
        index = VectorStoreIndex.from_documents(documents=documents)
        index.storage_context.persist()
    except Exception as e:
        print(f"Error setting up storage and/or loading index from newly created storage: {e}")
else:
    try:
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context=storage_context)
    except Exception as e:
        print(f"Error loading index from existing storage: {e}")

try:
    query_engine = index.as_query_engine(similarity_top_k=3)
    query_engine_tools = [
        QueryEngineTool(
            query_engine=query_engine,
            metadata=ToolMetadata(
                name="<topic>_data",
                description="Provides information about <topic>. Use a detailed plain text question as input to the tool."
            ),
        ),
    ]
    llm = OpenAI(model="gpt-3.5-turbo")
    context = """\
    You are an expert in all information that has to do with <topic>. \
    You will answer questions about <topic> as in the persona of a very knowledgeable expert. \
    """
    agent = ReActAgent.from_tools(
        tools=query_engine_tools,
        llm=llm,
        verbose=True, # Optional
        context=context,
    )
except Exception as e:
    print(f"Error setting up agent/tools: {e}")

agent.chat_repl()