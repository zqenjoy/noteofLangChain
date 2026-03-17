from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.runnables import RunnableLambda

str_parser = StrOutputParser()
json_parser=JsonOutputParser()
model = ChatTongyi(model="qwen3-max")

first_template = PromptTemplate.from_template("我叫{name}，我刚出生了一个{gender}孩子,请帮忙起名字，仅告诉我名字，不需要其他信息")

second_template = PromptTemplate.from_template("姓名：{name},请帮我解释含义")

my_func =RunnableLambda(lambda ai_msg:{"name":ai_msg.content})

chain = first_template | model | my_func | second_template | model | str_parser

res=  chain.stream({"name":'李木子',"gender":"男"})

for chunk in res:
    print(chunk,end="", flush=True)


