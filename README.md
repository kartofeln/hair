# Dashboard de Análisis de Competidores - Cuidado Capilar

Dashboard interactivo para analizar el mercado español de cuidado capilar, incluyendo competidores, segmentación y oportunidades de mercado.

## 🚀 Instalación

1. Clonar el repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
cd [NOMBRE_DEL_REPOSITORIO]
```

2. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar credenciales:
   - Copiar el archivo de ejemplo de configuración:
     ```bash
     cp .streamlit/secrets.toml.example .streamlit/secrets.toml
     ```
   - Editar `.streamlit/secrets.toml` con tus credenciales

## 🏃‍♂️ Ejecución

```bash
streamlit run dashboard_competidores.py
```

## 📊 Características

- Análisis de competidores por segmento y categoría
- Visualización de productos más comunes
- Análisis de canales de distribución
- Identificación de oportunidades de mercado
- Filtros interactivos
- Gráficos dinámicos

## 🔒 Seguridad

- Las credenciales se almacenan en `.streamlit/secrets.toml`
- Este archivo está excluido del control de versiones
- Nunca subas tus credenciales reales al repositorio

## 📝 Estructura del Proyecto

```
.
├── dashboard_competidores.py    # Código principal del dashboard
├── competidores_cabello_espana.py  # Datos de competidores
├── requirements.txt            # Dependencias del proyecto
├── .streamlit/
│   ├── secrets.toml           # Credenciales (no subir a git)
│   └── secrets.toml.example   # Plantilla de configuración
└── README.md                  # Documentación
```

## 🤝 Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles. 