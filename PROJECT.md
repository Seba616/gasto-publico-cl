# Análisis de Gasto Público en Chile — Mercado Público

## 1. Definición del proyecto

**Objetivo general:**
Analizar el comportamiento del gasto público en Chile a través de las órdenes de compra publicadas en Mercado Público (ChileCompra), comunicando los hallazgos mediante un dashboard interactivo.

**Motivación:**
Proyecto de portafolio para demostrar competencias en limpieza de datos, análisis exploratorio (EDA) y construcción de dashboards, usando una fuente de datos pública y real de Chile.

---

## 2. Alcance

### Dentro del alcance

- Descarga y limpieza de datos abiertos de órdenes de compra (ChileCompra).
- Análisis exploratorio de datos (EDA) enfocado en responder preguntas de negocio concretas.
- Dashboard interactivo con filtros (región, año, categoría/organismo).
- Documentación del proceso y de los hallazgos (README + notebook comentado).

### Fuera de alcance

- Modelos predictivos o de Machine Learning (este proyecto es EDA/BI, no ML).
- Consumo de la API en tiempo real como fuente principal de datos (solo como demo opcional al final).
- Análisis detallado de proveedores individuales (posible proyecto futuro).
- Comparación multianual profunda si el volumen de datos lo hace inviable para el tiempo disponible.

---

## 3. Preguntas de negocio (KPIs / hallazgos a responder)

1. **Distribución geográfica del gasto:** ¿Qué regiones concentran más gasto público?
2. **Categorías de compra:** ¿Qué categorías de productos/servicios se compran más (por monto y por cantidad de órdenes)?
3. **Estacionalidad:** ¿Existen patrones estacionales en el gasto (ej. aumento de compras a fin de año fiscal)?
4. **Concentración institucional:** ¿Qué organismos son los que más compran y en qué se especializan?
5. **(Opcional) Evolución temporal:** ¿Cómo ha cambiado el gasto público año a año?

**Criterio de éxito:** Dashboard funcional con filtros, capaz de sustentar 3-4 conclusiones claras y defendibles en una entrevista técnica.

---

## 4. Fuente de datos

- **Portal:** [datos-abiertos.chilecompra.cl/descargas/ordenes-y-licitaciones](https://datos-abiertos.chilecompra.cl/descargas/ordenes-y-licitaciones)
- **Formato de acceso:** Descarga masiva directa (CSV/Excel), sin necesidad de API key.
- **Alcance temporal:** A definir según volumen (1-2 años para mantener el proyecto abarcable en un fin de semana extendido).
- **Nota:** La API oficial (api.mercadopublico.cl) queda descartada como fuente principal por su lentitud para descargas masivas; se evalúa su uso solo como demo puntual.

---

## 5. Tecnologías

| Capa                                  | Tecnología                        | Justificación                                                                        |
| ------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------ |
| Lenguaje / manipulación de datos      | Python + pandas                   | Estándar de la industria en desarrollo de software (vs. R, más orientado a research) |
| Exploración                           | Jupyter Notebook                  | Iteración rápida, código + output + notas en un mismo lugar                          |
| Visualización exploratoria            | matplotlib / seaborn              | Suficiente para EDA dentro del notebook                                              |
| Visualización interactiva (dashboard) | plotly (opcional sobre Streamlit) | Gráficos interactivos (zoom, hover)                                                  |
| Dashboard                             | Streamlit                         | Python puro, sin necesidad de HTML/CSS/JS, deploy simple                             |
| Control de versiones                  | Git + GitHub                      | Estándar de la industria, portafolio público                                         |
| Deploy                                | Streamlit Community Cloud         | Gratuito, integración directa con GitHub                                             |

---

## 6. Arquitectura

Pipeline lineal simple (no requiere microservicios ni backend propio):

```
[Datos crudos]  →  [Limpieza / procesamiento]  →  [Datos procesados]  →  [Dashboard]
  (CSV/Excel          (notebook con pandas)          (CSV/parquet           (Streamlit
  descargado de                                       limpio)                lee este
  ChileCompra)                                                               archivo)
```

### Estructura de carpetas

```
gasto-publico-cl/
├── data/
│   ├── raw/              # archivo original, nunca se modifica
│   └── processed/        # archivo limpio, resultado del procesamiento
├── notebooks/
│   └── 01_exploracion.ipynb
├── src/
│   └── limpieza.py       # script reutilizable de limpieza, una vez validado en el notebook
├── app.py                 # dashboard de Streamlit
├── requirements.txt
└── README.md
```

**Principio clave:** separar `raw` de `processed` — el dato original nunca se toca, permitiendo reprocesar desde cero ante cualquier error.

---

## 7. Fases del proyecto

| Fase                                | Descripción                                                                                                     |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Fase 0 — Setup**                  | Repo en GitHub, estructura de carpetas, entorno virtual, `requirements.txt` inicial, descarga del dataset crudo |
| **Fase 1 — Exploración inicial**    | Carga del dataset, `.info()`, `.head()`, `.describe()`, identificación de problemas (nulos, tipos, duplicados)  |
| **Fase 2 — Limpieza**               | Corrección de tipos de datos, tratamiento de nulos, guardado en `data/processed/`                               |
| **Fase 3 — EDA**                    | Responder cada pregunta de negocio de la sección 3 con visualizaciones, documentar hallazgos                    |
| **Fase 4 — Dashboard**              | Migración del análisis a `app.py`, filtros interactivos, selección de 3-4 visualizaciones clave                 |
| **Fase 5 — Deploy + documentación** | Deploy en Streamlit Community Cloud, README final con contexto, hallazgos y cómo correr el proyecto localmente  |

---

## 8. Notas de aprendizaje

Proyecto desarrollado como ejercicio de aprendizaje práctico, construido paso a paso con foco en entender el "por qué" de cada decisión técnica, no solo el "cómo".
