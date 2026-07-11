# 01 - Returns and Risk

量化研究的第一步不是预测，而是把收益和风险算清楚。

## Core Concepts

- **Simple return**: 单期收益率，公式为 `price_t / price_{t-1} - 1`。
- **Cumulative return**: 多期复合收益，公式为 `(1 + r_1) * ... * (1 + r_n) - 1`。
- **Volatility**: 收益率的标准差，常用年化波动率衡量风险。
- **Max drawdown**: 从历史高点回落到低点的最大跌幅，衡量持有过程中的痛感。

## Practice

1. 准备一列价格数据。
2. 用 `simple_returns` 转换成收益率。
3. 用 `cumulative_returns` 查看资金曲线收益。
4. 用 `annualized_volatility` 和 `max_drawdown` 观察风险。

## Questions

- 同样的年化收益下，哪个策略的最大回撤更小？
- 最大回撤发生在什么时候？
- 如果加入手续费和滑点，收益曲线会变成什么样？
