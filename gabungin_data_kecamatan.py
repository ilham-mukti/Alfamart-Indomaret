import pandas as pd
import urllib.parse
import os.path


main_path = f'D:/Yok Belajar/Analisis/Alfamart - Indomaret/get_data/Alfamart/'
kecamatan_list = os.listdir(main_path)

list_data_kecamatan = []
for kecamatan in kecamatan_list:
	url_kecamatan = f'{main_path}{kecamatan}/datas_completed_{kecamatan}.csv'
	data_mentah = pd.read_csv(url_kecamatan)
	data_mentah['store'] = "Alfamart"
	list_data_kecamatan.append(data_mentah)

datas = pd.concat(list_data_kecamatan, ignore_index=True)
print(datas.shape)
datas.drop_duplicates(subset=['latitude', 'place_id'], keep='first', inplace=True)
datas.to_csv('data_full_completed_Alfamart.csv', index=False)
print(datas.shape)