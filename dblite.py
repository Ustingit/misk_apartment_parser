# -*- coding: utf-8 -*-"

import sqlite3


class LiteDb:
    """This class is wrapper to work with sqllite3 databases"""

    def __init__(self, db_name):
        """Method-contructor for LiteDb class

        Args:
            db_name: database name.
        """
        try:
            self.con = sqlite3.connect(db_name)
            self.cursor = self.con.cursor()
            self.cursor.execute('CREATE TABLE IF NOT EXISTS apartments (id INTEGER, url VARCHAR(100), price VARCHAR(30), '
                                'phone VARCHAR(30), ap_name VARCHAR(300), owner VARCHAR(100), about VARCHAR(5000))')
            self.con.commit()
        except sqlite3.OperationalError:
            print("EXCEPPPT DURING CREATING TABLE!")

    def execute_sql(self, sql):
        """Method to execute sql-rows

        Args:
            sql: sql-row to execute
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()


class ApartmentsDb:

    def __init__(self, db_name='apartments.db'):
        """Method-contructor for ApartmentsDb class

        Args:
            db_name: database name.
        """
        self.con = LiteDb(db_name=db_name).con
        self.cursor = self.con.cursor()

    def add_apartment(self, ap_id, url=None, price=None, phone=None, ap_name=None, owner=None, about=None):
        """Add apartment to database

        Args:
            ap_id:
            url:
            price:
            phone:
            ap_name:
            owner:
            about:

        Returns:
            ap_id: id of added apartment.
        """
        try:
            self.cursor.execute('INSERT INTO apartments '
                                '(id, url, price, phone, ap_name, owner, about) '
                                'VALUES({id}, "{url}", "{price}", "{phone}", '
                                '"{ap_name}", "{owner}", "{about}")'.format(id=ap_id,
                                                                            url=url,
                                                                            price=price,
                                                                            phone=phone,
                                                                            ap_name=ap_name,
                                                                            owner=owner,
                                                                            about=about))
            self.con.commit()
        except sqlite3.IntegrityError:
            print("ZAPIS S TAKIM AIDI UCHE EST!")
            self.cursor.execute('select * from apartments where id = {id}'.format(id=ap_id))
            print(self.cursor.fetchall())
            print("ZAPIS S TAKIM AIDI UCHE EST!END")

    def get_apartments(self):
        """Method to get all apartments from BD"""
        self.cursor.execute('SELECT * FROM apartments')
        self.con.commit()
        return self.cursor.fetchall()

    def get_exist_apartments_ids(self):
        """Method to get apartment's ids from BD"""
        self.cursor.execute('SELECT id FROM apartments')
        self.con.commit()
        return [i[0] for i in self.cursor.fetchall()]
