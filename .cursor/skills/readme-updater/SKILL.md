---
name: readme-updater
description: Analyze the `项目` directory and regenerate `项目/README.md` with current architecture, configuration, and run instructions. Use when updating project code, before git commits, or when README needs synchronization with implementation.
---

# README Updater

## Purpose

Keep `项目/README.md` aligned with the actual code structure and config in `项目/`.

## When To Use

- Before every git commit.
- After adding/removing modules under `项目/`.
- After changing tools, prompts, config files, or startup path.
- When user asks to update project documentation.

## Required Actions

1. Run:
   - `python .cursor/skills/readme-updater/scripts/update_readme.py`
2. Verify `项目/README.md` is updated.
3. Stage README changes before commit.

## Update Rules

- Keep documentation in Chinese.
- Only describe capabilities that exist in code.
- Ensure these sections exist:
  - 项目简介
  - 主要能力
  - 项目结构
  - 核心流程
  - 环境与依赖
  - 配置说明
  - 运行方式
  - 自动化说明
  - 已知注意点
- Mention hook path `.githooks/pre-commit`.

## Notes

- Source of truth is code under `项目/` and yaml under `项目/config/`.
- If script fails, stop commit and fix script/config first.
