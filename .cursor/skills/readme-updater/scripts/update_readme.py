from __future__ import annotations

from pathlib import Path
import textwrap
import yaml


def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data


def count_files(path: Path, pattern: str) -> int:
    if not path.exists():
        return 0
    return len(list(path.glob(pattern)))


def build_tree_lines(project_dir: Path) -> list[str]:
    entries = [
        ("app.py", "Streamlit 主入口（ReAct Agent）"),
        ("agent/react_agent.py", "Agent 封装与流式执行"),
        ("agent/tools/agent_tools.py", "业务工具集合"),
        ("agent/tools/middleware.py", "工具监控与动态提示词切换"),
        ("rag/vector_store.py", "向量库构建与检索器"),
        ("rag/rag_service.py", "检索总结服务"),
        ("model/factory.py", "模型工厂"),
        ("config/", "配置目录"),
        ("prompts/", "提示词目录"),
        ("data/", "知识与外部数据"),
        ("utils/", "通用工具"),
        ("logs/", "运行日志"),
    ]
    lines: list[str] = []
    for rel, desc in entries:
        exists = (project_dir / rel).exists()
        status = "OK" if exists else "MISSING"
        lines.append(f"- `{rel}`: {desc}（{status}）")
    return lines


def build_readme(project_dir: Path) -> str:
    config_dir = project_dir / "config"
    rag_cfg = load_yaml(config_dir / "rag.yml")
    chroma_cfg = load_yaml(config_dir / "chroma.yml")
    agent_cfg = load_yaml(config_dir / "agent.yml")

    data_dir = project_dir / "data"
    txt_count = count_files(data_dir, "*.txt")
    pdf_count = count_files(data_dir, "*.pdf")
    logs_count = count_files(project_dir / "logs", "*.log")

    chat_model = rag_cfg.get("chat_model_name", "未配置")
    embedding_model = rag_cfg.get("embedding_model_name", "未配置")
    collection = chroma_cfg.get("collection_name", "未配置")
    persist_dir = chroma_cfg.get("persist_directory", "未配置")
    top_k = chroma_cfg.get("k", "未配置")
    external_path = agent_cfg.get("external_data_path", "未配置")

    tree = "\n".join(build_tree_lines(project_dir))

    return textwrap.dedent(
        f"""\
# 智能扫地机器人客服（ReAct + RAG）

本项目是一个面向扫地/扫拖机器人场景的中文智能客服系统，使用 Streamlit 搭建交互界面，基于 LangChain Agent 实现 ReAct 工具调用，并结合 Chroma 向量库完成知识检索总结与报告生成场景支持。

## 主要能力

- ReAct 智能体：按需调用工具完成回答。
- RAG 检索总结：对本地知识文件进行检索与归纳。
- 报告模式切换：通过中间件在报告场景切换专用提示词。
- 流式响应：前端按流式分片展示模型输出。
- 调用日志：记录模型和工具执行信息，便于排错。

## 项目结构

{tree}

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

- 聊天模型：`{chat_model}`
- 向量模型：`{embedding_model}`
- Chroma 集合：`{collection}`
- 向量库目录：`{persist_dir}`
- 检索 Top-K：`{top_k}`
- 外部数据文件：`{external_path}`

## 数据概览

- `data/*.txt`：{txt_count} 个
- `data/*.pdf`：{pdf_count} 个
- `logs/*.log`：{logs_count} 个

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
"""
    )


def main() -> int:
    repo_root = Path(__file__).resolve().parents[4]
    project_dir = repo_root / "项目"
    readme_path = project_dir / "README.md"

    if not project_dir.exists():
        raise FileNotFoundError(f"项目目录不存在: {project_dir}")

    content = build_readme(project_dir).strip() + "\n"
    readme_path.write_text(content, encoding="utf-8")
    print(f"README updated: {readme_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
