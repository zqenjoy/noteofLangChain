# agent需要的工具
from langchain_core.tools import tool
from rag.rag_summarize import RagSummarizeService

rag = RagSummarizeService()

# rag向量的总结服务
@tool(description="从向量存储中检索参考资料")
def rag_summarize(query)->str:
    return rag.rag_summarize(query)

@tool(description="获取指定城市的天气，以消息字符串的形式返回")
def get_weather(city:str)->str:
    return f"{city}天气为晴天，气温26摄氏度，空气湿度50%，南风一级，AQI21，最近六小时降雨概率极低"