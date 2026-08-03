# Gasto Público en Chile — Análisis y Dashboard

Dashboard interactivo que analiza el gasto público en Chile a través de las
órdenes de compra publicadas en Mercado Público (ChileCompra), respondiendo
preguntas de negocio concretas sobre distribución geográfica, categorías de
compra, estacionalidad y concentración institucional.

**🔗 Ver el dashboard en vivo:** [gasto-publico-cl.streamlit.app](https://gasto-publico-cl.streamlit.app)

---

## Sobre el proyecto

Proyecto de portafolio enfocado en análisis de datos y BI, usando una fuente
de datos pública y real de Chile. Cubre el flujo completo: descarga de datos
abiertos, limpieza, análisis exploratorio (EDA), y dashboard interactivo con
filtros.

Para el detalle completo de objetivo, alcance, decisiones técnicas y
metodología, ver [PROJECT.md](PROJECT.md).

## Preguntas de negocio respondidas

1. ¿Qué regiones concentran más gasto público?
2. ¿Qué categorías de productos/servicios se compran más?
3. ¿Existe estacionalidad en el gasto?
4. ¿Qué organismos son los que más compran?

## Tecnologías

- **Python** + **pandas** — limpieza y análisis de datos
- **Jupyter Notebook** — exploración y documentación del proceso
- **Streamlit** + **Plotly** — dashboard interactivo
- **Datos:** [Datos Abiertos ChileCompra](https://datos-abiertos.chilecompra.cl/descargas/ordenes-y-licitaciones) — Órdenes de compra vía licitación, enero-mayo 2026

## Estructura del repositorio

```
gasto-publico-cl/
├── data/
│   ├── raw/              # datos originales descargados de ChileCompra
│   └── processed/        # dataset limpio, listo para análisis
├── notebooks/
│   ├── 01_exploracion.ipynb   # investigación inicial de los datos
│   ├── 02_limpieza.ipynb      # limpieza aplicada, paso a paso documentado
│   └── 03_eda.ipynb           # análisis exploratorio con las 4 preguntas de negocio
├── app.py                 # dashboard de Streamlit
├── requirements.txt
├── PROJECT.md              # definición completa del proyecto
└── README.md
```

## Cómo correrlo localmente

```bash
git clone https://github.com/Seba616/gasto-publico-cl.git
cd gasto-publico-cl
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
streamlit run app.py
```

## Principales hallazgos

- La **Región Metropolitana** concentra el mayor gasto público, más de 5
  veces el monto de la segunda región (Valparaíso).
- La categoría **"Defensa nacional, orden público y seguridad"** lidera el
  gasto por tipo de producto/servicio.
- El gasto muestra un **pico en febrero**, con caída sostenida hacia mayo
  (último mes disponible en el dataset).
- El **Servicio Nacional de Reinserción Social Juvenil** es la institución
  individual con mayor gasto, seguido de organismos vinculados a educación
  y protección de la niñez.

Detalle completo de cada hallazgo, con gráficos y contexto, disponible en
[`notebooks/03_eda.ipynb`](notebooks/03_eda.ipynb) y en el dashboard en vivo.
