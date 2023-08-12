import sqlite3

conn = sqlite3.connect("/home/roberto/projects/petshop/src/db.sqlite3")
cursor = conn.cursor()


def SearchNewsletterEmail() -> list:
    '''Procura emails onde newsletter = True no banco de dados e returona no formato
    [(email, nome),...]'''
    cursor.execute(f"SELECT email, nome FROM usuarios_atendimentos WHERE is_newsletter = True;")
    emails_validos = cursor.fetchall()
    cursor.execute(f"SELECT email, username FROM usuarios_account WHERE is_newsletter = True;")
    emails_validos += cursor.fetchall()
    emails_validos = set(emails_validos)
    emails_validos = list(emails_validos)
    cursor.close()
    conn.close()
    return emails_validos
   
