import pandas as pd

def run_etl():
    # 1. Extraer
    df = pd.read_csv("data/raw/train.csv")

    # 2. Inspección inicial
    print("Dimensiones iniciales:", df.shape)
    print("Columnas:", df.columns.tolist())

    # 3. Normalización de nombres de columnas
    df.columns = (
        df.columns.str.strip()      # quitar espacios
                 .str.lower()       # pasar a minúsculas
                 .str.replace(" ", "_")  # reemplazar espacios por guiones bajos
    )

    # 4. Manejo de nulos por columna
    if "precio" in df.columns:
        df["precio"] = df["precio"].fillna(0)

    if "cantidad" in df.columns:
        df["cantidad"] = df["cantidad"].fillna(df["cantidad"].median())

    if "fecha" in df.columns:
        df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
        df = df.dropna(subset=["fecha"])  # eliminar filas sin fecha válida

    # 5. Eliminación de duplicados
    df = df.drop_duplicates()

    # 6. Creación de columnas derivadas
    if "fecha" in df.columns:
        df["anio"] = df["fecha"].dt.year
        df["mes"] = df["fecha"].dt.month
        df["dia"] = df["fecha"].dt.day

    # 7. Guardar dataset limpio
    df.to_csv("data/processed/ventas_clean.csv", index=False)
    print("ETL completado. Archivo guardado en data/processed/ventas_clean.csv")
    print("Dimensiones finales:", df.shape)

if __name__ == "__main__":
    run_etl()

