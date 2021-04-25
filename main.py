from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys
import subprocess

cmd = "ip -4 addr | grep -oP '(?<=inet\s)\d+(\.\d+){3}'"
#cmd2 = "ip -4 addr show wlan0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'"
temp = "hello"

def system_call(command):
    p = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    return p.stdout.read()

app = QApplication(sys.argv)
temp = system_call(cmd)
temp = str(temp,'utf-8')
temp = temp.replace("127.0.0.1\n", " ")
label = QLabel()
label.setText("ip: " + temp)
label.setGeometry(0,0,800,400)
label.setAlignment(QtCore.Qt.AlignCenter)
label.setStyleSheet("font: 18pt;")
label.show()
label.setWindowTitle("Afficheur IP")
sys.exit(app.exec_())
