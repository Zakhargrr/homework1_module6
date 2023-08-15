import psycopg2

from src.utils import create_table

with psycopg2.connect(
        host="localhost",
        database="coursework_module5",
        user="postgres",
        password="12345678"
) as conn:
    create_table("yandex", "1740", conn)
    create_table("sberbank", "3529", conn)
    create_table("alfa_bank", "80", conn)
    create_table("tinkoff", "78638", conn)
    create_table("vk", "15478", conn)
    create_table("kaspersky", "1057", conn)
    create_table("avito", "84585", conn)
    create_table("mts", "3776", conn)
    create_table("vtb", "4181", conn)
    create_table("ozon", "2180", conn)
