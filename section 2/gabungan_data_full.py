

import pandas as pd


datas_1 = pd.read_csv("D:/Yok Belajar/Analisis/Alfamart - Indomaret/data_full_completed_Indomaret.csv")
datas_2 = pd.read_csv("D:/Yok Belajar/Analisis/Alfamart - Indomaret/section 2/df_places_id_Indomaret.csv")

datas_3 = pd.read_csv("D:/Yok Belajar/Analisis/Alfamart - Indomaret/data_full_completed_Alfamart.csv")
datas_4 = pd.read_csv("D:/Yok Belajar/Analisis/Alfamart - Indomaret/section 2/df_places_id_Alfamart.csv")

data_indomaret = pd.concat([datas_1, datas_2], axis=1)
data_alfamart = pd.concat([datas_3, datas_4], axis=1)

data_fixed = pd.concat([data_indomaret, data_alfamart], ignore_index=True)
data_fixed.drop(['distance'], axis=1, inplace=True)
print(data_fixed.shape)
data_fixed.drop_duplicates(subset=['latitude', 'place_id'], keep='first', inplace=True)
print(data_fixed.shape)
data_fixed.to_csv("DATA_JAKSEL_FIXED.csv", index=False)
