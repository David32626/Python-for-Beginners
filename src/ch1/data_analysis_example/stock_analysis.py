# pandas module
import pandas as pd

def get_mean_tv_cp(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    return df['Trade_Volume'].mean(), df['Closing_Price'].mean()

def main():
    for symbol in ['TSMC', 'MTK', 'HTC']:
        print (symbol + ": ")
        mean_trade_volume, mean_closing_price = get_mean_tv_cp(symbol)
        print ("  Mean Closing_Price: ", mean_closing_price)
        print ("  Mean Trade Volume: ", mean_trade_volume)

if __name__ == "__main__":
    main()