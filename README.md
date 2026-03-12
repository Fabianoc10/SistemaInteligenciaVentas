Sistema de Inteligencia de Ventas con SQL, Python y Dashboard
 Propósito
Este proyecto tiene como objetivo transformar datos de ventas en información útil y accionable para apoyar la toma de decisiones comerciales. Se busca identificar tendencias, productos de mayor desempeño y patrones de comportamiento que permitan optimizar inventario y estrategia comercial.

 Objetivos
Identificar productos con mejor desempeño en ventas.

Analizar variaciones de ventas en diferentes periodos (mensual, trimestral, anual).

Generar reportes ejecutivos y dashboards interactivos para facilitar la interpretación de resultados.

Proveer recomendaciones basadas en datos para apoyar decisiones estratégicas.

 Preguntas clave
¿Qué productos tienen mejor desempeño?

¿Cómo varían las ventas por periodo?

¿Qué tendencias ayudan a planear inventario?

 Tecnologías utilizadas
SQL (MySQL/PostgreSQL): gestión y consulta de datos.

Python (Pandas, NumPy, Matplotlib, Seaborn, Plotly): análisis y visualización.

Streamlit/Dash: construcción de dashboards interactivos.

Git + GitHub: control de versiones y colaboración.

Docker (opcional): reproducibilidad del entorno.

📂 Estructura del proyecto
SistemaInteligenciaVentas/
├── data/              # Datos crudos y procesados
├── notebooks/         # Jupyter Notebooks para análisis exploratorio
├── src/               # Scripts Python (ETL, análisis, visualizaciones)
├── visuals/           # Gráficos y capturas del dashboard
├── docs/              # Documentación (problema, objetivos, reportes)
├── requirements.txt   # Librerías necesarias
├── README.md          # Descripción general del proyecto
├── LICENSE            # Licencia de uso
└── .gitignore         # Archivos a excluir del repositorio

 Instalación
Clonar el repositorio:

git clone https://github.com/Fabianoc10/SistemaInteligenciaVentas.git
cd SistemaInteligenciaVentas

Crear entorno virtual:

python -m venv venv
venv\Scripts\activate      # Windows

Instalar dependencias:

pip install -r requirements.txt

 Uso
Ejecutar notebooks en notebooks/ para análisis exploratorio.
Correr el dashboard con:

streamlit run src/dashboard.py

 Documentación
La definición del problema y objetivos se encuentra en docs/Definicion_Problema_Objetivos.md.
Los reportes ejecutivos y hallazgos clave se irán agregando en esta carpeta.