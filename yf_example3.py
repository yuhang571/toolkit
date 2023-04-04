"""The purpose of the yf_example3 module is to download stock price data for
 Qantas for a given year and save the information in a CSV file."""
import os
import toolkit_config as cfg
import yf_example2
def qan_prc_to_csv(year):
    start = f"{year}-01-01"
    end = f"{year}-12-31"
    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    df= yf_example2.yf_prc_to_csv("QAN.AX",pth,start,end)
if __name__ == "__main__":
    qan_prc_to_csv(2020)