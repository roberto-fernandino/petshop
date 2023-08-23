import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

conn = sqlite3.connect(BASE_DIR / "db.sqlite3")
cursor = conn.cursor()


def product_image_path(instance, filename: str) -> str:
    """armazena a ext do arquivo e cria um path de acordo com o nome do produto"""
    ext = filename.split(".")[-1]
    filename = f"{instance.nome.replace(' ','_')}.{ext}"
    return f"produtos/{filename}"


def SearchProductsToPaymentGateway():
    """Faz um query em todos os produtos e retorna uma lista de dicionarios com todos os produtos"""
    cursor.execute(f"SELECT nome, descricao, category_id, preco FROM loja_produto")
    resultado = cursor.fetchall()
    # Extrai as colunas do ultimo query e salva em columns
    columns = [description[0] for description in cursor.description]
    # cria um dicionario de produtos usando zip para zipar columns, row (valor do query) e transformar em dicionario
    # no formato f"{columns}": f"{row}"
    produtos = [dict(zip(columns, row)) for row in resultado]
    cursor.close()
    conn.close()
    return produtos

