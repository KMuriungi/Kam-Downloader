from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

#import urllib.request # ONLY PRESENT IN Python 3 (URL handler)
from urllib import *

class kamDownloader(QDialog):
    def __init__(self): # initializing or calling the constractor
        QDialog.__init__(self)

        QDialog.resize(self, 320, 240)

        self.setWindowTitle("KamDownloader")
        self.setWindowIcon(QIcon('Icons/WindowTitleIcon.png'))

        #self.palette = QPalette()
        #self.palette.setBrush(QPalette.Background, QBrush(QPixmap("windows8.jpg")))
        #QDialog.setPalette(self.palette)

        self.setFocus()

        myLayout = QGridLayout()


        self.myUrl= QLineEdit()
        self.saveLocation = QLineEdit()
        bnSaveAS = QPushButton("Browse Save Location")
        bnSaveAS.setIcon(QIcon('Icons/saveAS.png'))
        self.progressBar = QProgressBar()
        bnPause = QPushButton("Pause")
        bnPause.setIcon(QIcon('Icons/Pause.png'))
        bnDownload = QPushButton("Download")
        bnDownload.setIcon(QIcon('Icons/Download.png'))
        bnCancel = QPushButton('Cancel')
        bnCancel.setIcon(QIcon('Icons/Cancel.png'))

        self.myUrl.setPlaceholderText("URL")
        self.myUrl.setAlignment(Qt.AlignHCenter)
        self.saveLocation.setPlaceholderText("File Save Location")
        self.saveLocation.setAlignment(Qt.AlignHCenter)

        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignHCenter)

        myLayout.addWidget(self.myUrl, 0, 0, 1, 3)
        myLayout.addWidget(self.saveLocation, 1, 0, 1, 3)
        myLayout.addWidget(bnSaveAS, 2, 1)
        myLayout.addWidget(self.progressBar, 3, 0, 1, 3)

        myLayout.addWidget(bnPause, 4, 0)
        myLayout.addWidget(bnDownload, 4, 1)
        myLayout.addWidget(bnCancel, 4, 2)

        self.setLayout(myLayout)

        bnDownload.clicked.connect(self.bnDownload)
        bnSaveAS.clicked.connect(self.checkFile)
        #bnPause.clicked.connect(self.pause)
        bnCancel.clicked.connect(self.close)


        #self.Status()
   # def Status(self):
       # self.setStatusTip("Ready")
       # self.show()

    def checkFile(self):
        saveFile = QFileDialog.getSaveFileName(self, caption="Save File As", directory=".", filter="All Files (*.*)")
        self.saveLocation.setText(QDir.toNativeSeparators(saveFile))

    def bnDownload(self):
        myUrl = self.myUrl.text()
        saveLocation = self.saveLocation.text()
        try:
            urllib.request.urlretrieve(myUrl, saveLocation,self.report)
        except Exception:
            QMessageBox.warning(self, "Warning!!!", "Error occurred while downloading your file. Use a Valid URL.")
            return

        QMessageBox.Information(self, " Download Message", "Your File has finished downloading successfully !!!")
        self.progressBar.setValue(0)
        self.myUrl.setText("")
        self.saveLocation.setText("")

    def report(self, blockNum, blockSize, totalSize):
        currentValue = blockNum * blockSize
        if totalSize > 0:
            percent = currentValue * 100 / totalSize
            self.progressBar.setValue(int (percent))

App = QApplication(sys.argv)
Dialog = kamDownloader()
Dialog.show()
sys.exit(App.exec_())
