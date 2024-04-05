import pandas
import sqlite3
#выводит списком всех гостей
def get_guest(conn):
 return pandas.read_sql(
 '''
 SELECT guest_name FROM guest
 ''', conn)

#
def get_booking_guest(conn, guest_id):
    return pandas.read_sql('''
        SELECT room_booking.room_booking_id AS Номер_бронирования,
                        room.room_name AS Номер_комнаты,
                        room_booking.guest_id AS Клиент,
                        room_booking.check_in_date AS Дата_заселения,
                        room_booking.check_out_date AS Дата_выселения,
                        status.status_name AS Статус
        FROM room_booking JOIN room USING(room_id) JOIN status USING(status_id)
        WHERE room_booking.guest_id = :id
    ''', conn, params={"id": guest_id})

def get_guest_id(conn, guest_name):
    return pandas.read_sql('''
        SELECT guest_id
        FROM guest
        WHERE guest_name = :name
    ''', conn, params={"name": guest_name})

conn = sqlite3.connect('booking.sqlite')
guest_id = 3  # Здесь указываем ID нужного клиента
bookings = get_booking_guest(conn, guest_id)

# Вывод результатов
print(bookings)

conn.close()
