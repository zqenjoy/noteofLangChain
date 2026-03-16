from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage , SystemMessage , AIMessage

chat = ChatTongyi(model="qwen3-max")

# message = [
# HumanMessage(content="给我写一首唐诗"), #提问prompt
# ]
#
# for chunk in chat.stream(input=message):
#     print(chunk.content,end='', flush=True)

# 注意这个使用的是chunk.content获取内容


# messages = [
# SystemMessage(content="你是一位来自边塞的诗人"), #系统设定
# HumanMessage(content="给我写一首唐诗"), #提问prompt
# AIMessage(content="鹅鹅鹅,曲项向天歌,白毛浮绿水,红掌拨清波"),
# HumanMessage(content="按照你上一个回复,给我再写一首唐诗"), #提问prompt
# ]
#
# res=chat.stream(input=messages)
# for chunk in res:
#     print(chunk.content,end='', flush=True)



ollamaChat = ChatOllama(model="qwen3:4b")

# messages = [
# SystemMessage(content="你是一位来自边塞的诗人"), #系统设定
# HumanMessage(content="给我写一首唐诗"), #提问prompt
# AIMessage(content="鹅鹅鹅,曲项向天歌,白毛浮绿水,红掌拨清波"),
# HumanMessage(content="按照你上一个回复,给我再写一首唐诗"), #提问prompt
# ]

# 消息的简写形式
messages = [
("system","你是一位来自边塞的诗人"), #系统设定
("human","给我写一首唐诗"), #提问prompt
('assistant',"鹅鹅鹅,曲项向天歌,白毛浮绿水,红掌拨清波"),
('human',"按照你上一个回复,给我再写一首唐诗"), #提问prompt
]

res=ollamaChat.stream(input=messages)
for chunk in res:
    print(chunk.content,end='', flush=True)
