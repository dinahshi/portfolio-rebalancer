import json

from rebalancer import rebalancer

def test_get_buys_and_sells():
  with open('data.json') as data:
    test_data = json.load(data)
    assert (rebalancer.get_buys_and_sells(test_data['investments']) ==
      ['buy 9 shares of GOOG', 'sell 114 shares of TSLA'])

def test_get_buys_and_sells_no_change():
  with open('balanced_data.json') as data:
    test_data = json.load(data)
    assert (rebalancer.get_buys_and_sells(test_data['investments']) == [])
