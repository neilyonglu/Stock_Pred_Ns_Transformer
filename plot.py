import matplotlib.pyplot as plt
import numpy as np

pred = np.load(r'results\stock01_ns_Transformer_custom_ftM_sl30_ll0_pl1_dm512_nh8_el16_dl16_df2048_fc1_ebtimeF_dtTrue_Exp_h256_l2_0\pred.npy').squeeze(1)
true = np.load(r'results\stock01_ns_Transformer_custom_ftM_sl30_ll0_pl1_dm512_nh8_el16_dl16_df2048_fc1_ebtimeF_dtTrue_Exp_h256_l2_0\true.npy').squeeze(1)

x = np.arange(383)
y_pred = pred[:, 1]
y_true = true[:, 1]
plt.plot(x, y_pred)
plt.plot(x, y_true)
plt.show()