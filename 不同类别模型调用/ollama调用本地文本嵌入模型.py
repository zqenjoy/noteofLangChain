from langchain_community.embeddings import DashScopeEmbeddings

# DashScopeEmbeddings中不传模式用的是text-embedding-v1模型
# model = DashScopeEmbeddings()

# print(model.embed_query('我喜欢你'))
# print(model.embed_documents(['我喜欢你','我稀饭你','我讨厌你']))


print('---------ollama本地嵌入模型---------------')

from langchain_ollama import OllamaEmbeddings

model = OllamaEmbeddings(model='qwen3-embedding:4b')
# print(model.embed_query('我喜欢你'))
print(model.embed_documents(['我喜欢你','我稀饭你','我讨厌你']))