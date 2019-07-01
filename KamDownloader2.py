import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#import urllib.request # ONLY PRESENT IN Python 3 (URL handler)
from urllib import *

class myWindow(QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        #QMainWindow.__init__(self)

        #QMainWindow.resize(self, 320, 240)

        self.setWindowTitle("KamsDownloader")
        self.setWindowIcon(QIcon('Icons/WindowTitleIcon.png'))

        myMenuBar = self.menuBar()

        file = myMenuBar.addMenu("File")
        #file.setShortcut("Alt+F")
        #file.QShortcut(QKeySequence("Alt+F"), self, self.close)
        file.addAction("New")
        save = QAction("Save", self)
        #save.setShortcut("Ctrl+S")
        file.addAction(save)
        quit = QAction("Quit", self)
        file.addAction(quit)
        #file.triggered[QAction].connect(self.processtrigger)

        downloads = myMenuBar.addMenu("Downloads")
        #downloads.setShortcut("Alt+D")
        paste = QAction("Paste Link", self)
        #paste.setShortcut("Ctrl+V")
        downloads.addAction(paste)
        pause = QAction("Pause All", self)
        #pause.setShortcut("Ctrl+H")
        downloads.addAction(pause)
        resume = QAction("Resume All", self)
        #resume.setShortcut("Ctrl+R")
        downloads.addAction(resume)
        downloads.addAction("Remove All")
        remove = QAction("Remove All", self)
        #remove.setShortcut("Ctrl+X")
        downloads.addAction(remove)
        #downloads.triggered[QAction].connect(self.processtrigger)

        tools = myMenuBar.addMenu("Tools")
        #tools.setShortcut("Alt+T")
        preferences = QAction("Preferences", self)
        #preferences.setShortcut("Ctrl+Shift+P")
        tools.addAction(preferences)
        generalSettings = QAction("General Settings", self)
        #generalSettings.setShortcut("Ctrl+Shift+S")
        tools.addAction(generalSettings)
        #tools.triggered[QAction].connect(self.processtrigger)

        help = myMenuBar.addMenu("Help")
        #help.setShortcut("Alt+H")
        helpCenter = QAction("Help Center", self)
        #helpCenter.setShortcut("F1")
        help.addAction(helpCenter)
        feedback = QAction("Feedback", self)
        #feedback.setShortcut("F2")
        help.addAction(feedback)
        about = QAction("About", self)
        #about.setShortcut("F9")
        help.addAction(about)
        #help.triggered[QAction].connect(self.processtrigger)

        self.setFocus()

        myWidget = QWidget(self)
        self.setCentralWidget(myWidget)
        myLayout = QGridLayout()
        myWidget.setLayout(myLayout)

        self.myUrl = QLineEdit()
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

        #myWidget.setLayout(myLayout)

        bnDownload.clicked.connect(self.bnDownload)
        bnSaveAS.clicked.connect(self.checkFile)
        # bnPause.clicked.connect(self.pause)
        bnCancel.clicked.connect(self.close) # Supposed to Cancel the Download not Close the Entire App


        # self.Status()
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
            urllib.request.urlretrieve(myUrl, saveLocation, self.report)
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
            self.progressBar.setValue(int(percent))

app = QApplication(sys.argv)
Gui = myWindow()
Gui.show()
sys.exit(app.exec_())