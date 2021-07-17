from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys
import subprocess
import time

cmd = "ip -4 addr | grep -oP '(?<=inet\s)\d+(\.\d+){3}'"
#cmd2 = "ip -4 addr show wlan0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'"
temp = "hello"

def system_call(command):
    p = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    return p.stdout.read()

app = QApplication(sys.argv)
temp=""
while temp=="":
    temp1 = system_call(cmd)
    temp1 = str(temp1,'utf-8')
    temp = temp1.replace("127.0.0.1\n", "")
    time.sleep(5)

label = QLabel()
label.setText("ip: " + temp)
label.setGeometry(0,0,800,400)
label.setAlignment(QtCore.Qt.AlignCenter)
label.setStyleSheet("font: 18pt;")
label.show()
label.setWindowTitle("Afficheur IP")
sys.exit(app.exec_())pp.exec_())
