import requests
import pandas as pd
import matplotlib.pyplot as plt
import json
import streamlit as st

# Función para simular respuesta de API (datos hardcodeados para ejemplo)
def simular_respuesta_api():
    """
    Simula una respuesta de API con datos de ejemplo.
    En un escenario real, reemplaza esto con consumir_api().
    """
    return [
        {"uid": "CHEROKES", "flujo": 100.0, "presion": 5.0},  # Punto de partida
        {"uid": "CHEROKES 1", "flujo": 30.0, "presion": 4.5},
        {"uid": "CHEROKES 2", "flujo": 40.0, "presion": 4.0},
        {"uid": "CHEROKES 3", "flujo": 20.0, "presion": 3.5}
    ]

# Función para calcular el balance de agua (sin cambios)
def calcular_balance(datos):
    if not datos:
        return {"error": "No hay datos disponibles"}
    
    punto_partida = datos[0]
    flujo_entrada = punto_partida['flujo']
    flujo_salida_total = sum(p['flujo'] for p in datos[1:])
    diferencia = flujo_entrada - flujo_salida_total
    fuga_derivacion = "Sí" if abs(diferencia) > 0.01 else "No"
    
    return {
        "flujo_entrada": flujo_entrada,
        "flujo_salida_total": flujo_salida_total,
        "diferencia": diferencia,
        "fuga_derivacion": fuga_derivacion
    }

# Función para visualizar datos (sin cambios)
def visualizar_datos(datos, balance):
    df = pd.DataFrame(datos)
    
    st.pyplotfigure(figsize=(10, 5))
    st.pyplot.subplot(1, 2, 1)
    st.pyplot.bar(df['uid'], df['flujo'], color='blue')
    st.pyplot.title('Flujos por Punto (L/s)')
    st.pyplot.xlabel('UID')
    st.pyplot.ylabel('Flujo (L/s)')
    st.pyplot.axhline(y=balance['flujo_entrada'], color='red', linestyle='--', label='Flujo de Entrada')
    st.pyplot.legend()
    
    st.pyplot.subplot(1, 2, 2)
    st.pyplot.plot(df['uid'], df['presion'], marker='o', color='green')
    st.pyplot.title('Presiones por Punto (kg/cm²)')
    st.pyplot.xlabel('UID')
    st.pyplot('Presión (kg/cm²)')
    
    st.pyplot.tight_layout()
    plt.show()
    
    print("=== Balance de Agua ===")
    print(f"Flujo de Entrada: {balance['flujo_entrada']} L/s")
    print(f"Flujo de Salida Total: {balance['flujo_salida_total']} L/s")
    print(f"Diferencia: {balance['diferencia']} L/s")
    print(f"¿Fuga o Derivación?: {balance['fuga_derivacion']}")

# Programa principal (modificado para usar simulación)
if __name__ == "__main__":
    # Usar simulación en lugar de API real
    datos = simular_respuesta_api()
    
    if datos:
        balance = calcular_balance(datos)
        visualizar_datos(datos, balance)
    else:
        print("No se pudieron obtener datos.")
