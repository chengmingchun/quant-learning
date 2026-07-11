"""Return calculation helpers."""

from __future__ import annotations

import pandas as pd


def simple_returns(prices: pd.Series) -> pd.Series:
    """Calculate simple period returns from a price series."""
    return prices.pct_change().dropna()


def cumulative_returns(returns: pd.Series) -> pd.Series:
    """Calculate cumulative returns from period returns."""
    return (1 + returns).cumprod() - 1


def max_drawdown(equity_curve: pd.Series) -> float:
    """Calculate the maximum drawdown from an equity curve."""
    running_peak = equity_curve.cummax()
    drawdown = equity_curve / running_peak - 1
    return float(drawdown.min())


def annualized_volatility(returns: pd.Series, periods_per_year: int = 252) -> float:
    """Calculate annualized volatility from period returns."""
    return float(returns.std(ddof=1) * periods_per_year**0.5)
