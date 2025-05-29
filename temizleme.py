import pandas as pd
import numpy as np

#dosyayı okuyacağım
df = pd.read_csv('ilkbinsirket_clean.csv')
df['change_in_rank'] = pd.to_numeric(df['change_in_rank'], errors='coerce')
#change_in_rank sütunundaki değerleri change_in_rank degeri ile dolduruyoruz.
mean_rank_change = df['change_in_rank'].mean()  # change_in_rank sütununun ortalamasını hesaplıyoruz
df['change_in_rank'].fillna(mean_rank_change, inplace=True)

df.columns = ['sira', 'isim', 'gelirler', 'gelir_yüzde_degisim', 'karlar', 'kar_yuzde_degisim', 
              'varliklar', 'piyasa_degeri', 'sira_degisikligi', 'calısanlar']

print(df.head())
df.to_csv('ilkbinsirket_clean_updated.csv', index=False)