"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

with (psycopg2.connect(host="localhost", database="north", user="postgres", password="541709") as conn):
    with conn.cursor() as cur:
        with open ("north_data/employees_data.csv", "r", encoding="UTF-8") as file:
            file_reader = csv.reader(file, delimiter=",")
            count = 0
            for row in file_reader:
                if count == 0:
                    continue
                    count += 1
                cur.execute("INSERT INTO employees values (%s, %s, %s, %s, %s, %s)",
                                    (row[0],row[1],row[2],row[3],row[4],row[5]))

            cur.execute("SELECT * FROM employees")
            rows = cur.fetchall()
            for row in rows:
                print(rows)


        with open ("north_data/customers_data.csv", "r", encoding="UTF-8") as file:
            file_reader = csv.reader(file, delimiter=",")
            count = 0
            for row in file_reader:
                if count == 0:
                    continue
                    count += 1
                cur.execute("INSERT INTO customers values (%s, %s, %s)",
                                    (row[0],row[1],row[2]))

            cur.execute("SELECT * FROM customers")
            rows = cur.fetchall()
            for row in rows:
                print(rows)

        with open ("north_data/orders_data.csv", "r", encoding="UTF-8") as file:
            file_reader = csv.reader(file, delimiter=",")
            count = 0
            for row in file_reader:
                if count == 0:
                    continue
                    count += 1
                cur.execute("INSERT INTO orders values (%s, %s, %s, %s, %s)",
                                    (row[0],row[1],row[2],row[3],row[4]))

            cur.execute("SELECT * FROM orders")
            rows = cur.fetchall()
            for row in rows:
                print(rows)