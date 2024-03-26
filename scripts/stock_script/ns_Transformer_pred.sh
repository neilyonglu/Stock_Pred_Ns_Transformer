python -u generate_30day_csv.py \
  --stop_date 20240326 \
  --gt 1 \

python -u run_pred.py \
  --is_training 0 \
  --root_path data/stock \
  --data_path data_30days.csv \
  --model_id stock01 \
  --model ns_Transformer \
  --data custom \
  --features M \
  --seq_len 30 \
  --label_len 0 \
  --pred_len 1 \
  --e_layers 16 \
  --d_layers 16 \
  --factor 3 \
  --enc_in 4 \
  --dec_in 4 \
  --c_out 4 \
  --gpu 0 \
  --des 'Exp_h256_l2' \
  --p_hidden_dims 256 256 \
  --p_hidden_layers 2 \
  --itr 1 \
  --do_predict \

python -u pred_30days.py \
  --real_prediction_dir ./results/stock01_ns_Transformer_custom_ftM_sl30_ll0_pl1_dm512_nh8_el16_dl16_df2048_fc3_ebtimeF_dtTrue_Exp_h256_l2_0/real_prediction.npy \

