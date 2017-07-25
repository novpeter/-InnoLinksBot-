## -*- coding: utf-8 -*-

import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sqlite3
import os
import config


def create_database():
    if os.path.isfile(config.db_path):
        os.remove(config.db_path)
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute(config.create_db_command)
    print("Table created successfully...")
    conn.commit()
    cursor.close()
    conn.close()


def import_data():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('./json/client_secret.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open("companies").sheet1
    companies = sheet.get_all_records()
    id = 0
    for row in companies:
        id +=1
        card_title = str(row['card_title']).replace("text:", "").replace("number:", "").replace("empty:", "").replace('\\n'," ")
        category = str(row['category']).replace("text:", "").replace("number:", "").replace("empty:", "").replace('\\n'," ")
        subcategory = str(row['subcategory']).replace("text:", "").replace("number:", "").replace("empty:", "").replace('\\n'," ")
        description = str(row['description']).replace("text:", "").replace("number:", "").replace("empty:", "").replace('\\n'," ")
        address = str(row['address']).replace("text:", "").replace("number:", "").replace("empty:", "").replace('\\n'," ")
        phone = str(row['phone']).replace("text:", "").replace("number:", "").replace("empty:", "").replace('\\n'," ")
        schedule = str(row['schedule']).replace("text:", "").replace("number:", "").replace("empty:", "").replace('\\n'," ")
        links = str(row['links']).replace("text:", "").replace("number:", "").replace("empty:", "").replace('\\n'," ")

        cursor.execute(f"INSERT INTO COMPANY (id,name,category,subcategory,description,address,phone,schedule,links) \
                        VALUES ('{id}', '{card_title}', '{category}', '{subcategory}', '{description}', '{address}', '{phone}', '{schedule}', '{links}')")
    conn.commit()
    cursor.close()
    conn.close()
    print("Information imported")

create_database()
import_data()