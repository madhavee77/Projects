

from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
import random
#import pyperclip
import webbrowser
import sys


WORDLIST_FILENAME = "words.txt"

class RandomString_Generator(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()

        self.menuBar = QMenuBar()
        self.default_characters = QPushButton()
        self.characters = QLineEdit()
        self.passwordlength = QLineEdit()
        self.pl_option = QComboBox()
        self.progress = QProgressBar()
        self.generate = QPushButton("Generate Password")
        self.result = QLineEdit()
#        self.clipboard = QPushButton("Copy to clipboard")
        self.clear = QPushButton("Clear")

        self.fileMenu = QMenu("File", self)
        self.clearAction = self.fileMenu.addAction("Clear")
        self.exitAction = self.fileMenu.addAction("Exit")
        self.menuBar.addMenu(self.fileMenu)
        self.helpMenu = QMenu("Help", self)
        self.source_code = self.helpMenu.addAction("Source Code")
        self.information = self.helpMenu.addAction("About Me")
        self.menuBar.addMenu(self.helpMenu)
        self.characters.setPlaceholderText("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890$@^`,|%;.~()/\{}:?[]=-+_#!")
        self.characters.setFixedWidth(524)
        self.passwordlength.setPlaceholderText("password length")
        self.passwordlength.setFixedWidth(85)
        self.passwordlength.setAlignment(Qt.AlignHCenter)
        self.passwordlength.setValidator(QIntValidator(0, 999))
        self.passwordlength.setMaxLength(3)
        self.pl_option.setFixedWidth(58)
        self.pl_option.addItems([ "8", "16", "32", "64", "128"])
        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)
        self.generate.setFixedWidth(125)
        self.default_characters.setFixedWidth(24)
#        self.default_characters.setIcon(QIcon(r'C:\Users\SalahGfx\Desktop\Password Generator Files\file-default-icon-62367.png'))
        self.result.setReadOnly(True)
        self.result.setFixedWidth(425)

        layout.addWidget(self.default_characters, 0, 0)
        layout.addWidget(self.characters, 0, 1, 1, 2)
        layout.addWidget(self.passwordlength, 0, 3)
        layout.addWidget(self.pl_option, 0, 4)
        layout.addWidget(self.generate, 1, 0, 1, 2)
        layout.addWidget(self.result, 1, 2)
        layout.addWidget(self.progress, 1, 3, 1, 2)
#        layout.addWidget(self.clipboard, 3, 0, 1, 3)
        layout.addWidget(self.clear, 3, 3, 1, 2)

        layout.setMenuBar(self.menuBar)
        self.setLayout(layout)
        self.setFocus()
        self.setWindowTitle("Random String Password Generator")

        self.generate.clicked.connect(self.generated)
#        self.clipboard.clicked.connect(self.clipboard_copy)
        self.clear.clicked.connect(self.cleared)
        self.default_characters.clicked.connect(self.default)
        self.pl_option.currentIndexChanged.connect(self.numbers)
        self.clearAction.triggered.connect(self.cleared)
        self.exitAction.triggered.connect(self.exit)
#        self.source_code.triggered.connect(self.get_source_code)
        self.information.triggered.connect(self.info_window)

        self.new_window = Info_Window()
#        self.new_window.setWindowIcon(QIcon(r'C:\Users\SalahGfx\Desktop\Password Generator Files\Lock_closed_key_2-512.png'))
        self.new_window.setWindowTitle("")



    def info_window(self):
        self.new_window.setWindowFlags(Qt.WindowCloseButtonHint)
        self.new_window.show()
        self.new_window.setFixedSize(665, 350)


    def exit(self):
        sys.exit(app.exec_())


    def numbers(self):
        if self.pl_option.currentText() == 'Default':
            self.passwordlength.setText(8)
        else:
            self.passwordlength.setText(self.pl_option.currentText())


    def default(self):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890$@^`,|%;.~()/\{}:?[]=-+_#!"
        self.characters.setText(characters)


    def generated(self):
        try:
            characters = self.characters.text()
            password_length = int(self.passwordlength.text())
        except Exception:
            return

        self.password = ""
        for i in range(password_length):
            try:
                characters_index = random.randrange(len(characters))
            except Exception:
                return
            self.password = self.password + characters[characters_index]
            self.progress.setValue(100)
        self.result.setText(self.password)




    def cleared(self):
        self.characters.setText("")
        self.passwordlength.setText("")
        self.progress.setValue(0)
        self.result.setText("")
        self.passwordlength.setText(None)
        self.pl_option.setCurrentIndex(0)


class Info_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        info_layout = QGridLayout()

        self.info = QLabel("Password Generator\n"
                           "Version 1.0\n"
                           )
        self.about_me = QLabel("")
        self.Font = QFont()
        self.Font.setBold(True)
        self.about_me.setFont(self.Font)
        self.Hline = QFrame()
        self.Hline.setFrameShape(self.Hline.HLine)
        self.Hline.setFrameShadow(self.Hline.Sunken)
        self.Vline = QFrame()
        self.Vline.setFrameShape(self.Vline.VLine)
        self.Vline.setFrameShadow(self.Vline.Sunken)
        self.image_label = QLabel()


        info_layout.addWidget(self.info, 0, 2)
        info_layout.addWidget(self.Vline, 0, 1)
        info_layout.addWidget(self.image_label, 0, 0)
        info_layout.addWidget(self.Hline, 1, 0, 1, 3)


        self.setLayout(info_layout)

class PassPhrase_Generator(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()

        self.menuBar = QMenuBar()
        self.default_characters = QPushButton()
        self.characters = QLineEdit()
        self.passwordlength = QLineEdit()
        self.pl_option = QComboBox()
        self.progress = QProgressBar()
        self.generate = QPushButton("Generate Password")
        self.result = QLineEdit()
#        self.clipboard = QPushButton("Copy to clipboard")
        self.clear = QPushButton("Clear")

        self.fileMenu = QMenu("File", self)
        self.clearAction = self.fileMenu.addAction("Clear")
        self.exitAction = self.fileMenu.addAction("Exit")
        self.menuBar.addMenu(self.fileMenu)
        self.helpMenu = QMenu("Help", self)
#        self.source_code = self.helpMenu.addAction("Source Code")
#        self.information = self.helpMenu.addAction("About Me")
#        self.menuBar.addMenu(self.helpMenu)
#        self.characters.setPlaceholderText("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890$@^`,|%;.~()/\{}:?[]=-+_#!")
        self.characters.setFixedWidth(524)
        self.passwordlength.setPlaceholderText("Enter length")
        self.passwordlength.setFixedWidth(85)
        self.passwordlength.setAlignment(Qt.AlignHCenter)
        self.passwordlength.setValidator(QIntValidator(0, 999))
        self.passwordlength.setMaxLength(3)
        self.pl_option.setFixedWidth(58)
        self.pl_option.addItems([ "Default","8", "16", "32", "64", "128"])
        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)
        self.generate.setFixedWidth(125)
        self.default_characters.setFixedWidth(24)
#        self.default_characters.setIcon(QIcon(r'C:\Users\SalahGfx\Desktop\Password Generator Files\file-default-icon-62367.png'))
        self.result.setReadOnly(True)
        self.result.setFixedWidth(425)

        layout.addWidget(self.default_characters, 0, 0)
        layout.addWidget(self.characters, 0, 1, 1, 2)
        layout.addWidget(self.passwordlength, 0, 3)
        layout.addWidget(self.pl_option, 0, 4)
        layout.addWidget(self.generate, 1, 0, 1, 2)
        layout.addWidget(self.result, 1, 2)
        layout.addWidget(self.progress, 1, 3, 1, 2)
#        layout.addWidget(self.clipboard, 3, 0, 1, 3)
        layout.addWidget(self.clear, 3, 3, 1, 2)

        layout.setMenuBar(self.menuBar)
        self.setLayout(layout)
        self.setFocus()
        self.setWindowTitle("Pass Phrase Password Generator")

        self.generate.clicked.connect(self.generated)
#        self.clipboard.clicked.connect(self.clipboard_copy)
        self.clear.clicked.connect(self.cleared)
        self.default_characters.clicked.connect(self.default)
        self.pl_option.currentIndexChanged.connect(self.numbers)
        self.clearAction.triggered.connect(self.cleared)
        self.exitAction.triggered.connect(self.exit)
#        self.source_code.triggered.connect(self.get_source_code)


        self.new_window = Info_Window()
#        self.new_window.setWindowIcon(QIcon(r'C:\Users\SalahGfx\Desktop\Password Generator Files\Lock_closed_key_2-512.png'))
        self.new_window.setWindowTitle("")

    def load_words(self):
  
    # inFile: file
        inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
        line = inFile.readline()
    # wordlist: list of strings
        wordlist = line.split()
       
        return wordlist

    def choose_word(self):
        wordlist=self.load_words()
        return random.choice(wordlist)

    def info_window(self):
        self.new_window.setWindowFlags(Qt.WindowCloseButtonHint)
        self.new_window.show()
        self.new_window.setFixedSize(665, 350)


    def exit(self):
        sys.exit(app.exec_())


    def numbers(self):
        if self.pl_option.currentText() == 'Default':
            self.passwordlength.setText("8")
        else:
            self.passwordlength.setText(self.pl_option.currentText())


    def default(self):
#        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890$@^`,|%;.~()/\{}:?[]=-+_#!"
        random_word_1= self.choose_word();
        random_word_2= self.choose_word();
        random_word_3= self.choose_word();
#        concatenated_str="1234567890"+random_word_1+random_word_2+random_word_3+"$@^`,|%;.~()/\{}:?[]=-+_#!";
        concatenated_str=random_word_1+random_word_2+random_word_3;
#        print (concatenated_str);
        self.characters.setText(concatenated_str)


    def generated(self):
        try:
            characters = self.characters.text()
            password_length = int(self.passwordlength.text())
        except Exception:
            return

        self.password = ""
        for i in range(password_length):
            try:
                characters_index = random.randrange(len(characters))
            except Exception:
                return
            self.password = self.password + characters[characters_index]
            self.progress.setValue(100)
        self.result.setText(self.password)




    def cleared(self):
        self.characters.setText("")
        self.passwordlength.setText("")
        self.progress.setValue(0)
        self.result.setText("")
        self.passwordlength.setText(None)
        self.pl_option.setCurrentIndex(0)
        

class PersonActionMethod_PasswordGenerator(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
#
        self.menuBar = QMenuBar()
#        self.default_characters = QPushButton()
        self.person = QLineEdit()
        self.action = QLineEdit()
        self.object = QLineEdit()
        self.passwordlength = QLineEdit()
        self.pl_option = QComboBox()
        self.progress = QProgressBar()
        self.generate = QPushButton("Generate Password")
        self.result = QLineEdit()
#        self.clipboard = QPushButton("Copy to clipboard")
        self.clear = QPushButton("Clear")
        self.person.setPlaceholderText("Choose a person")
        self.action.setPlaceholderText("Choose an action")
        self.object.setPlaceholderText("Choose an object")
        self.fileMenu = QMenu("File", self)
        self.clearAction = self.fileMenu.addAction("Clear")
        self.exitAction = self.fileMenu.addAction("Exit")
        self.menuBar.addMenu(self.fileMenu)
        self.helpMenu = QMenu("Help", self)
#        self.source_code = self.helpMenu.addAction("Source Code")
#        self.information = self.helpMenu.addAction("About Me")
#        self.menuBar.addMenu(self.helpMenu)
#        self.characters.setPlaceholderText("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890$@^`,|%;.~()/\{}:?[]=-+_#!")
#        self.person.setFixedWidth(524)
        self.passwordlength.setPlaceholderText("Enter length")
        self.passwordlength.setFixedWidth(85)
        self.passwordlength.setAlignment(Qt.AlignHCenter)
        self.passwordlength.setValidator(QIntValidator(0, 999))
        self.passwordlength.setMaxLength(3)
        self.pl_option.setFixedWidth(58)
        self.pl_option.addItems([ "Default","8", "16", "32", "64", "128"])
        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)
        self.generate.setFixedWidth(125)
#        self.default_characters.setFixedWidth(24)
#        self.default_characters.setIcon(QIcon(r'C:\Users\SalahGfx\Desktop\Password Generator Files\file-default-icon-62367.png'))
        self.result.setReadOnly(True)
        self.result.setFixedWidth(425)
#
#        layout.addWidget(self.default_characters, 0, 0)
        layout.addWidget(self.person, 0, 0, 1, 2)
        layout.addWidget(self.action, 1, 0, 1, 2)
        layout.addWidget(self.object, 2, 0, 1, 2)
        layout.addWidget(self.passwordlength, 0, 3)
        layout.addWidget(self.pl_option, 0, 4)
        layout.addWidget(self.generate, 3, 3, 1, 2 )
        layout.addWidget(self.result, 3, 2)
        layout.addWidget(self.progress, 1, 3, 1, 2)
#        layout.addWidget(self.clipboard, 3, 0, 1, 3)
        layout.addWidget(self.clear,3, 0, 1, 2)

        layout.setMenuBar(self.menuBar)
        self.setLayout(layout)
        self.setFocus()
        self.setWindowTitle("Pass Phrase Password Generator")

        self.generate.clicked.connect(self.generated)
#        self.clipboard.clicked.connect(self.clipboard_copy)
        self.clear.clicked.connect(self.cleared)
#        self.default_characters.clicked.connect(self.default)
        self.pl_option.currentIndexChanged.connect(self.numbers)
        self.clearAction.triggered.connect(self.cleared)
        self.exitAction.triggered.connect(self.exit)
#        self.source_code.triggered.connect(self.get_source_code)


        self.new_window = Info_Window()
#        self.new_window.setWindowIcon(QIcon(r'C:\Users\SalahGfx\Desktop\Password Generator Files\Lock_closed_key_2-512.png'))
        self.new_window.setWindowTitle("")

    def load_words(self):
  
    # inFile: file
        inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
        line = inFile.readline()
    # wordlist: list of strings
        wordlist = line.split()
       
        return wordlist

    def choose_word(self):
        wordlist=self.load_words()
        return random.choice(wordlist)

    def info_window(self):
        self.new_window.setWindowFlags(Qt.WindowCloseButtonHint)
        self.new_window.show()
        self.new_window.setFixedSize(665, 350)


    def exit(self):
        sys.exit(app.exec_())


    def numbers(self):
        if self.pl_option.currentText() == 'Default':
            self.passwordlength.setText("8")
        else:
            self.passwordlength.setText(self.pl_option.currentText())

#
    def default(self):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890$@^`,|%;.~()/\{}:?[]=-+_#!"
        random_word_1= self.choose_word();
        random_word_2= self.choose_word();
        random_word_3= self.choose_word();
        concatenated_str="1234567890"+random_word_1+random_word_2+random_word_3+"$@^`,|%;.~()/\{}:?[]=-+_#!";
        concatenated_str=random_word_1+random_word_2+random_word_3;
        print (concatenated_str);
        self.person.setText(concatenated_str)


    def generated(self):
        try:
            person = self.person.text()
            password_length = int(self.passwordlength.text())
        except Exception:
            return

        self.password = ""
        for i in range(password_length):
            try:
                person_index = random.randrange(len(person))
            except Exception:
                return
            self.password = self.password + person[person_index]
            self.progress.setValue(100)
        self.result.setText(self.password)


#    def clipboard_copy(self):
#        if len(self.result.text()) > 0:
#            pyperclip.copy(self.result.text())
#            QMessageBox.information(self, "Information", "Password has been copied to clipboard!")
#        else:
#            return


    def cleared(self):
        self.person.setText("")
        self.passwordlength.setText("")
        self.progress.setValue(0)
        self.result.setText("")
        self.passwordlength.setText(None)
        self.pl_option.setCurrentIndex(0)
        
class Menu(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.menuBar = QMenuBar()
      
        self.fileMenu = QMenu("File", self)
        self.clearAction = self.fileMenu.addAction("Clear")
        self.exitAction = self.fileMenu.addAction("Exit")
        self.generator_type_1 = QRadioButton("Random Password Generator");
        self.generator_type_2 = QRadioButton("Pass Phrase Password Generator");
        self.generator_type_3 = QRadioButton("Person-Action-Object Password Generator");
        if self.generator_type_1.isChecked() == True:
            print ("SELECTED METHOD 1");
            window = Password_Generator()
            window.setFixedSize(732, 120)

            window.show()
     
            
		
        self.generate = QPushButton("Select")
       
        layout.addWidget(self.generator_type_1, 0, 0)
   

       
        layout.addWidget(self.generate, 1, 2)
#        layout.addWidget(self.progress, 1, 3, 1, 2)
#        layout.addWidget(self.clipboard, 3, 0, 1, 3)
     
        layout.addWidget(self.generator_type_2, 1, 0, 1, 2)
        layout.addWidget(self.generator_type_3, 2, 0, 1, 2)

        layout.setMenuBar(self.menuBar)
#        self.generate.clicked.connect(self.type_1(self.generator_type_1))
        self.setLayout(layout)
        self.setFocus()
        self.setWindowTitle("Password Generator")


        self.new_window = Info_Window()
#        self.new_window.setWindowIcon(QIcon(r'C:\Users\SalahGfx\Desktop\Password Generator Files\Lock_closed_key_2-512.png'))
        self.new_window.setWindowTitle("")
    
    def info_window(self):
        self.new_window.setWindowFlags(Qt.WindowCloseButtonHint)
        self.new_window.show()
        self.new_window.setFixedSize(665, 350)
#
    def type_1(self,generator_type_1):
        try:
            if generator_type_1.isChecked() == True:
                    window = Password_Generator()
                    window.setFixedSize(732, 120)

                    window.show()
#      
        except Exception:
            return False

    def exit(self):
        sys.exit(app.exec_())
        

app = QApplication(sys.argv)

window = Menu()
window.setFixedSize(732, 120)
window.show()
#
window = PassPhrase_Generator()
window.setFixedSize(732, 120)
window.setWindowIcon(QIcon(r'C:\Users\SalahGfx\Desktop\Password Generator Files\Lock_closed_key_2-512.png'))
window.show()

window = PersonActionMethod_PasswordGenerator()
window.setFixedSize(732, 300)
window.setWindowIcon(QIcon(r'C:\Users\SalahGfx\Desktop\Password Generator Files\Lock_closed_key_2-512.png'))
window.show()
        
window = RandomString_Generator()
window.setFixedSize(732, 120)
window.setWindowIcon(QIcon(r'C:\Users\SalahGfx\Desktop\Password Generator Files\Lock_closed_key_2-512.png'))
window.show()

sys.exit(app.exec_())