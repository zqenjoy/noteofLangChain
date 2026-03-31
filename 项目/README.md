# 智能扫地机器人客服（ReAct + RAG）

本项目是一个面向扫地/扫拖机器人场景的中文智能客服系统，使用 Streamlit 搭建交互界面，基于 LangChain Agent 实现 ReAct 工具调用，并结合 Chroma 向量库完成知识检索总结与报告生成场景支持。

## 主要能力

- ReAct 智能体：按需调用工具完成回答。
- RAG 检索总结：对本地知识文件进行检索与归纳。
- 报告模式切换：通过中间件在报告场景切换专用提示词。
- 流式响应：前端按流式分片展示模型输出。
- 调用日志：记录模型和工具执行信息，便于排错。

## 项目结构

- `app.py`: Streamlit 主入口（ReAct Agent）（OK）
- `agent/react_agent.py`: Agent 封装与流式执行（OK）
- `agent/tools/agent_tools.py`: 业务工具集合（OK）
- `agent/tools/middleware.py`: 工具监控与动态提示词切换（OK）
- `rag/vector_store.py`: 向量库构建与检索器（OK）
- `rag/rag_service.py`: 检索总结服务（OK）
- `model/factory.py`: 模型工厂（OK）
- `config/`: 配置目录（OK）
- `prompts/`: 提示词目录（OK）
- `data/`: 知识与外部数据（OK）
- `utils/`: 通用工具（OK）
- `logs/`: 运行日志（OK）

## 核心流程

1. `streamlit run 项目/app.py` 启动 Web 聊天页面。  
2. 用户输入后，`agent/react_agent.py` 驱动 `create_agent(...).stream(...)`。  
3. 智能体按提示词与上下文调用工具（RAG、天气、用户信息、外部数据等）。  
4. `agent/tools/middleware.py` 负责工具监控与报告上下文注入。  
5. 若上下文标记为报告场景，动态切换为 `prompts/report_prompt.txt`。  
6. 最终回答在页面流式展示，并写入会话历史。  

## 环境与依赖

- Python 3.10+
- 建议依赖：
  - `streamlit`
  - `langchain`
  - `langchain-community`
  - `langchain-chroma`
  - `langchain-text-splitters`
  - `pyyaml`
- 需具备通义模型访问能力（`ChatTongyi` / `DashScopeEmbeddings`）。

## 配置说明

- 聊天模型：`qwen3-max`
- 向量模型：`text-embedding-v4`
- Chroma 集合：`agent`
- 向量库目录：`chroma_db`
- 检索 Top-K：`3`
- 外部数据文件：`data/external/records.csv`

## 数据概览

- `data/*.txt`：5 个
- `data/*.pdf`：1 个
- `logs/*.log`：44 个

## 运行方式

```bash
streamlit run 项目/app.py
```

可选：手动构建/更新向量库

```bash
python 项目/rag/vector_store.py
```

## 自动化说明（提交前更新 README）

仓库包含一个项目级 skill：

- `.cursor/skills/readme-updater/SKILL.md`

对应 git hook：

- `.githooks/pre-commit`

每次 `git commit` 前会自动执行：

```bash
python .cursor/skills/readme-updater/scripts/update_readme.py
git add 项目/README.md
```

## 已知注意点

- `fetch_external_data` 的类型注解与实际返回类型存在差异（注解为 `str`，成功时返回字典）。
- 当前项目未提供 `requirements.txt`，建议补齐以便环境复现。
- 向量文件 md5 记录逻辑可进一步增强为追加式或结构化持久化。
