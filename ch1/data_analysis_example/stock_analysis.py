# pandas module
import pandas as pd

def get_mean_tv_cp(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    return df['Trade_Volume'].mean(), df['Closing_Price'].mean()

def main():
    for symbol in ['2330', '2454', '2498']:
        print (symbol + " Mean Closing_Price" + "Mean Trade Volume")
        mean_trade_volume, mean_closing_price = get_mean_tv_cp(symbol)
        print (mean_trade_volume, mean_closing_price)

if __name__ == "__main__":
    main()