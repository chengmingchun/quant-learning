# Quant Learning

用于记录量化交易学习过程的代码仓库：数据获取、因子研究、策略回测、风险评估和学习笔记。

## Repository Structure

```text
.
├── data/
│   ├── raw/          # 原始数据，不提交到 Git
│   └── processed/    # 清洗后的数据，不提交到 Git
├── docs/             # 学习笔记、概念整理、实验记录
├── notebooks/        # 探索性分析和研究草稿
├── src/              # 可复用代码
└── tests/            # 单元测试
```

## Suggested Learning Path

1. 市场数据基础：K 线、复权、成交量、收益率、波动率。
2. Python 数据分析：`pandas`、`numpy`、可视化和数据清洗。
3. 因子研究：动量、均值回归、估值、质量、情绪等。
4. 回测框架：信号、调仓、手续费、滑点、资金曲线和最大回撤。
5. 风险控制：仓位管理、组合暴露、止损、VaR 和压力测试。
6. 实盘准备：数据质量、交易接口、日志、监控和复盘。

## Getting Started

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
pytest
```

## Notes

- 不要提交真实 API key、账号信息或本地下载的数据。
- 大型数据集建议放在 `data/` 下并通过 `.gitignore` 排除。
- 研究代码先放 `notebooks/`，稳定后再整理进 `src/`。
