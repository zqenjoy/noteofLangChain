from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool

@tool(description="查询天气")
def get_weather()->str:
    return "晴天"


@tool(description="获取股价，传入股票名称，返回字符串信息")
def get_price(name:str)->str:
    return f"股票{name}的价格是12元"

@tool(description="获取股票信息，传入股票名称，返回字符串信息")
def get_info(name:str)->str:
    return f"{name}是一家上市公司，专注于it教育"

agent = create_agent(
    model=ChatTongyi(model="qwen3-max"), #llm  qwen3-max"无法查询天气，所以需要我告诉它去调用工具查询天气
     tools=[get_price,get_info],
    system_prompt="你是一个聊天助手，能回答用户的问题"
)

# invoke输出
# res = agent.invoke(
#     {
#         "messages":[
#             {"role":"user","content":"明天南昌的天气如何？"}
#         ]
#     }
# )
# for msg in res["messages"]:
#     print(type(msg).__name__,msg.content)


# 流式输出
for chunk in agent.stream({
    "messages":[
        {"role":"user","content":"传智教育股价多少，并介绍一下"}
    ]
},stream_mode="values"):
    latest_msg=chunk["messages"][-1]
    # print(latest_msg)
    if latest_msg.content:
        print(type(latest_msg),latest_msg.content)
    try:
        if latest_msg.tool_calls:
            print(f"工具调用：{[tc["name"] for tc in latest_msg.tool_calls]}" )
    except AttributeError as e:
        pass

