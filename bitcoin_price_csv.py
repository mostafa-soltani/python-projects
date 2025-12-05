import requests
import ast
import time
import csv
import os

url = 'https://api.diadata.org/v1/assetQuotation/Bitcoin/0x0000000000000000000000000000000000000000'

rqs = requests.get(url=url)
            

text = ast.literal_eval(rqs.text)  
symbol = text.get('Symbol')
name = text.get('Name')
blockchain = text.get('Blockchain')
price = text.get('Price')
ys_price = text.get('PriceYesterday')
time1 = text.get('Time')
print(text)

def update_price():
    try:
        while True:
            for i in range(1,10):
                rqs = requests.get(url=url)
            
                text = ast.literal_eval(rqs.text)
                symbol = text.get('Symbol')
                name = text.get('Name')
                blockchain = text.get('Blockchain')
                price = text.get('Price')
                ys_price = text.get('PriceYesterday')
                time1 = text.get('Time')

                print("Updated:")
                print(symbol, price)
                

                file_exitses = os.path.exists('bitcoin_price.csv')


                try:
                    with open('bitcoin_price.csv','a',newline='') as f:
                        writer = csv.writer(f)
                        if not file_exitses :
                            tils = []
                            for key in text.keys():
                                print(key)
                                tils.append(key)
                            writer.writerow(tils)
                            print('done')
                        tiit = []
                        for value in text.values():
                            tiit.append(value)
                        writer.writerow(tiit)
                        print('valu 1 done')

                except Exception as e:
                    print(f'error {e}')

                time.sleep(130)


    except Exception as e:
        print("Error:", e)

update_price()