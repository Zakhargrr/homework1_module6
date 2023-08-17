from models.db_class import DBManager

db_manager = DBManager("db_name",
                       "db_password")  # введите имя и пароль от базы данных, в которых хотите создать таблицы

db_manager.create_table("yandex", "1740")
db_manager.create_table("sberbank", "3529")
db_manager.create_table("alfa_bank", "80")
db_manager.create_table("tinkoff", "78638")
db_manager.create_table("vk", "15478")
db_manager.create_table("kaspersky", "1057")
db_manager.create_table("avito", "84585")
db_manager.create_table("mts", "3776")
db_manager.create_table("vtb", "4181")
db_manager.create_table("ozon", "2180")
