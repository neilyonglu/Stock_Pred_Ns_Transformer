import pandas as pd
import requests
import pandas as pd
from datetime import datetime, timedelta
import argparse

def Get_Stock_Informations(stock_code, start_date, stop_date):
    information_url = ('http://140.116.86.242:8081/stock/' +
                       'api/v1/api_get_stock_info_from_date_json/' +
                       str(stock_code) + '/' +
                       str(start_date) + '/' +
                       str(stop_date)
                       )
    result = requests.get(information_url).json()
    if(result['result'] == 'success'):
        return result['data']
    return dict([])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generating 30 Days .csv')

    parser.add_argument('--stop_date', type=int, default=20240326, help='stop date(YYYYMMDD)')
    parser.add_argument('--gt', type=bool, default=1, help='Ground Truth')
    args = parser.parse_args()
    
    stop_date_obj = datetime.strptime(str(args.stop_date), "%Y%m%d") # 将 stop_date 转换为 datetime 对象
    start_date_obj = stop_date_obj - timedelta(days=70)
    start_date = int(start_date_obj.strftime("%Y%m%d")) # 将 start_date_obj 转换为整数格式
    stop_date = int(stop_date_obj.strftime("%Y%m%d")) # 将 stop_date_obj 转换为整数格式

    print(f"Start date: {start_date}")
    print(f"Stop date: {stop_date}")
    
    #讀取股票資訊
    stock_code = 2330
    data = Get_Stock_Informations(stock_code, start_date, stop_date)

    # 指定 JSON 檔案的資料結構
    df = pd.DataFrame(data)
    df.sort_values("date", inplace=True)
    
    df.drop('stock_code_id', axis=1, inplace=True)

    if args.gt == 1:
        start_value = len(df) - 31
    else:
        start_value = len(df) - 30
        
    data_30_days = df.iloc[start_value:(start_value + 30), :]
    ground_value = df.iloc[(start_value + 30):(start_value + 31), :]

    print(data_30_days.to_string())

    data_30_days.to_csv(r'data\stock\data_30days.csv', index=False)
    ground_value.to_csv(r'data\stock\data_D31_groundtruth.csv', index=False)