import pandas as pd
import argparse
import numpy as np
import pandas as pd
import numpy as np

def rmse(y_true, y_pred):
    # 計算預測誤差
    errors = y_pred - y_true
    # 計算均方誤差
    mse = np.mean(errors**2)
    # 計算 RMSE
    rmse = np.sqrt(mse)
    return rmse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generating 30 Days .csv')

    parser.add_argument('--real_prediction_dir', type=str, default='./results/stock01_ns_Transformer_custom_ftM_sl30_ll0_pl1_dm512_nh8_el16_dl16_df2048_fc3_ebtimeF_dtTrue_Exp_h256_l2_0/real_prediction.npy', help='real_prediction.npy dir')
    args = parser.parse_args()
    
    data_30_days = pd.read_csv(r'data\stock\data_30days.csv')
    ground_value = pd.read_csv(r'data\stock\data_D31_groundtruth.csv')
    
    cols = 'date','capacity','turnover','change','transaction_volume'
    for col in cols:    
        data_30_days.drop(col, axis=1, inplace=True)
        ground_value.drop(col, axis=1, inplace=True)
        
    data_np = data_30_days.to_numpy()
    mean = np.mean(data_np, axis=0)
    std = np.std(data_np, axis=0)

    pre_path = str(args.real_prediction_dir)
    pred_np = np.load(pre_path)
    pred = pred_np * std + mean
    pred = pred.reshape(1,4)
    print('Prediction', pred)
    ground_value_np = ground_value.to_numpy()
    
    try: 
        print('Ground Value', ground_value_np)
        pred_np = pred_np.reshape(1,4)
        ground_value_np =  (ground_value_np - mean)/std
        rmses = []
        for i in range(4):
            rmses.append(rmse(ground_value_np[0][i], pred_np[0][i]))

        print('RMSE', rmses)
    
    except:
        print('No Ground Truth.')