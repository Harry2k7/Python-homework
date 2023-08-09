from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_scientific(object):
    def setupUi(self, scientific):
        scientific.setObjectName("scientific")
        scientific.resize(470, 630)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(scientific.sizePolicy().hasHeightForWidth())
        scientific.setSizePolicy(sizePolicy)
        scientific.setMinimumSize(QtCore.QSize(470, 630))
        scientific.setMaximumSize(QtCore.QSize(470, 630))
        self.model = QtWidgets.QLabel(scientific)
        self.model.setGeometry(QtCore.QRect(150, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.model.setFont(font)
        self.model.setAlignment(QtCore.Qt.AlignCenter)
        self.model.setObjectName("model")
        self.display0 = QtWidgets.QLineEdit(scientific)
        self.display0.setEnabled(False)
        self.display0.setGeometry(QtCore.QRect(10, 70, 451, 53))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.display0.setFont(font)
        self.display0.setObjectName("display0")
        self.display = QtWidgets.QLineEdit(scientific)
        self.display.setEnabled(False)
        self.display.setGeometry(QtCore.QRect(10, 120, 451, 50))
        self.display.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.display.setFont(font)
        self.display.setObjectName("display")
        self.layoutWidget = QtWidgets.QWidget(scientific)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 180, 451, 441))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mc = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mc.sizePolicy().hasHeightForWidth())
        self.mc.setSizePolicy(sizePolicy)
        self.mc.setObjectName("mc")
        self.horizontalLayout.addWidget(self.mc)
        self.mr = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mr.sizePolicy().hasHeightForWidth())
        self.mr.setSizePolicy(sizePolicy)
        self.mr.setObjectName("mr")
        self.horizontalLayout.addWidget(self.mr)
        self.m1 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m1.sizePolicy().hasHeightForWidth())
        self.m1.setSizePolicy(sizePolicy)
        self.m1.setObjectName("m1")
        self.horizontalLayout.addWidget(self.m1)
        self.m2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m2.sizePolicy().hasHeightForWidth())
        self.m2.setSizePolicy(sizePolicy)
        self.m2.setObjectName("m2")
        self.horizontalLayout.addWidget(self.m2)
        self.ms = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ms.sizePolicy().hasHeightForWidth())
        self.ms.setSizePolicy(sizePolicy)
        self.ms.setObjectName("ms")
        self.horizontalLayout.addWidget(self.ms)
        self.m = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m.sizePolicy().hasHeightForWidth())
        self.m.setSizePolicy(sizePolicy)
        self.m.setObjectName("m")
        self.horizontalLayout.addWidget(self.m)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chan = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chan.sizePolicy().hasHeightForWidth())
        self.chan.setSizePolicy(sizePolicy)
        self.chan.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chan.setFont(font)
        self.chan.setObjectName("chan")
        self.horizontalLayout_2.addWidget(self.chan)
        self.pi = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pi.sizePolicy().hasHeightForWidth())
        self.pi.setSizePolicy(sizePolicy)
        self.pi.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pi.setFont(font)
        self.pi.setObjectName("pi")
        self.horizontalLayout_2.addWidget(self.pi)
        self.ce = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ce.sizePolicy().hasHeightForWidth())
        self.ce.setSizePolicy(sizePolicy)
        self.ce.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ce.setFont(font)
        self.ce.setObjectName("ce")
        self.horizontalLayout_2.addWidget(self.ce)
        self.c = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c.sizePolicy().hasHeightForWidth())
        self.c.setSizePolicy(sizePolicy)
        self.c.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.c.setFont(font)
        self.c.setObjectName("c")
        self.horizontalLayout_2.addWidget(self.c)
        self.dele = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dele.sizePolicy().hasHeightForWidth())
        self.dele.setSizePolicy(sizePolicy)
        self.dele.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dele.setFont(font)
        self.dele.setObjectName("dele")
        self.horizontalLayout_2.addWidget(self.dele)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sin = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sin.sizePolicy().hasHeightForWidth())
        self.sin.setSizePolicy(sizePolicy)
        self.sin.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sin.setFont(font)
        self.sin.setObjectName("sin")
        self.horizontalLayout_4.addWidget(self.sin)
        self.cos = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cos.sizePolicy().hasHeightForWidth())
        self.cos.setSizePolicy(sizePolicy)
        self.cos.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cos.setFont(font)
        self.cos.setObjectName("cos")
        self.horizontalLayout_4.addWidget(self.cos)
        self.tan = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tan.sizePolicy().hasHeightForWidth())
        self.tan.setSizePolicy(sizePolicy)
        self.tan.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tan.setFont(font)
        self.tan.setObjectName("tan")
        self.horizontalLayout_4.addWidget(self.tan)
        self.e = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.e.sizePolicy().hasHeightForWidth())
        self.e.setSizePolicy(sizePolicy)
        self.e.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.e.setFont(font)
        self.e.setObjectName("e")
        self.horizontalLayout_4.addWidget(self.e)
        self.rand = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rand.sizePolicy().hasHeightForWidth())
        self.rand.setSizePolicy(sizePolicy)
        self.rand.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rand.setFont(font)
        self.rand.setObjectName("rand")
        self.horizontalLayout_4.addWidget(self.rand)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sqrt = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sqrt.sizePolicy().hasHeightForWidth())
        self.sqrt.setSizePolicy(sizePolicy)
        self.sqrt.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sqrt.setFont(font)
        self.sqrt.setObjectName("sqrt")
        self.horizontalLayout_3.addWidget(self.sqrt)
        self.back = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.horizontalLayout_3.addWidget(self.back)
        self.abso = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.abso.sizePolicy().hasHeightForWidth())
        self.abso.setSizePolicy(sizePolicy)
        self.abso.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.abso.setFont(font)
        self.abso.setObjectName("abso")
        self.horizontalLayout_3.addWidget(self.abso)
        self.up = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up.sizePolicy().hasHeightForWidth())
        self.up.setSizePolicy(sizePolicy)
        self.up.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.up.setFont(font)
        self.up.setObjectName("up")
        self.horizontalLayout_3.addWidget(self.up)
        self.down = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.down.sizePolicy().hasHeightForWidth())
        self.down.setSizePolicy(sizePolicy)
        self.down.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.down.setFont(font)
        self.down.setObjectName("down")
        self.horizontalLayout_3.addWidget(self.down)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.extract = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extract.sizePolicy().hasHeightForWidth())
        self.extract.setSizePolicy(sizePolicy)
        self.extract.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.extract.setFont(font)
        self.extract.setObjectName("extract")
        self.horizontalLayout_7.addWidget(self.extract)
        self.lef = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lef.sizePolicy().hasHeightForWidth())
        self.lef.setSizePolicy(sizePolicy)
        self.lef.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lef.setFont(font)
        self.lef.setObjectName("lef")
        self.horizontalLayout_7.addWidget(self.lef)
        self.rig = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rig.sizePolicy().hasHeightForWidth())
        self.rig.setSizePolicy(sizePolicy)
        self.rig.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rig.setFont(font)
        self.rig.setObjectName("rig")
        self.horizontalLayout_7.addWidget(self.rig)
        self.estate = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.estate.sizePolicy().hasHeightForWidth())
        self.estate.setSizePolicy(sizePolicy)
        self.estate.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.estate.setFont(font)
        self.estate.setObjectName("estate")
        self.horizontalLayout_7.addWidget(self.estate)
        self.divi = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.divi.sizePolicy().hasHeightForWidth())
        self.divi.setSizePolicy(sizePolicy)
        self.divi.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.divi.setFont(font)
        self.divi.setObjectName("divi")
        self.horizontalLayout_7.addWidget(self.divi)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.inde = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inde.sizePolicy().hasHeightForWidth())
        self.inde.setSizePolicy(sizePolicy)
        self.inde.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inde.setFont(font)
        self.inde.setObjectName("inde")
        self.horizontalLayout_8.addWidget(self.inde)
        self.d7 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d7.sizePolicy().hasHeightForWidth())
        self.d7.setSizePolicy(sizePolicy)
        self.d7.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.d7.setFont(font)
        self.d7.setAutoDefault(False)
        self.d7.setObjectName("d7")
        self.horizontalLayout_8.addWidget(self.d7)
        self.d8 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d8.sizePolicy().hasHeightForWidth())
        self.d8.setSizePolicy(sizePolicy)
        self.d8.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.d8.setFont(font)
        self.d8.setAutoDefault(False)
        self.d8.setObjectName("d8")
        self.horizontalLayout_8.addWidget(self.d8)
        self.d9 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d9.sizePolicy().hasHeightForWidth())
        self.d9.setSizePolicy(sizePolicy)
        self.d9.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.d9.setFont(font)
        self.d9.setAutoDefault(False)
        self.d9.setObjectName("d9")
        self.horizontalLayout_8.addWidget(self.d9)
        self.mul = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mul.sizePolicy().hasHeightForWidth())
        self.mul.setSizePolicy(sizePolicy)
        self.mul.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mul.setFont(font)
        self.mul.setObjectName("mul")
        self.horizontalLayout_8.addWidget(self.mul)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.tind = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tind.sizePolicy().hasHeightForWidth())
        self.tind.setSizePolicy(sizePolicy)
        self.tind.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tind.setFont(font)
        self.tind.setObjectName("tind")
        self.horizontalLayout_9.addWidget(self.tind)
        self.d4 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d4.sizePolicy().hasHeightForWidth())
        self.d4.setSizePolicy(sizePolicy)
        self.d4.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.d4.setFont(font)
        self.d4.setAutoDefault(False)
        self.d4.setObjectName("d4")
        self.horizontalLayout_9.addWidget(self.d4)
        self.d5 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d5.sizePolicy().hasHeightForWidth())
        self.d5.setSizePolicy(sizePolicy)
        self.d5.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.d5.setFont(font)
        self.d5.setAutoDefault(False)
        self.d5.setObjectName("d5")
        self.horizontalLayout_9.addWidget(self.d5)
        self.d6 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d6.sizePolicy().hasHeightForWidth())
        self.d6.setSizePolicy(sizePolicy)
        self.d6.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.d6.setFont(font)
        self.d6.setAutoDefault(False)
        self.d6.setObjectName("d6")
        self.horizontalLayout_9.addWidget(self.d6)
        self.sub = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sub.sizePolicy().hasHeightForWidth())
        self.sub.setSizePolicy(sizePolicy)
        self.sub.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sub.setFont(font)
        self.sub.setObjectName("sub")
        self.horizontalLayout_9.addWidget(self.sub)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.log = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log.sizePolicy().hasHeightForWidth())
        self.log.setSizePolicy(sizePolicy)
        self.log.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.log.setFont(font)
        self.log.setObjectName("log")
        self.horizontalLayout_10.addWidget(self.log)
        self.d1 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d1.sizePolicy().hasHeightForWidth())
        self.d1.setSizePolicy(sizePolicy)
        self.d1.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.d1.setFont(font)
        self.d1.setAutoDefault(False)
        self.d1.setObjectName("d1")
        self.horizontalLayout_10.addWidget(self.d1)
        self.d2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d2.sizePolicy().hasHeightForWidth())
        self.d2.setSizePolicy(sizePolicy)
        self.d2.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.d2.setFont(font)
        self.d2.setAutoDefault(False)
        self.d2.setObjectName("d2")
        self.horizontalLayout_10.addWidget(self.d2)
        self.d3 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d3.sizePolicy().hasHeightForWidth())
        self.d3.setSizePolicy(sizePolicy)
        self.d3.setMaximumSize(QtCore.QSize(16777215, 65))
        self.d3.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.d3.setFont(font)
        self.d3.setAutoDefault(False)
        self.d3.setObjectName("d3")
        self.horizontalLayout_10.addWidget(self.d3)
        self.add = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy)
        self.add.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.horizontalLayout_10.addWidget(self.add)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.ln = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln.sizePolicy().hasHeightForWidth())
        self.ln.setSizePolicy(sizePolicy)
        self.ln.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ln.setFont(font)
        self.ln.setObjectName("ln")
        self.horizontalLayout_11.addWidget(self.ln)
        self.ant = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ant.sizePolicy().hasHeightForWidth())
        self.ant.setSizePolicy(sizePolicy)
        self.ant.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.ant.setFont(font)
        self.ant.setAutoDefault(False)
        self.ant.setObjectName("ant")
        self.horizontalLayout_11.addWidget(self.ant)
        self.d0 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d0.sizePolicy().hasHeightForWidth())
        self.d0.setSizePolicy(sizePolicy)
        self.d0.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.d0.setFont(font)
        self.d0.setAutoDefault(False)
        self.d0.setObjectName("d0")
        self.horizontalLayout_11.addWidget(self.d0)
        self.point = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.point.sizePolicy().hasHeightForWidth())
        self.point.setSizePolicy(sizePolicy)
        self.point.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.point.setFont(font)
        self.point.setAutoDefault(False)
        self.point.setObjectName("point")
        self.horizontalLayout_11.addWidget(self.point)
        self.equ = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equ.sizePolicy().hasHeightForWidth())
        self.equ.setSizePolicy(sizePolicy)
        self.equ.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.equ.setFont(font)
        self.equ.setObjectName("equ")
        self.horizontalLayout_11.addWidget(self.equ)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.selectwindow = QtWidgets.QComboBox(scientific)
        self.selectwindow.setGeometry(QtCore.QRect(10, 10, 121, 41))
        self.selectwindow.setObjectName("selectwindow")
        self.selectwindow.addItem("")
        self.selectwindow.addItem("")

        self.retranslateUi(scientific)
        QtCore.QMetaObject.connectSlotsByName(scientific)

    def retranslateUi(self, scientific):
        _translate = QtCore.QCoreApplication.translate
        scientific.setWindowTitle(_translate("scientific", "Form"))
        self.model.setText(_translate("scientific", "Инженерный"))
        self.mc.setText(_translate("scientific", "MC"))
        self.mr.setText(_translate("scientific", "MR"))
        self.m1.setText(_translate("scientific", "M+"))
        self.m2.setText(_translate("scientific", "M-"))
        self.ms.setText(_translate("scientific", "MS"))
        self.m.setText(_translate("scientific", "M"))
        self.chan.setText(_translate("scientific", "2^nd"))
        self.pi.setText(_translate("scientific", "π"))
        self.ce.setText(_translate("scientific", "CE"))
        self.c.setText(_translate("scientific", "C"))
        self.dele.setText(_translate("scientific", "<-"))
        self.sin.setText(_translate("scientific", "sin"))
        self.cos.setText(_translate("scientific", "cos"))
        self.tan.setText(_translate("scientific", "tan"))
        self.e.setText(_translate("scientific", "e"))
        self.rand.setText(_translate("scientific", "rand"))
        self.sqrt.setText(_translate("scientific", "x^2"))
        self.back.setText(_translate("scientific", "1/x"))
        self.abso.setText(_translate("scientific", "|x|"))
        self.up.setText(_translate("scientific", "⌊x⌋ "))
        self.down.setText(_translate("scientific", "⌈x⌉ "))
        self.extract.setText(_translate("scientific", "√x"))
        self.lef.setText(_translate("scientific", "("))
        self.rig.setText(_translate("scientific", ")"))
        self.estate.setText(_translate("scientific", "n!"))
        self.divi.setText(_translate("scientific", "÷"))
        self.inde.setText(_translate("scientific", "x^y"))
        self.d7.setText(_translate("scientific", "7"))
        self.d8.setText(_translate("scientific", "8"))
        self.d9.setText(_translate("scientific", "9"))
        self.mul.setText(_translate("scientific", "×"))
        self.tind.setText(_translate("scientific", "10^x"))
        self.d4.setText(_translate("scientific", "4"))
        self.d5.setText(_translate("scientific", "5"))
        self.d6.setText(_translate("scientific", "6"))
        self.sub.setText(_translate("scientific", "-"))
        self.log.setText(_translate("scientific", "log"))
        self.d1.setText(_translate("scientific", "1"))
        self.d2.setText(_translate("scientific", "2"))
        self.d3.setText(_translate("scientific", "3"))
        self.add.setText(_translate("scientific", "+"))
        self.ln.setText(_translate("scientific", "ln"))
        self.ant.setText(_translate("scientific", "±"))
        self.d0.setText(_translate("scientific", "0"))
        self.point.setText(_translate("scientific", "."))
        self.equ.setText(_translate("scientific", "="))
        self.selectwindow.setItemText(0, _translate("scientific", "standard"))
        self.selectwindow.setItemText(1, _translate("scientific", "Инженерный"))