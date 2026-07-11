import pandas as pd

from src.returns import annualized_volatility, cumulative_returns, max_drawdown, simple_returns


def test_simple_returns() -> None:
    prices = pd.Series([100.0, 105.0, 103.95])

    returns = simple_returns(prices)

    assert returns.round(4).tolist() == [0.05, -0.01]


def test_cumulative_returns() -> None:
    returns = pd.Series([0.10, -0.05, 0.20])

    result = cumulative_returns(returns)

    assert result.round(4).tolist() == [0.10, 0.045, 0.254]


def test_max_drawdown() -> None:
    equity_curve = pd.Series([1.00, 1.20, 1.10, 1.30, 1.00])

    result = max_drawdown(equity_curve)

    assert round(result, 4) == -0.2308


def test_annualized_volatility() -> None:
    returns = pd.Series([0.01, -0.02, 0.03, -0.01])

    result = annualized_volatility(returns, periods_per_year=252)

    assert round(result, 4) == 0.3520
