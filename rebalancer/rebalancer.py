"""Calculates the buys and sells required to bring the actual allocation of
investments as close as possible to the target allocations.

Args:
  investments: a list of dicts representing each investment.

Returns:
  List of buys and sells required to rebalance given investments.

"""
def get_buys_and_sells(investments):
  return _format_buys_and_sells(zip(investments, _calculate_diffs(investments)))


def _calculate_diffs(investments):
  total = (investments[0]['share_price']*investments[0]['shares_owned']/
    investments[0]['actual_allocation'])

  return [int(round(i['target_allocation']*total)/i['share_price']) -
    i['shares_owned'] for i in investments]


def _format_buys_and_sells(diff):
  instructions = []
  for i in diff:
    if i[1] > 0:
      instructions.append("buy " + str(i[1]) + " shares of " + i[0]['ticker'])
    elif i[1] < 0:
      instructions.append("sell " + str(-1*i[1]) + " shares of " + i[0]['ticker'])

  return instructions
