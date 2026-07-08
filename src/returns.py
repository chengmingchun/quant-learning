"""Return calculation helpers."""

from __future__ import annotations

import pandas as pd


def simple_returns(prices: pd.Series) -> pd.Series:
    """Calculate simple period returns from a price series."""
    return prices.pct_change().dropna()
