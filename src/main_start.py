import sys

# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton

def main():
	app = QApplication(sys.argv)

	window = QWidget()
	window.setWindowTitle('PyQt5 App')
	window.setGeometry(100, 100, 280, 80)
	window.move(60, 15)

	helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
	helloMsg.move(60, 15)

	# layout = QHBoxLayout()
	# layout.addWidget(QPushButton('Left'))
	# layout.addWidget(QPushButton('Center'))
	# layout.addWidget(QPushButton('Right'))
	# window.setLayout(layout)


	# 4. Show your application's GUI
	window.show()

	# 5. Run your application's event loop (or main loop)
	sys.exit(app.exec_())



if __name__ == '__main__':
	main()