from langchain.agents.middleware import wrap_tool_call, before_model
from langchain_core.messages import ToolMessage
from typing import Callable
from langchain.tools.tool_node import ToolCallRequest
from langgraph.types import Command
from utils.logger_handler import logger


@wrap_tool_call
def monitor_tool(
        request:ToolCallRequest,#请求数据封装
        # 执行函数本身
        handler:Callable[[ToolCallRequest],ToolMessage  | Command]
)->ToolMessage|Command: #工具执行监控
    logger.info(f"[monitor_tool]执行工具：{request.tool_call['name']}")
    logger.info(f"[monitor_tool]执行参数：{request.tool_call['args']}")

    try:
        result =  handler(request)
        logger.info(f"[monitor_tool]工具：{request.tool_call['name']}调用成攻")
        return result
    except Exception as e:
        logger.error(f"[monitor_tool]工具：{request.tool_call['name']}调用失败，失败原因：{str(e)}")
        raise e

@before_model
def log_before_model(
        state:AgentState, #整个agent之智能体中的状态记录
        runtime:Runtime,  #级整个执行过程中的上下文信息
):
    logger.info(f"[log_before_model]即将调用模型，带有{len(state['messages'])}条消息。")

    logger.debug(f"[log_before_model]消息内容：{type(state['messages'][-1].__name__)}|{state['messages'][-1].content.strip()}")
    return None

def report_prompt_switch():# 动态切换提示词
    pass
