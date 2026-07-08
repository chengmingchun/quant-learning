import pandas as pd

from src.returns import simple_returns


def test_simple_returns() -> None:
    prices = pd.Series([100.0, 105.0, 103.95])

    returns = simple_returns(prices)

    assert returns.tolist() == [0.05, -0.01]
