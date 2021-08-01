def mean(num):
    sum = 0
    for n in num:
        sum += n
    m = sum / len(num)

    return m


def dev(num, mean):
    sdev = 0
    for n in num:
        sdev = sdev + (n - mean) ** 2
    d = pow(sdev / (len(num) - 1), 0.5)

    return d


def get_yields(close):
    y = list()
    for i in range(len(close) - 1):
        temp = (close[i + 1] - close[i]) / close[i] * 100
        y.append(round(temp, 2))
    print('每个月的收益率（%）分别为： ', y)

    return y


def total_return(unit_return, period):
    period_return = pow(1 + unit_return, period) - 1

    return period_return


if __name__ == "__main__":
    p = [581.4, 679.5367, 743.9922, 841.5278, 959.7865, 877.0123, 984, 972.6, 1142, 1150, 1180.01, 1129, 1183]
    rf = 3
    r = get_yields(p)
    totol_return = (p[-1] - p[0]) / p[0] * 100

    Sharp_Ratio = (totol_return - rf) / (dev(r, mean(r)) * pow(12, 0.5))

    print("资产p的夏普比率为：{:.4f}".format(Sharp_Ratio))

    print(total_return(0.01, 72))