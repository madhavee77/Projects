#Run this code in spyder(python 3.7). With software other than spyder, pyperclip1.3 and PyQt5 modules are required.

#passwordgenerator.py and words.txt file should be in same folder before running.

#All the classes run separately as they are not implemented together.

#To run the code, uncomment the these lines, at the end of the code, from one of the class which you have to run  

For Menu, uncomment these lines:
1. app = QApplication(sys.argv)
2. window = Menu()
3. window.setFixedSize(732, 120)
4. window.show()

For Pass-Phrase method, uncomment these lines:
1. window = PassPhrase_Generator()
2. window.setFixedSize(732, 120)
3. window.show()

For Person-Action-Object Method, uncomment these lines:
1. window = PersonActionMethod_PasswordGenerator()
2. window.setFixedSize(732, 300)
3. window.show()

For Randon Password Generator method, uncomment these lines:
1. window = RandomString_Generator()
2. window.setFixedSize(732, 120)
3. window.show()

