import time
import json
import requests
import pandas as pd
from urllib.parse import urlencode
import csv
import os.path
import numpy as np
from google_maps_api_alfaindo_oop import GooglePlaces

class get_data:
	def __init__(self, id_kota):
		self.id_kota = id_kota

	def get_daerah(self, tingkat_daerah, id):
		list_nama_daerah = []
		list_id_daerah = []
		if(tingkat_daerah=="kecamatan"):
			url_param = f"kecamatan?id_kota={id}"
		elif(tingkat_daerah=="kelurahan"):
			url_param = f"kelurahan?id_kecamatan={id}"

		url = f"http://dev.farizdotid.com/api/daerahindonesia/{url_param}"
		result = requests.get(url).json()
		dict_daerah = result[tingkat_daerah]
		for i in range(0, len(dict_daerah)):
			nama_daerah = dict_daerah[i]['nama']
			list_nama_daerah.append(nama_daerah)
			id_daerah = dict_daerah[i]['id']
			list_id_daerah.append(id_daerah)

		return list_nama_daerah, list_id_daerah

	def start_scraping(self):
		kecamatan = self.get_data_kecamatan()
		nama_kecamatan = kecamatan[0]
		id_kecamatan = kecamatan[1]
		for x in range(0,len(id_kecamatan)):
			kelurahan = self.get_data_kelurahan(id_kecamatan[x])

			print(nama_kecamatan[x])
			print(kelurahan[0])

			model = GooglePlaces(path, keyword, kelurahan[0], nama_kecamatan[x], kota, api_key, type)
			model.start()

			#return nama_kecamatan[x], kelurahan[0]

	def get_data_kecamatan(self):
		nama_kecamatan = self.get_daerah("kecamatan", self.id_kota)[0]
		id_kecamatan = self.get_daerah("kecamatan", self.id_kota)[1]
		return nama_kecamatan, id_kecamatan

	def get_data_kelurahan(self, id_kecamatan):
		nama_kelurahan = self.get_daerah("kelurahan", id_kecamatan)[0]
		id_kelurahan = self.get_daerah("kelurahan", id_kecamatan)[1]
		return nama_kelurahan, id_kelurahan


id = 3171
type = 1
keyword = 'Indomaret'
kota = "Jakarta Selatan"
api_key = 'xxx' # Api Key
path = f"D:/Yok Belajar/Analisis/Alfamart - Indomaret/get_data/"

x = get_data(id)
x.start_scraping()

# id 3171 jaksel
# 0. Ini manual http://dev.farizdotid.com/api/daerahindonesia/kota?id_provinsi=31, cari id
# 1. http://dev.farizdotid.com/api/daerahindonesia/kecamatan?id_kota=3171 {id_kota}, ini cari kecamatan
# 2. http://dev.farizdotid.com/api/daerahindonesia/kelurahan?id_kecamatan=3171010, ini cari kelurahan
# https://farizdotid.com/blog/dokumentasi-api-daerah-indonesia/