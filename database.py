import sqlite3

#---------------------------------------- Database Aplikasi ---------------------------------------------------------------------------------------------------------------

def create_table():
    conn = sqlite3.connect('kafe.db')
    cursor = conn.cursor() 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kafe (
            nama TEXT PRIMARY KEY, 
            kenyamanan TEXT, 
            harga TEXT, 
            pelayanan TEXT, 
            kopi TEXT, 
            rec TEXT)''')
    conn.commit()
    conn.close()
    
def insert_kafe(nama, kenyamanan, harga, pelayanan, kopi, rec):
    conn = sqlite3.connect('kafe.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO kafe (nama, kenyamanan, harga, pelayanan, kopi, rec) VALUES (?, ?, ?, ?, ?, ?)', 
                   (nama, kenyamanan, harga, pelayanan, kopi, rec))
    conn.commit()
    conn.close()
    
def search_kafe(query):
    conn = sqlite3.connect('kafe.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM kafe WHERE nama = ?', (query,))
    row = cursor.fetchone()
    conn.close()
    return row

def fetch_all_nama():
    conn = sqlite3.connect('kafe.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nama FROM kafe')
    nama = cursor.fetchall()
    conn.close()
    return [n[0] for n in nama]

def nama_exists(nama):
    conn = sqlite3.connect('kafe.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM kafe WHERE nama = ?', (nama,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

create_table()