import os

# Define la cantidad de archivos a generar (10 cumple con 5 < n < 20)
n_archivos = 10 
directorio = "dataset_docker"

# Crea la carpeta si no existe
if not os.path.exists(directorio):
    os.makedirs(directorio)

for i in range(1, n_archivos + 1):
    # Genera una plantilla básica de red Docker con subredes dinámicas
    contenido_yaml = f"""networks:
  red_simulada_{i}:
    driver: bridge
    ipam:
      config:
        - subnet: 172.18.{i}.0/24
"""
    nombre_archivo = f"{directorio}/docker_test_{i}.yml"
    
    with open(nombre_archivo, "w") as f:
        f.write(contenido_yaml)
        
print(f"Se han generado exitosamente {n_archivos} archivos de prueba en la carpeta '{directorio}'.")