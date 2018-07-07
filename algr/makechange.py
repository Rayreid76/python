def coins():
    coin=int(input('Please enter amount to make change:'))
    print(coin/25, "quarters")
    coin = coin%25
    print(coin/10, "dimes")
    coin = coin%10
    print(coin/5, "nickles")
    coin = coin%5
    print(coin/1, "pennies")

coins()
