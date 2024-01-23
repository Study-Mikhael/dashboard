# Import Lib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Body
st.title('Belajar Analisis Data')

# Pendefinisian
df = pd.read_csv("main_data.csv")
st.dataframe(data=df)

# Visualisasi Keseluruhan Data
st.header("Visualisasi Keseluruhan Data")

# Score yang Ditampilkan
score_order = ['Baik', 'Bagus', "Biasa", "Jelek", "Buruk"]

# Grup Bar Sesuai Kategori
plt.figure(figsize=(12, 8))
sns.countplot(x='product_category_name_english',
              hue='score_category',
              data=df,
              palette='viridis',
              order=df['product_category_name_english'].unique(),
              hue_order=score_order)
plt.title('Kategori Yang Mendapat Score Baik Hingga Buruk')
plt.xlabel('Product Category (English)')
plt.ylabel('Count')
plt.legend(title='Score Category')
plt.xticks(rotation=90, ha='right')
st.pyplot(plt)

# Visualisasi 5 Barang Yang Berpotensi Menjadi Barang Rekomendasi
st.header("Visualisasi 5 Barang Yang Berpotensi Menjadi Barang Rekomendasi")
# Score yang Ditampilkan
score_order = ['Baik', 'Bagus']

# Grup Bar Sesuai Kategori
plt.figure(figsize=(12, 8))
sns.countplot(x='product_category_name_english',
              hue='score_category',
              data=df,
              palette='viridis',
              order=df['product_category_name_english'].unique(),
              hue_order=score_order)
plt.title('Kategori Yang Mendapat Score Baik Dan Bagus')
plt.xlabel('Product Category (English)')
plt.ylabel('Count')
plt.legend(title='Score Category')
plt.xticks(rotation=90, ha='right')
st.pyplot(plt)

# Visualisasi 5 Barang Yang Berpotensi Harus Ditinjau Kembali
st.header("Visualisasi 5 Barang Yang Berpotensi Harus Ditinjau Kembali")
# Score yang Ditampilkan
score_order = ['Jelek', 'Buruk']

# Grup Bar Sesuai Kategori
plt.figure(figsize=(12, 8))
sns.countplot(x='product_category_name_english',
              hue='score_category',
              data=df,
              palette='viridis',
              order=df['product_category_name_english'].unique(),
              hue_order=score_order)
plt.title('Kategori Yang Mendapat Score Jelek Dan Buruk')
plt.xlabel('Product Category (English)')
plt.ylabel('Count')
plt.legend(title='Score Category')
plt.xticks(rotation=90, ha='right')
st.pyplot(plt)