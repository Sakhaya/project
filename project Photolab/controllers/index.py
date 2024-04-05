from app import app
from flask import render_template, request, session

import sqlite3
from utils import get_db_connection
from models.index_model import get_guest, get_booking_guest, get_guest_id

#, get_book_reader, get_new_reader ,
#borrow_book

@app.route('/', methods=['GET'])
def index():
    conn = get_db_connection()
    
    if request.values.get('guest'):
        guest_id = int(request.values.get('guest'))
        session['guest_id'] = guest_id

    elif "guest_id" not in session:
        session['guest_id'] = 1
        
    df_guest = get_guest(conn)
    df_booking_guest = get_booking_guest(conn, session['guest_id'])
    
     # выводим форму
    html = render_template(
        'index.html',
        guest_id = session['guest_id'],
        combo_box = df_guest,
        booking_guest = df_booking_guest,
        len=len)
    return html

