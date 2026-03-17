from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser

str_parser = StrOutputParser()
json_parser=JsonOutputParser()
model = ChatTongyi(model="qwen3-max")

first_template = PromptTemplate.from_template("我叫{name}，我刚出生了一个{gender}孩子,请帮忙起名字,并封装成json返回。key为name，value为名字，请严格遵守规定的格式。")

second_template = PromptTemplate.from_template("姓名：{name},请帮我解释含义")

# 构建链
chain = first_template | model | json_parser | second_template | model |str_parser

res= chain.stream({"name":"黎明","gender":"女"})
for chunk in res:
    print(chunk,end="",flush=True)
# print(type(res))