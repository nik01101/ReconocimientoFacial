

# 👤 Reconocimiento Facial

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)  
[![OpenCV](https://img.shields.io/badge/OpenCV-Enabled-green.svg)](https://opencv.org/)  
[![face_recognition](https://img.shields.io/badge/Face%20Recognition-OK-red.svg)](https://github.com/ageitgey/face_recognition)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](#)  

Proyecto en **Python** para reconocimiento facial, indexación y registro de asistencia.  
Detecta rostros desde la **webcam**, los compara con imágenes previamente almacenadas y genera un **registro de asistencia** en formato CSV.

---

## 📸 Vista previa

![image](https://github.com/user-attachments/assets/ca8f74ae-5463-4803-aabe-86260d2e4c1a)


https://github.com/user-attachments/assets/c70f3f19-190c-454b-a1bf-ea0f465aaa86

---

## 🚀 Características

- Detección y reconocimiento facial en tiempo real.  
- Registro de asistencia en archivo CSV (`Attendance.csv`).  
- Indexación automática de rostros desde la carpeta `ImagenesAttendance/`.  
- Ejecución local sin necesidad de servidor externo.  

---

## 📦 Requisitos

- **Python 3.8+**  
- Librerías:  
  - `opencv-python`  
  - `face_recognition`  
  - `numpy`  
  - `pandas`  

---

## ⚙️ Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/nik01101/ReconocimientoFacial.git
   cd ReconocimientoFacial
2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
    ```
   ```bash

   pip install opencv-python face_recognition numpy pandas

## ▶️ Uso
Ejecuta el script principal de prueba:

  ```bash
    python AttendanceTesteo.py
```

Al iniciar, el sistema cargará las imágenes de ImagenesAttendance/.

Luego abrirá la cámara y comenzará a detectar rostros.

Si un rostro coincide con la base, se registra la asistencia en Attendance.csv.

## 📂 Estructura del proyecto
```

ReconocimientoFacial/
├── ImagenesAttendance/     # Imágenes de rostros conocidos
├── AttendanceTesteo.py     # Script principal
├── Attendance.csv          # Registro de asistencia generado
├── basics.py               # Script auxiliar
├── requirements.txt        # Dependencias (opcional)
├── README.md               # Documentación
└── .idea/                  # Configuración del IDE (ignorar)
```
## 🛠 Tecnologías usadas
Python 3.8+

OpenCV → procesamiento de imágenes.

face_recognition → detección y comparación de rostros.

NumPy y Pandas → manejo de datos.

## 🤝 Contribuciones
¡Las contribuciones son bienvenidas!
Si quieres colaborar:

Haz un fork del proyecto.

Crea una rama (git checkout -b feature/nueva-funcionalidad).

Haz commit de tus cambios (git commit -m "Agrego nueva funcionalidad").

Haz push (git push origin feature/nueva-funcionalidad).

Crea un Pull Request.

## 📜 Licencia
Este proyecto está bajo la licencia MIT.
Consulta el archivo LICENSE para más detalles.

## ⭐ Créditos
Desarrollado por Nikcolas Canessa 💻
