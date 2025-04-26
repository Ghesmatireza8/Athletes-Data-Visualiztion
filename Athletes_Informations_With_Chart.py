from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton, QLineEdit, QListWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import res


plt.rcParams.update({
    'axes.titlesize': 8,
    'axes.labelsize': 7,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'axes.labelcolor': 'white',
    'xtick.color': 'white',
    'ytick.color': 'white',
    'text.color': 'white',
    'figure.figsize': (2, 2),
    'axes.facecolor': (0,0,0,0),
    'figure.facecolor': '#094163',
    'lines.linewidth': 1,
})

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("Data_Visualization.ui", self)

        # Define Our Widgets
        # Define layouts for show charts
        self.layout1 = self.findChild(QVBoxLayout, "verticalLayout_3")
        self.layout2 = self.findChild(QVBoxLayout, "verticalLayout_4")
        self.layout3 = self.findChild(QVBoxLayout, "verticalLayout_5")
        self.layout4 = self.findChild(QVBoxLayout, "verticalLayout_6")

        # Define lineEdits for save new info of athletes in CSV
        self.lineEdit1 = self.findChild(QLineEdit, "lineEdit1")
        self.lineEdit2 = self.findChild(QLineEdit, "lineEdit2")
        self.lineEdit3 = self.findChild(QLineEdit, "lineEdit3")
        self.lineEdit4 = self.findChild(QLineEdit, "lineEdit4")
        self.lineEdit5 = self.findChild(QLineEdit, "lineEdit5")
        self.lineEdit6 = self.findChild(QLineEdit, "lineEdit6")
        self.lineEdit7 = self.findChild(QLineEdit, "lineEdit7")
        self.lineEdit8 = self.findChild(QLineEdit, "lineEdit8")
        self.lineEdit9 = self.findChild(QLineEdit, "lineEdit9")
        self.lineEdit10 = self.findChild(QLineEdit, "lineEdit10")
        self.lineEdit11 = self.findChild(QLineEdit, "lineEdit11")
        self.lineEdit12 = self.findChild(QLineEdit, "lineEdit12")
        self.lineEdit13 = self.findChild(QLineEdit, "lineEdit13")
        self.lineEdit14 = self.findChild(QLineEdit, "lineEdit14")

        # Define pushButtons
        self.info_save_bt = self.findChild(QPushButton, "info_save_bt")
        self.show_charts_bt = self.findChild(QPushButton, "show_charts_bt")
        self.show_data_bt = self.findChild(QPushButton, "show_data_bt")

        # Define QTableWidget
        self.tableWidget = self.findChild(QTableWidget, "tableWidget")

        # Define label
        self.label_info = self.findChild(QLabel, "label_info")


        # Do something
        self.info_save_bt.clicked.connect(self.info_save)
        self.show_data_bt.clicked.connect(self.show_data)
        self.show_charts_bt.clicked.connect(self.show_charts)

        # Show The App
        self.show()
        self.show_charts()



    def show_charts(self):
        self.chart1 = MplCanvas(self)
        self.chart2 = MplCanvas(self)
        self.chart3 = MplCanvas(self)
        self.chart4 = MplCanvas(self)
        data = pd.read_csv("realistic_athletes_dataset.csv")

        # for clear all layouts and set new chart
        self.layout1.takeAt(0)
        self.layout2.takeAt(0)
        self.layout3.takeAt(0)
        self.layout4.takeAt(0)


        # plot
        grouped = data.groupby('Daily_Training_Duration_min')['Body_Fat_Percentage'].mean().reset_index()
        self.chart1.ax.plot(grouped['Daily_Training_Duration_min'], grouped['Body_Fat_Percentage'], color='#96ba2a')
        self.chart1.ax.set_title("Mean of Daily Training Duration with Body Fat Percentage")
        self.chart1.ax.set_xlabel("Daily Training Duration (Min)")
        self.chart1.ax.set_ylabel("Body Fat Percentage")
        self.chart1.ax.spines['top'].set_color('white')
        self.chart1.ax.spines['bottom'].set_color('white')
        self.chart1.ax.spines['left'].set_color('white')
        self.chart1.ax.spines['right'].set_color('white')
        #self.chart1.ax.legend()
        self.chart1.draw()


        # scatter chart
        self.chart2.ax.scatter(data.Age, data.VO2_Max,
                                alpha=0.2,
                                s=data.Weekly_Training_Sessions * 10,
                                c=data.Years_of_Experience)
        self.chart2.ax.set_title("Age with VO2Max chart and color of points based Years of Experience")
        self.chart2.ax.set_xlabel("Age")
        self.chart2.ax.set_ylabel("VO2Max")
        self.chart2.ax.spines['top'].set_color('white')
        self.chart2.ax.spines['bottom'].set_color('white')
        self.chart2.ax.spines['left'].set_color('white')
        self.chart2.ax.spines['right'].set_color('white')
        self.chart2.ax.legend(title='Weekly Training Sessions', fontsize=4, title_fontsize=6)
        self.chart2.draw()


        # bar chart
        data_age = data.groupby('Age').Age.count()
        self.chart3.ax.bar(data_age.index, data_age, color='#96ba2a')
        self.chart3.ax.set_title("Age with count of age chart")
        self.chart3.ax.set_xlabel("Age")
        self.chart3.ax.set_ylabel("count of age")
        self.chart3.ax.spines['top'].set_color('white')
        self.chart3.ax.spines['bottom'].set_color('white')
        self.chart3.ax.spines['left'].set_color('white')
        self.chart3.ax.spines['right'].set_color('white')
        #self.chart3.ax.legend()
        self.chart3.draw()


        # pie chart
        data_sport = data['Sport'].value_counts()
        self.chart4.ax.pie(data_sport,
                            labels=data_sport.index,
                            explode=[0.1,0,0,0,0],
                            shadow=True,
                            autopct='%1.1f%%',
                            textprops={'fontsize': 11})
        self.chart4.ax.set_title("count of sports")
        #self.chart4.ax.legend()
        self.chart4.draw()


        self.layout1.addWidget(self.chart1)
        self.layout2.addWidget(self.chart2)
        self.layout3.addWidget(self.chart3)
        self.layout4.addWidget(self.chart4)




    def show_data(self):
        with open("realistic_athletes_dataset.csv", newline='', encoding='utf-8') as show_file:
            reader = csv.reader(show_file)
            data = list(reader)
            show_file.close()

        self.tableWidget.setRowCount(len(data) - 1)
        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setHorizontalHeaderLabels(data[0])

        for row_idx, row in enumerate(data[1:]):
            for col_idx, value in enumerate(row):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(value))



    def info_save(self):
        if self.lineEdit1.text() == "" or self.lineEdit2.text() == "" or self.lineEdit3.text() == "" or self.lineEdit4.text() == "" or self.lineEdit5.text() == "" or self.lineEdit6.text() == "" or self.lineEdit7.text() == "" or self.lineEdit8.text() == "" or self.lineEdit9.text() == "" or self.lineEdit10.text() == "" or self.lineEdit11.text() == "" or self.lineEdit12.text() == "" or self.lineEdit13.text() == "" or self.lineEdit14.text() == "":
            self.label_info.setText("Please inter info")
        else:
            line_1 = int(self.lineEdit1.text())
            line_2 = int(self.lineEdit2.text())
            line_3 = self.lineEdit3.text()
            line_4 = int(self.lineEdit4.text())
            line_5 = int(self.lineEdit5.text())
            line_6 = int(self.lineEdit6.text())
            line_7 = float(self.lineEdit7.text())
            line_8 = float(self.lineEdit8.text())
            line_9 = self.lineEdit9.text()
            line_10 = int(self.lineEdit10.text())
            line_11 = int(self.lineEdit11.text())
            line_12 = int(self.lineEdit12.text())
            line_13 = float(self.lineEdit13.text())
            line_14 = int(self.lineEdit14.text())

            with open("realistic_athletes_dataset.csv", "a", newline='', encoding='utf-8') as save_file:
                writer = csv.writer(save_file)
                writer.writerow([line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8, line_9, line_10, line_11, line_12, line_13, line_14])
                save_file.close()


            self.label_info.setText("Data Saved")
            self.lineEdit1.setText("")
            self.lineEdit2.setText("")
            self.lineEdit3.setText("")
            self.lineEdit4.setText("")
            self.lineEdit5.setText("")
            self.lineEdit6.setText("")
            self.lineEdit7.setText("")
            self.lineEdit8.setText("")
            self.lineEdit9.setText("")
            self.lineEdit10.setText("")
            self.lineEdit11.setText("")
            self.lineEdit12.setText("")
            self.lineEdit13.setText("")
            self.lineEdit14.setText("")


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
