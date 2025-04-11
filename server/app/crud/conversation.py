from datetime import datetime
from app.db.connection import get_connection

def create_conversation(question: str, answer: str):
    conn = get_connection()
    cursor = conn.cursor()

    today_date = datetime.now()

    query = "INSERT INTO conversation (created_at, question, answer) VALUES (%s, %s, %s)"
    values = (today_date, question, answer)

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

def get_conversation_dates() :
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT DATE_FORMAT(created_at,"%Y-%m-%d") AS dates FROM conversation GROUP BY created_at ORDER BY DESC"
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records

# 인자인 date 는 "2025-04-10" 같은 문자열
def get_conversation_by_date(date: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # 특정 날짜에 해당하는 채팅내역 조회
    query = "SELECT question, answer FROM conversation WHERE DATE(created_at) = %s ORDER BY created_at ASC"
    cursor.execute(query, (date,))
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records