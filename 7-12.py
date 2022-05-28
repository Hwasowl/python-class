def sumValue(*values, **kwargs):
    hap = 0
    for v in values:
        hap += v

    for key in kwargs:
        hap += kwargs[key]
    return hap

coffeePrice = { 'value': 2000, '에스프레소':2000,'아메리카노':2800,'카페라테':3200 }

print(sumValue(1, 2, 3, **coffeePrice))
print(sumValue(2, 3, 4, **coffeePrice))
