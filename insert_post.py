#!/usr/bin/python3
# -*- coding: UTF-8 -*-


try:
    import psycopg2
except:
    sys.exit("[!] Instale a lib psycopg2")
try:
    con = psycopg2.connect("host=127.0.0.1 dbname=test user=elias password=elias")
    cur = con.cursor()
    cur.execute("insert into client(id,nome,cpf) values(1,'elias',123)")
    con.commit()
    print("Registro add")
except Exception as e:
    print ("Erro: {}".format(e))
    print("Rollback...")
    con.rollback()
finally:
    print("Finalizando...")
    cur.close()
    con.close()
