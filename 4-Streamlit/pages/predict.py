import streamlit as st
import pandas as pd
import numpy as np
import pickle 
from joblib import load

#Kullanıcı girişleri için 
circuits = {
    "Bahrain Grand Prix": 3,
    "Saudi Arabian Grand Prix": 77,
    "Australian Grand Prix": 1,
    "Emilia Romagna Grand Prix": 21,
    "Miami Grand Prix": 79,
    "Spanish Grand Prix": 4,
    "Monaco Grand Prix": 6,
    "Azerbaijan Grand Prix": 73,
    "Canadian Grand Prix": 7,
    "British Grand Prix": 9, 
    "Austrian Grand Prix": 70,
    "French Grand Prix": 34,
    "Hungarian Grand Prix": 11,
    "Belgian Grand Prix": 13,
    "Dutch Grand Prix" :  39,
    "Italian Grand Prix": 14,
    "Singapore Grand Prix": 15,
    "Japanese Grand Prix" : 22,
    "United States Grand Prix": 69,
    "Mexico City Grand Prix": 32,
    "São Paulo Grand Prix" : 18,
    "Abu Dhabi Grand Prix" : 24,
    "Qatar Grand Prix": 78,
    "Las Vegas Grand Prix": 80,
    "Chinese Grand Prix": 17,
}
drivers = {
    "Lewis Hamilton": 1,
    "Fernando Alonso": 4,
    "Sebastian Vettel": 20,
    "Pierre Gasly": 842,
    "Nico Hülkenberg": 807,
    "Sergio Pérez": 815,
    "Daniel Ricciardo": 817,
    "Valtteri Bottas": 822,
    "Max Verstappen": 830,
    "Carlos Sainz": 832,
    "Esteban Ocon": 839,
    "Lance Stroll": 840,
    "Charles Leclerc": 844,
    "Lando Norris": 846,
    "George Russell": 847,
    "Alexander Albon": 848,
    "Nicholas Latifi": 849,
    "Yuki Tsunoda": 852,
    "Mick Schumacher": 854,
    "Guanyu Zhou": 855,
    "Nyck de Vries": 856,
    "Oscar Piastri": 857,
    "Logan Sargeant": 858,
    "Liam Lawson": 859,
    "Oliver Bearman": 860,
}

constructors = {
    "Mercedes": 131,
    "Red Bull": 214,
    "Ferrari": 117,
    "Aston Martin": 9,
    "McLaren": 1,
    "Alpine": 51,
    "Alfa Romeo": 210,
    "Haas": 6,
    "AlphaTauri": 213,
    "Williams": 3,
}


# Tahmin Sayfası
st.title("Formula 1 Tahmin Uygulaması")
st.write("Lütfen yarış verilerini girerek tahmini görmek için gerekli bilgileri doldurun.")

# Kullanıcıdan seçim yapılmasını sağlama
circuit_name = st.selectbox("Pist Seçimi (Circuit)", list(circuits.keys()))
driver_name = st.selectbox("Sürücü Seçimi (Driver)", list(drivers.keys()))
constructor_name = st.selectbox("Takım Seçimi (Constructor)", list(constructors.keys()))
grid = st.number_input("Başlangıç Sırası (grid)", min_value=1, step=1)
pit_stop_time = st.number_input("Pit Stop Süresi (s)", min_value=0.0, step=0.1)

# Seçimlerden ID'leri eşleştirme
circuit_id = circuits[circuit_name]
driver_id = drivers[driver_name]
constructor_id = constructors[constructor_name]

# Tahmin butonu
tahmin_butonu = st.button("Tahmin Yap")

if tahmin_butonu:
    # Kullanıcı girdilerini bir DataFrame'e dönüştürme
    user_input = pd.DataFrame({
        "circuitId": [circuit_id],
        "driverId": [driver_id],
        "constructorId": [constructor_id],
        "grid": [grid],
        "pit_stop_time": [pit_stop_time]
    }, columns=["circuitId", "driverId", "constructorId", "pit_stop_time", "grid"])

    # Modeli yükleme
    try:
        model= load("model.pkl")
       
        # Tahmin yapma
        prediction = model.predict(user_input)
        st.success(f"{driver_name} bu yarışı tahmini olarak {prediction[0]}. sırada bitirir")
    except FileNotFoundError:
        st.error("Model dosyası bulunamadı. Lütfen modelinizi 'model.pkl' olarak kaydedin ve yükleyin.")
    except Exception as e:
        st.error(f"Bir hata oluştu: {e}")
