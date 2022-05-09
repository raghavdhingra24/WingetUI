import sys, os, darkdetect, qtmodern.styles, win32mica
from PySide2 import QtWidgets, QtCore, QtGui
import MainWindow, Tools

if hasattr(sys, 'frozen'):
    realpath = sys._MEIPASS
else:
    realpath = '/'.join(sys.argv[0].replace("\\", "/").split("/")[:-1])



debugging = True

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class MainApplication(QtWidgets.QApplication):
    def __init__(self):
        try:
            super().__init__(sys.argv)
            print("[        ] Starting main application...")


            os.chdir(os.path.expanduser("~"))

            self.window = MainWindow.MainWindow()

            self.trayIcon = QtWidgets.QSystemTrayIcon()

            Tools.registerApplication(self)
            self.trayIcon.setIcon(QtGui.QIcon(realpath+"/icon.png"))
            self.trayIcon.setToolTip("WingetUI Store")
            self.trayIcon.setVisible(True)

            
            if(darkdetect.isDark()):
                qtmodern.styles.light(self)
                win32mica.ApplyMica(self.window.winId(), win32mica.MICAMODE.LIGHT)
            else:
                self.window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
                self.setStyle("fusion")
                win32mica.ApplyMica(self.window.winId(), win32mica.MICAMODE.DARK)
                self.setStyleSheet(darkSS)
            

        

            self.exec_()
        except Exception as e:
            if(debugging):
                raise e


colors = Tools.getColors()

darkSS = f"""
* {{
    background-color: transparent;
    color: #eeeeee;
    font-family: "Segoe UI Variable Display semib"
}}

QPushButton,#FocusLabel {{
    width: 150px;
    background-color:rgba(81, 81, 81, 25%);
    border-radius: 6px;
    border: 1px solid rgba(86, 86, 86, 25%);
    height: 25px;
    font-size: 10pt;
    border-top: 1px solid rgba(99, 99, 99, 25%);
}}
QPushButton:hover {{
    background-color:rgba(86, 86, 86, 25%);
    border-radius: 6px;
    border: 1px solid rgba(100, 100, 100, 25%);
    height: 30px;
    border-top: 1px solid rgba(107, 107, 107, 25%);
}}

QLineEdit {{
    background-color: rgba(81, 81, 81, 25%);
    font-family: "Segoe UI Variable Display";
    font-size: 9pt;
    width: 300px;
    padding: 5px;
    border-radius: 6px;
    border: 0.6px solid rgba(86, 86, 86, 25%);
    border-bottom: 2px solid rgb({colors[4]});
}}
QLineEdit:disabled {{
    background-color: rgba(81, 81, 81, 25%);
    font-family: "Segoe UI Variable Display";
    font-size: 9pt;
    width: 300px;
    padding: 5px;
    border-radius: 6px;
    border: 0.6px solid rgba(86, 86, 86, 25%);
}}

QScrollBar:vertical {{
    background: transparent;
    border: 1px solid #1f1f1f;
    margin: 3px;
    width: 18px;
    border: none;
    border-radius: 4px;
}}
QScrollBar::handle {{
    margin: 3px;
    min-height: 20px;
    min-width: 20px;
    border-radius: 3px;
    background: #505050;
}}
QScrollBar::handle:hover {{
    margin: 3px;
    border-radius: 3px;
    background: #808080;
}}
QScrollBar::add-line {{
    height: 0;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}}
QScrollBar::sub-line {{
    height: 0;
    subcontrol-position: top;
    subcontrol-origin: margin;
}}
QScrollBar::up-arrow, QScrollBar::down-arrow {{
    background: none;
}}
QScrollBar::add-page, QScrollBar::sub-page {{
    background: none;
}}
QHeaderView,QAbstractItemView {{
    background-color: #55303030;
    border-radius: 6px;
    border: none;
    padding: 1px;
    height: 25px;
    border: 1px solid #1f1f1f;
    margin-bottom: 5px;
}}
QHeaderView::section {{
    background-color: transparent;
    border-radius: 6px;
    padding: 4px;
    height: 25px;
    margin: 1px;
}}
QTreeWidget {{
    show-decoration-selected: 0;
    background-color: transparent;
    padding: 5px;
    border-radius: 6px;
    border: 0px solid #1f1f1f;
}}
QTreeWidget::item {{
    margin-top: 3px;
    margin-bottom: 3px;
    padding-top: 3px;
    padding-bottom: 3px;
    outline: none;
    background-color: #55303030;
    height: 25px;
    border-bottom: 1px solid #1f1f1f;
    border-top: 1px solid #1f1f1f;
}}
QTreeWidget::item:selected {{
    margin-top: 2px;
    margin-bottom: 2px;
    padding: 0px;
    padding-top: 3px;
    padding-bottom: 3px;
    outline: none;
    background-color: #77303030;
    height: 25px;
    border-bottom: 1px solid #393939;
    border-top: 1px solid #404040;
}}
QTreeWidget::item:hover {{
    margin-top: 2px;
    margin-bottom: 2px;
    padding: 0px;
    padding-top: 3px;
    padding-bottom: 3px;
    outline: none;
    background-color: #88343434;
    height: 25px;
    border-bottom: 1px solid #393939;
    border-top: 1px solid #404040;
}}
QTreeWidget::item:first {{
    border-top-left-radius: 6px;
    border-bottom-left-radius: 6px;
    border-left: 1px solid #1f1f1f;
}}
QTreeWidget::item:last {{
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
    border-right: 1px solid #1f1f1f;
}}
QTreeWidget::item:first:selected {{
    border-left: 1px solid #393939;
}}
QTreeWidget::item:last:selected {{
    border-right: 1px solid #393939;
}}
QTreeWidget::item:first:hover {{
    border-left: 1px solid #393939;
}}
QTreeWidget::item:last:hover {{
    border-right: 1px solid #393939;
}}
QProgressBar {{
    border-radius: 2px;
    height: 4px;
    border: 0px;
}}
QProgressBar::chunk {{
    background-color: rgb({colors[4]});
    border-radius: 2px;
}}
"""


MainApplication()