import sqlite3
def get_db_connection():
 #return sqlite3.connect('library.sqlite')
    # создаем базу данных и устанавливаем соединение с ней
    con = sqlite3.connect("booking.sqlite")
    # открываем файл с дампом базой двнных
    f_damp = open('booking.db','r', encoding ='utf-8-sig')
    # читаем данные из файла
    damp = f_damp.read()
    # закрываем файл с дампом
    f_damp.close()
    # запускаем запросы
    con.executescript(damp)
    # сохраняем информацию в базе данных
    con.commit()
    return con
