from langchain.agents import create_agent,AgentState
from langchain.agents.middleware import before_agent, before_model, after_agent, after_model, wrap_model_call, \
    wrap_tool_call
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool
from langgraph.runtime import Runtime


@tool(description="查询天气，传入城市名称，返回城市的天气")
def get_weather(city)->str:
    return "晴天"


@before_agent
def log_before_agent(state:AgentState,runtime:Runtime)->None:
    print(f"[before agent]agent启动,附带上{len(state["messages"])}消息")

@after_agent
def log_after_agent(state:AgentState,runtime:Runtime)->None:
    print(f"[after agent]agent结束,附带上{len(state["messages"])}消息")

@before_model
def log_before_model(state:AgentState,runtime:Runtime)->None:
    print(f"[before model]模型即将调用,附带上{len(state["messages"])}消息")

@after_model
def log_after_model(state:AgentState,runtime:Runtime)->None:
    print(f"[after model]模型即将停止,附带上{len(state["messages"])}消息")

@wrap_model_call
def wrap_model_hook(request,handler):
    print('模型调用啦')
    return handler(request)


@wrap_tool_call
def wrap_tool_hook(request,handler):
    print(f"工具执行：{request.tool_call['name']}")
    print(f"工具执行传入参数：{request.tool_call['args']}")
    return handler(request)


agent = create_agent(
    model=ChatTongyi(model="qwen3-max"), #llm  qwen3-max"无法查询天气，所以需要我告诉它去调用工具查询天气
     tools=[get_weather],
    middleware=[log_before_agent,log_after_agent,log_before_model,log_after_model,wrap_model_hook,wrap_tool_hook],
    system_prompt="你是一个聊天助手，能回答用户的问题"
)

# invoke输出
res = agent.invoke(
    {
        "messages":[
            {"role":"user","content":"明天南昌的天气如何？"}
        ]
    }
)
for msg in res["messages"]:
    print(type(msg).__name__,msg.content)

