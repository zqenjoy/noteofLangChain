from langchain_community.llms.tongyi import Tongyi
from langchain_ollama import OllamaLLM

# llms = Tongyi(model="qwen-max")
#
# res= llms.invoke(input="你是什么模型？什么类型的模型？")

# print('这是使用invoke调用llm------》/n',res)



model=OllamaLLM(model="qwen3:4b")
# res=model.invoke(input="你是什么模型？什么类型的模型？")
res= model.stream(input="你是什么模型？什么类型的模型？")# 流式输出，返回时类型为list，for循环输出
for chunk in res:
    print(chunk,end="",flush=True)

