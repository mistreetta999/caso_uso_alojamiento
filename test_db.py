import psycopg2

try:
    conn = psycopg2.connect(
        dbname="sistema",
        user="carolinam",
        password="superseguro",
        host="127.0.0.1",
        port="5432"
    )
    print("✅ Conexión a Postgres OK")
    conn.close()
except Exception as e:
    print("❌ Error de conexión:", e)
