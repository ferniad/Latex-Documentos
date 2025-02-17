import numpy as np

def calcular_porcentaje_error(vector_teorico, vector_datos):
    # Convertimos los vectores a arreglos de numpy para facilitar los cálculos
    vector_teorico = np.array(vector_teorico)
    vector_datos = np.array(vector_datos)
    
    # Asegurarse de que los vectores tengan la misma longitud
    if len(vector_teorico) != len(vector_datos):
        raise ValueError("Los vectores deben tener la misma longitud.")
    
    # Calcular el porcentaje de error
    porcentaje_error = np.abs((vector_teorico - vector_datos) / vector_teorico) * 100
    
    return porcentaje_error

# Ejemplo de uso
vector_teorico = [110.0000 , 11.0293 , 1155.1 , 371.1590 , 1213.2 , 0.9521 , 1129.2]  # Ejemplo de vector teórico
vector_datos = [116.6726 , 11.5761 , 1155.1 , 699.9905 , 1350.6 , 0.8552 , 1129.2]     #vector de datos de 100 hz
#118.8136 , 13.2088 , 1155.1 , 1062.5 , 1569.4, 0.7361 , 1129.2 100 hz
#110 , 11.0293 , 1155.1 , 371.1589 , 1213.2 , 0.9521 , 1129.2  180hz
#118.8136 , 11.7527 , 1155.1 , 784.6681 , 1396.4 , 0.8272 , 1129.2  200hz
#110 , 11.0293 , 1155.1 , 371.1589 , 1213.2 0.9521 , 1129.2
#116.6726 , 11.5761 , 1155.1 , 699.9905 , 1350.6 , 0.8552 , 1129.2
error = calcular_porcentaje_error(vector_teorico, vector_datos)
print("Porcentaje de error:", error)
