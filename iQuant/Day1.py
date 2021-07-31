# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def stock_buy():
    stock_price = eval(input('请输入股票单价：'))
    cash = eval(input('请输入购入股票的金额：'))

    # stock_price = eval(stock_price_str)
    # cash_str = eval(cash_str)
    mini_amount = 100
    unit_price = stock_price * mini_amount

    if cash < unit_price:
        print("资金不足，无法购入一手股票")
    else:
        share = cash // unit_price * mini_amount
        print("可以购入{}股{}股票".format(share, unit_price))


def limit_updown():
    close_price = float(input("请输入股票昨日收盘价："))
    # close_price = price;
    limit_up_price = close_price * (1 + 0.1)
    limit_up_price = myround(limit_up_price, 2)

    limit_down_price = close_price * (1 - 0.1)
    limit_down_price = myround(limit_down_price, 2)

    print("涨停价：{:.2f}, 跌停价：{:.2f}".format(limit_up_price, limit_down_price))


def myround(base, numofbit):
    amp = 10 ** (numofbit + 1)
    base = base * amp
    if str(base).split(".")[0][-1] == str(5):
        base += 5
    base = base / amp
    result = float(round(base, numofbit))
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stock_buy()
    limit_updown()

