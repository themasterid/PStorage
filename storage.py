from pysqlcipher3 import dbapi2 as sqlite3
import json
from myui import Ui_MyWindow
from PyQt5 import QtWidgets
import sys
from funcs.functions import hide_text_from_changes, btns_edit_click, btns_save_click


class SoyleWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(SoyleWindow, self).__init__()
        self.ui = Ui_MyWindow()
        self.ui.setupUi(self)

        self.connDB()  # decrypt the table using the key
        # Create table first, second comment this strings in the future, 
        # do not download data from json, but through the GUI form.
        # self.create_table_new('db.json')        
        self.ui.listWidget.setCurrentRow(0)
        self.ui.listWidget.addItems(self.get_items_names())
        hide_text_from_changes(self)
        self.ui.listWidget.currentRowChanged.connect(self.click)
        btns_edit_click(self) # edit from base
        btns_save_click(self) # save in base
        self.cur.close()

    # decrypt the table using the key
    def connDB(self):
        self.conn = sqlite3.connect('db.sqlite')
        self.cur = self.conn.cursor()
        self.cur.execute("PRAGMA key='secretmegasecretkey12345'")

    # get name who send signal on press btn
    def who_btn_clicked(self):
        sender = self.sender()  # who send signal
        if sender.objectName() == 'pushButton_Name_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Name.setDisabled(False)
        elif sender.objectName() == 'pushButton_Login_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Login.setDisabled(False)
        elif sender.objectName() == 'pushButton_Password_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Password.setDisabled(False)
        elif sender.objectName() == 'pushButton_OldPassword_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_OldPassword.setDisabled(False)
        elif sender.objectName() == 'pushButton_Email_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Email.setDisabled(False)
        elif sender.objectName() == 'pushButton_OldEmail_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_OldEmail.setDisabled(False)
        elif sender.objectName() == 'pushButton_Quation_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Quation.setDisabled(False)
        elif sender.objectName() == 'pushButton_Answer_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Answer.setDisabled(False)
        elif sender.objectName() == 'pushButton_Code_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Code.setDisabled(False)
        elif sender.objectName() == 'pushButton_Phone_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Phone.setDisabled(False)
        elif sender.objectName() == 'pushButton_Recoverycode_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Recoverycode.setDisabled(False)
        elif sender.objectName() == 'pushButton_FIO_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_FIO.setDisabled(False)
        elif sender.objectName() == 'pushButton_Country_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Country.setDisabled(False)
        elif sender.objectName() == 'pushButton_State_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_State.setDisabled(False)
        elif sender.objectName() == 'pushButton_City_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_City.setDisabled(False)
        elif sender.objectName() == 'pushButton_Addres_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Addres.setDisabled(False)
        elif sender.objectName() == 'pushButton_ZipCode_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_ZipCode.setDisabled(False)

    def update_table(self):
        hide_text_from_changes(self)
        rows = self.ui.listWidget.currentRow()
        texts = self.view_table_by_IDs(str(rows))
        new_names_text = tuple()
        new_names_text += (rows,)
        new_names_text += (self.ui.textEdit_Name.toPlainText(),)
        new_names_text += (self.ui.textEdit_Login.toPlainText(),)
        new_names_text += (self.ui.textEdit_Password.toPlainText(),)
        new_names_text += (self.ui.textEdit_OldPassword.toPlainText(),)
        new_names_text += (self.ui.textEdit_Email.toPlainText(),)
        new_names_text += (self.ui.textEdit_OldEmail.toPlainText(),)
        new_names_text += (self.ui.textEdit_Quation.toPlainText(),)
        new_names_text += (self.ui.textEdit_Answer.toPlainText(),)
        new_names_text += (self.ui.textEdit_Code.toPlainText(),)
        new_names_text += (self.ui.textEdit_Phone.toPlainText(),)
        new_names_text += (self.ui.textEdit_Recoverycode.toPlainText(),)
        new_names_text += (self.ui.textEdit_FIO.toPlainText(),)
        new_names_text += (self.ui.textEdit_Country.toPlainText(),)
        new_names_text += (self.ui.textEdit_State.toPlainText(),)
        new_names_text += (self.ui.textEdit_City.toPlainText(),)
        new_names_text += (self.ui.textEdit_Addres.toPlainText(),)
        new_names_text += (self.ui.textEdit_ZipCode.toPlainText(),)
        if [new_names_text] == texts:
            self.statusBar().showMessage('Изменения не внесены')
        else:
            self.update_to_table(new_names_text)
            sender = self.sender()
            self.statusBar().showMessage('Изменения внесены ' +
                                         str(sender.objectName().split('_')[1]))

    def update_to_table(self, new_names_text):
        self.cur = self.conn.cursor()
        rows = self.ui.listWidget.currentRow()
        update = '''UPDATE db SET
        id = '{0}', 
        Name = '{1}',
        Login = '{2}',
        Password = '{3}',
        OldPassword = '{4}',
        Email = '{5}',
        OldEmail = '{6}',
        Quation = '{7}',
        Answer = "{8}",
        Code = '{9}',
        Phone = '{10}',
        Recoverycode = '{11}',
        FIO = '{12}',
        Country = '{13}',
        State = '{14}',
        City = '{15}',
        Addres = '{16}',
        ZipCode = '{17}'  
        WHERE 
        ID == {18};
        '''.format(
            new_names_text[0],
            new_names_text[1],
            new_names_text[2],
            new_names_text[3],
            new_names_text[4],
            new_names_text[5],
            new_names_text[6],
            new_names_text[7],
            new_names_text[8],
            new_names_text[9],
            new_names_text[10],
            new_names_text[11],
            new_names_text[12],
            new_names_text[13],
            new_names_text[14],
            new_names_text[15],
            new_names_text[16],
            new_names_text[17],
            rows)
        self.cur.execute(update)
        self.conn.commit()

    # Get items name
    def get_items_names(self):
        self.cur.execute("SELECT Name, Login FROM db;")
        get_name = self.cur.fetchmany(0)
        list_names = []
        for _ in range(len(get_name)):
            list_names.append(get_name[_][0] + " (" + get_name[_][1] + ")")
        return list_names

    def click(self):
        hide_text_from_changes(self)
        rows = self.ui.listWidget.currentRow()
        texts = self.view_table_by_IDs(str(rows))
        self.ui.textEdit_Name.setPlainText(texts[0][1])
        self.ui.textEdit_Login.setPlainText(texts[0][2])
        self.ui.textEdit_Password.setPlainText(texts[0][3])
        self.ui.textEdit_OldPassword.setPlainText(texts[0][4])
        self.ui.textEdit_Email.setPlainText(texts[0][5])
        self.ui.textEdit_OldEmail.setPlainText(texts[0][6])
        self.ui.textEdit_Quation.setPlainText(texts[0][7])
        self.ui.textEdit_Answer.setPlainText(texts[0][8])
        self.ui.textEdit_Code.setPlainText(texts[0][9])
        self.ui.textEdit_Phone.setPlainText(texts[0][10])
        self.ui.textEdit_Recoverycode.setPlainText(texts[0][11])
        self.ui.textEdit_FIO.setPlainText(texts[0][12])
        self.ui.textEdit_Country.setPlainText(texts[0][13])
        self.ui.textEdit_State.setPlainText(texts[0][14])
        self.ui.textEdit_City.setPlainText(texts[0][15])
        self.ui.textEdit_Addres.setPlainText(texts[0][16])
        self.ui.textEdit_ZipCode.setPlainText(texts[0][17])

    def view_table_by_IDs(self, name):
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM db WHERE ID = '{0}';".format(name))
        return self.cur.fetchmany(0)

    def open_json_file(self, fname):
        self.fname = fname
        with open(self.fname, 'r', encoding='utf-8') as read_json_file:
            data_json = json.load(read_json_file)
            read_json_file.close()
        return data_json

    def create_table_new(self, fname):
        self.cur.execute('DROP TABLE IF EXISTS db')
        self.cur.execute(
            '''CREATE TABLE db (
            id INT AUTO_INCREMENT NOT NULL, Name VARCHAR(100), Login VARCHAR(100), Password VARCHAR(100), OldPassword VARCHAR(100), Email VARCHAR(300),
            OldEmail VARCHAR(100), Quation VARCHAR(300), Answer VARCHAR(300), Code VARCHAR(300), Phone VARCHAR(20), Recoverycode VARCHAR(300), 
            FIO VARCHAR(300), Country VARCHAR(100), State VARCHAR(100), City VARCHAR(100), Addres VARCHAR(300), ZipCode VARCHAR(50),
            PRIMARY KEY (id)
            );'''
        )
        self.conn.commit()
        fh = self.open_json_file(fname)
        for key, _ in fh.items():
            Name = fh[key][0]['Name']
            Login = fh[key][0]['Login']
            Password = fh[key][0]['Password']
            OldPassword = fh[key][0]["Old Password"]
            Email = fh[key][0]["Email"]
            OldEmail = fh[key][0]["Old Email"]
            Quation = fh[key][0]["Quation"]
            Answer = fh[key][0]["Answer"]
            Code = fh[key][0]["Code"]
            Phone = fh[key][0]["Phone"]
            Recoverycode = fh[key][0]["Recovery code"]
            FIO = fh[key][0]["FIO"]
            Country = fh[key][0]["Country"]
            State = fh[key][0]["State"]
            City = fh[key][0]["City"]
            Addres = fh[key][0]["Addres"]
            ZipCode = fh[key][0]["Zip Code"]
            self.cur.execute(
                '''INSERT INTO db ( id, Name, Login, Password, OldPassword, Email, OldEmail, Quation, Answer, Code, Phone, Recoverycode, FIO, Country, State, City, Addres, ZipCode ) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? );''',
                (int(key), Name, Login, Password, OldPassword, Email, OldEmail, Quation, Answer, Code, Phone, Recoverycode, FIO, Country, State, City, Addres, ZipCode))
        return self.conn.commit()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = SoyleWindow()
    application.show()
    sys.exit(app.exec())