import psycopg


try:
    conn = psycopg.connect('postgresql://testdb')
except Exception as e:
    print('Connot connect to DB because of: ', e)


cursor = conn.cursor()
