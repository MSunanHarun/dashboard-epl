import streamlit as st
import pandas as pd
from Olah import pilihmusim
from Olah import pilihklub
from Olah import golterbanyak
from Olah import kebobolanterbanyak
from Olah import kemenanganterbanyak
from Olah import kekalahanterbanyak
from Olah import cekfloat
from Olah import golpermusim

import warnings

klasmen_all_team=cekfloat(pd.read_csv("Dataset/Klasmen_all.csv"))
klasmen_22_musim=cekfloat(pd.read_csv("Dataset/Klasmen 22 musim.csv"))
juara_permusim=cekfloat(pd.read_csv("Dataset/Juara Permusim.csv"))
all_juara=cekfloat(pd.read_csv("Dataset/All Juara.csv"))

st.title("Dashboard EPL 2000-2022")
tab1,tab2,tab3,tab4,tab5=st.tabs(["Klasmen Semua Klub","Juara Tiap Musim","Perolehan Tropi","Klasmen Per Musim","Data Per Klub"])


with tab1:
    st.header("Data Klub EPL 2000-2022")
    
    col1,col2=st.columns(2)

    with col1:
        st.subheader("Lima Besar Klub Terbaik")
        data=klasmen_all_team.iloc[:5,:]
        st.bar_chart(data,x="Club",y="Poin")
    
    with col2:
        st.subheader("Lima Klub Terbawah")
        data=klasmen_all_team.iloc[-5:,:]
        st.bar_chart(data,x="Club",y="Poin")

    st.subheader("Gol Yang Dicetak Permusim")
    st.line_chart(golpermusim(klasmen_22_musim),y="GoalScored")

    st.subheader("Klasmen Klub EPL 2000-2022")
    st.dataframe(klasmen_all_team)

with tab2:
    st.header("Data Juara Tiap Musim")
    col1,col2,col3=st.columns(3)

    with col1:
        st.header("Poin Tim Juara Per Musim")
        st.line_chart(juara_permusim,x="Season",y="Poin")

    with col2:
        st.header("Jumlah Gol Tim Juara Per Musim")
        st.line_chart(juara_permusim,x="Season",y="Goal_Scored")

    with col3:
        st.header("Jumlah Kebobolan Tim Juara Per Musim")
        st.line_chart(juara_permusim,x="Season",y="Goal_Conceede")
    st.header("Klasmen Juara Tiap Musim")
    st.dataframe(juara_permusim)

with tab3:
    st.header("Perolehan Tropi")
    st.bar_chart(all_juara,x="Klub",y="Tropi")


with tab4:
    st.header("Data Permusim")
    pilihan=st.selectbox(
        "Pilih Musim",
        juara_permusim["Season"]
    )
    tampil=pilihmusim(pilihan,klasmen_22_musim)

    col1,col2=st.columns(2)

    with col1:
        st.subheader("Gol Terbanyak")
        st.write(f"{golterbanyak(tampil)['Klub']} dengan {golterbanyak(tampil)['JumlahGol']} Gol")  
    with col2:
        st.subheader("Kebobolan Terbanyak")
        st.write(f"{kebobolanterbanyak(tampil)['Klub']} dengan {kebobolanterbanyak(tampil)['JumlahKebobolan']} Gol")  

    col3,col4=st.columns(2)
    with col3:
        st.subheader("Kemenangan Terbanyak")
        st.write(f"{kemenanganterbanyak(tampil)['Klub']} dengan {kemenanganterbanyak(tampil)['JumlahKemenangan']} kemenangan")  
    with col4:
        st.subheader("Kekalahan Terbanyak")
        st.write(f"{kekalahanterbanyak(tampil)['Klub']} dengan {kekalahanterbanyak(tampil)['JumlahKekalahan']} kekalahan")  
        
    st.subheader(f"Klasmen musim {pilihan}")
    st.dataframe(tampil)

with tab5:
    st.header("Data PerKlub")
    pilihan=st.selectbox(
        "Pilih Klub",
        klasmen_all_team["Club"]
    )
    tampil=pilihklub(pilihan,klasmen_22_musim)

    col1,col2=st.columns(2)
    with col1:
        st.subheader("Grafik Jumlah Gol")
        st.line_chart(tampil,x="Season",y="GoalScored")
    with col2:
        st.subheader("Grafik Jumlah Kebobolan")
        st.line_chart(tampil,x="Season",y="GoalConceeded")
    
    col3,col4=st.columns(2)
    with col3:
        st.subheader("Grafik Jumlah Kemenangan")
        st.line_chart(tampil,x="Season",y="Win")
    with col4:
        st.subheader("Grafik Jumlah Kekalahan")
        st.line_chart(tampil,x="Season",y="Loss")
    st.subheader(f"Pencapaian Klub {tampil['Klub'][0]} 2000-2022")
    data=tampil.drop(["Klub"],axis=1)
    st.dataframe(data)


