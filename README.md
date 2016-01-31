# portfolio-rebalancer

A Python module to handle portfolio rebalancing. Each portfolio has a set of investments and target allocations for these investments. As share prices fluctuate, the actual allocations diverge from the target allocations. `portfolio-rebalancer` calculates the set of buys and sells required to rebalance the investments.

## Usage

Use the method `get_buys_and_sells` with a list of dicts representing the current state of investments including fields `ticker`, `target_allocation`, `actual_allocation`, `shares_owned`, and `share_price`. The output will be a list of strings representing the set of buys and sells necessary to rebalance the investments.

```
>>>investments = [
  {
    'share_price': 98,
    'target_allocation': 0.6,
    'ticker': 'GOOG',
    shares_owned': 52,
    'actal_allocation': 0.5096
  }, {
    'share_price': 22,
    'target_allocation': 0.3,
    'ticker': 'AAPL',
    'shares_owned': 136,
    'actal_allocation': 0.2992
  }, {
    'share_price': 8,
    'target_allocation': 0.1,
    'ticker': 'TSLA',
    'shares_owned': 239,
    'actual_allocation': 0.1912
  }
]

>>> rebalancer.get_buys_and_sells(investments)
[u'buy 9 shares of GOOG', u'sell 114 shares of TSLA']

```

## Technical Choices

I chose Python for its minimal boilerplating. I used [py.test](http://pytest.org/latest/) for automated testing due to my familiarity with the framework.

## Trade-offs

I broke out formatting into a helper method called `_format_buys_and_sells` as I make the assumption that string formatting is for the benefit of user experience. Changing the code to interface better with an automated buying or selling module would be easy as the formatting code is not coupled with the calculations. However, this slows performance as another traversal of the list of investments is required to build this formatted list. It still takes linear time but perhaps the difference between `n` and `2n` matters. If so, the algorithm could be refactored as shown below to build the string array in the same loop as the difference calculation, reducing to a single traversal.

```
for i in investments:
  diff = ... # same as current code

  if diff > 0:
    instructions.append("buy " + ...)
  elif diff < 0:
    instructions.append("sell " + ...)

return instructions
```
