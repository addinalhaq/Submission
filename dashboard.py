import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Fungsi untuk membaca file CSV
def read_file(file):
    df = pd.read_csv(file)
    return df

# Main function
def main():
    st.title("Aplikasi Analisis Data Bike Sharing")
    
    # Upload file day.csv
    st.subheader("Upload file day.csv")
    uploaded_day_file = st.file_uploader("Upload CSV file for day data", type=["csv"])
    if uploaded_day_file is not None:
        day_df = read_file(uploaded_day_file)
        st.write("Data day.csv berhasil dimuat.")
        
        # Menjawab pertanyaan 1
        st.subheader("Pertanyaan 1: Bagaimana pengaruh suhu terhadap jumlah peminjam sepeda?")
        st.write("Visualisasi hubungan antara suhu dan jumlah peminjam sepeda:")
        sns.set_style("whitegrid")
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.scatterplot(x=day_df['temp'], y='cnt' ,data=day_df, palette='viridis', alpha=0.7, ax=ax)
        ax.set_title('Hubungan antara Suhu dan Jumlah Penyewa Sepeda', fontsize=16)
        ax.set_xlabel('Suhu (Celcius)', fontsize=14)
        ax.set_ylabel('Jumlah Penyewa', fontsize=14)
        st.pyplot(fig)

    # Upload file hour.csv
    st.subheader("Upload file hour.csv")
    uploaded_hour_file = st.file_uploader("Upload CSV file for hour data", type=["csv"])
    if uploaded_hour_file is not None:
        hour_df = read_file(uploaded_hour_file)
        st.write("Data hour.csv berhasil dimuat.")
        
        # Menjawab pertanyaan 2
        st.subheader("Pertanyaan 2: Pada jam berapa jumlah peminjam banyak berdatangan?")
        st.write("Visualisasi jumlah peminjam sepeda per jam:")
        sns.set_style("whitegrid")
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.barplot(y="cnt", x="hr", data=hour_df, color="skyblue", ax=ax)
        ax.set_title('Jumlah Penyewa Sepeda per Jam', fontsize=16)
        ax.set_xlabel('Jam', fontsize=14)
        ax.set_ylabel('Jumlah Penyewa', fontsize=14)
        ax.tick_params(axis='x', labelsize=12)
        st.pyplot(fig)

if __name__ == "__main__":
    main()
