# -*- coding: utf-8 -*-"

import pyodbc


class MssqlDb:
    """This class is wrapper to work with mssql databases"""

    def __init__(self):
        """Method-contructor for LiteDb class

        Args:
            db_name: database name.
        """
        try:
            self.conn = pyodbc.connect(
                'DRIVER={ODBC Driver 11 for SQL Server};SERVER=USTIN-PC\SQLEXPRESS;DATABASE=temporaryDB;UID=sa;PWD=qweasdzxc')
            self.cursor = self.conn.cursor()
            # self.cursor.execute('CREATE TABLE IF NOT EXISTS apartments (id INTEGER, url VARCHAR(100), price VARCHAR(30), '
            #                    'phone VARCHAR(30), ap_name VARCHAR(300), owner VARCHAR(100), about VARCHAR(5000))')
            # self.con.commit()
        except:
            print("EXCEPPPT DURING CONNECTION TO DATABASE!")

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
        self.con = MssqlDb().conn
        self.cursor = self.con.cursor()

    def get_apartment_by_id(self, id):
        """Method to get all apartments from BD"""
        self.cursor.execute('select * from apartments where id = {id}'.format(id=id))
        return self.cursor.fetchall()

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
        except pyodbc.IntegrityError:
            print("\n\nZAPIS S TAKIM AIDI UCHE EST!: " + self.get_apartment_by_id(ap_id) + "\n\n")

    def add_apartment(self, flat):
        """Add apartment to database

        Args:
            flat: object of class Flat

        Returns:
            ap_id: id of added apartment.
        """
        try:
            self.cursor.execute('INSERT INTO apartments '
                                '(Name,'
                                ' Author,'
                                ' Price,'
                                ' Phone,'
                                ' Description,'
                                ' DateCreated,'
                                ' DateActualTo,'
                                ' IsActive, IsDonated,'
                                ' ParsingSource,'
                                ' ShortId,'
                                ' SourceURL,'
                                ' mainPhotoUrl,'
                                ' photosListUrls) '
                                'VALUES '
                                '({name},'
                                ' "{author}", '
                                '"{price}", '
                                '"{phone}", '
                                '"{phoneImgBinary}", '
                                '"{mainApPhotoBinary}", '
                                '"{creationDate}", '
                                '"{actualToDate}", '
                                '"{isActive}", '
                                '"{isDonated}", '
                                '"{donateDueDate}", '
                                '"{internalComment}", '
                                '"{clientId}", '
                                '"{parsingSource}", '
                                '"{shortId}", '
                                '"{mainPhotoUrl}", "{photosListUrls}")'.format(name=flat.name,
                                                                               author=flat.author,
                                                                               price=flat.price,
                                                                               phone=flat.phone,
                                                                               description=flat.description,
                                                                               phoneImgBinary=flat.phoneImgBinary,
                                                                               mainApPhotoBinary=flat.mainApPhotoBinary,
                                                                               creationDate=flat.creationDate,
                                                                               actualToDate=flat.actualToDate,
                                                                               isActive=flat.isActive,
                                                                               isDonated=flat.isDonated,
                                                                               donateDueDate=flat.donateDueDate,
                                                                               internalComment=flat.internalComment,
                                                                               clientId=flat.clientId,
                                                                               parsingSource=flat.parsingSource,
                                                                               shortId=flat.shortId,
                                                                               mainPhotoUrl=flat.mainPhotoUrl,
                                                                               photosListUrls=flat.photosListUrls))
            self.con.commit()
        except pyodbc.IntegrityError:
            print("\n\nZAPIS S TAKIM AIDI UCHE EST!: " + self.get_apartment_by_id(flat.ap_id) + "\n\n")

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
