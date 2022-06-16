import pandas as pd
import urllib.parse
import os.path


main_path = f'D:/Yok Belajar/Analisis/Alfamart - Indomaret/get_data/Indomaret/'
kecamatan_list = os.listdir(main_path)

for kecamatan in kecamatan_list:
	kelurahan_list = os.listdir(main_path+kecamatan)
	print(kecamatan)
	list_data_gabugan = []
	for kelurahan in kelurahan_list:
		if "type" in kelurahan:
			print(kelurahan)
			url_kelurahan_1 = main_path+kecamatan+f'/{kelurahan}'
			data_1 = pd.read_csv(url_kelurahan_1)
			list_data_gabugan.append(data_1)

	kelurahan_list_2 = os.listdir(main_path+kecamatan+'/2/')
	list_data_gabugan_2 = []
	for kelurahan_2 in kelurahan_list_2:
		url_kelurahan_2 = main_path+kecamatan+'/2/'+kelurahan_2
		print(url_kelurahan_2)

		data_2 = pd.read_csv(url_kelurahan_2)
		list_data_gabugan.append(data_2)


	datas = pd.concat(list_data_gabugan, ignore_index=True)
	print(f"Data gabungan shape: {datas.shape}")
	datas.drop_duplicates(subset=['latitude', 'place_id'], keep='first', inplace=True)
	print(f"Data fixed duplicates shape: {datas.shape}")
	path_asli = main_path+kecamatan
	datas.to_csv(f"{path_asli}/datas_completed_{kecamatan}.csv", index=False)



