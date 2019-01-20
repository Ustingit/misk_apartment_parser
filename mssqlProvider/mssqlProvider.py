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

    def add_apartment(self, flat):
        """Add apartment to database

        Args:
            flat: object of class Flat

        Returns:
            ap_id: id of added apartment.
        """
        query = """INSERT INTO apartments (Name, Author, Price, Phone, Description, DateCreated, DateActualTo, 
        IsActive, IsDonated, DonateDueDate, InternalComment, ClientId, ParsingSource, ShortId, SourceURL, 
        mainPhotoUrl, photosListUrls, phoneImgURL) VALUES ({name}, {author}, {price}, {phone},{description}, 
        {creationDate}, {actualToDate}, {isActive}, {isDonated}, {donateDueDate}, {internalComment}, 
        {clientId}, {parsingSource}, {shortId}, {sourceURL}, {mainPhotoUrl}, {photosListUrls}, 
        {phoneImgURL})""".format(name=flat.name,
                                 author=flat.author,
                                 price=flat.price,
                                 phone=flat.phone,
                                 description=flat.description,
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
                                 photosListUrls=flat.photosListUrls,
                                 sourceURL=flat.sourceURL,
                                 phoneImgURL=flat.phoneImgURL)
        qew = """INSERT INTO apartments (Name, Author, Price, Phone, Description, DateCreated, DateActualTo, 
        IsActive, IsDonated, DonateDueDate, InternalComment, ClientId, ParsingSource, ShortId, SourceURL, 
        mainPhotoUrl, photosListUrls, phoneImgURL) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        asdf = (qew % (self.getValueOrNull(flat.name), self.getValueOrNull(flat.author),
                       self.getValueOrNull(flat.price), flat.phone, self.getValueOrNull(flat.description),
                       self.getValueOrNull(flat.creationDate), self.getValueOrNull(flat.actualToDate), flat.isActive,
                       flat.isDonated,
                       self.getValueOrNull(flat.donateDueDate), self.getValueOrNull(flat.internalComment),
                       flat.clientId,
                       flat.parsingSource,
                       self.getValueOrNull(flat.shortId), self.getValueOrNull(flat.mainPhotoUrl),
                       self.getValueOrNull(flat.photosListUrls), self.getValueOrNull(flat.sourceURL),
                       self.getValueOrNull(flat.phoneImgURL)))
        self.cursor.execute(asdf)
        self.con.commit()

    def get_apartments(self):
        """Method to get all apartments from BD"""
        self.cursor.execute('SELECT * FROM apartments')
        return self.cursor.fetchall()

    def get_exist_apartments_ids(self):
        """Method to get apartment's ids from BD"""
        self.cursor.execute('SELECT id FROM apartments')
        return [i[0] for i in self.cursor.fetchall()]

    def get_exist_apartments_short_ids(self):
        """Method to get apartment's ids from BD"""
        self.cursor.execute('SELECT ShortId FROM apartments')
        return [i[0] for i in self.cursor.fetchall()]

    def add_unpased_apartment(self, unparsed_flat):
        """Method to get all apartments from BD"""
        asd = """INSERT INTO UnparsedApartments (URL ,HTML ,ErrorDate ,Exception) 
                               VALUES ('{URL}', '{HTML}', '{ErrorDate}', '{Exception}')""".format(
            URL=unparsed_flat.URL,
            HTML=unparsed_flat.HTML,
            ErrorDate=unparsed_flat.ErrorDate,
            Exception=unparsed_flat.Exception)
        self.cursor.execute(asd)
        self.con.commit()

    def getValueOrNull(self, value):
        return "'" + value + "'" if value else "'" + str(value) + "'"
