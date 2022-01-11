from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
from SudokuSolverUI import *

class MyWindow(QMainWindow, Ui_MainWindow):
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('sudoku.png'))
        self.setupUi(self)
        global lineEditList
        lineEditList = [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5, self.lineEdit_6, self.lineEdit_7, self.lineEdit_8, self.lineEdit_9, self.lineEdit_10, self.lineEdit_11, self.lineEdit_12, self.lineEdit_13, self.lineEdit_14, self.lineEdit_15, self.lineEdit_16, self.lineEdit_17, self.lineEdit_18, self.lineEdit_19, self.lineEdit_20, self.lineEdit_21, self.lineEdit_22, self.lineEdit_23, self.lineEdit_24, self.lineEdit_25, self.lineEdit_26, self.lineEdit_27, self.lineEdit_28, self.lineEdit_29, self.lineEdit_30, self.lineEdit_31, self.lineEdit_32, self.lineEdit_33, self.lineEdit_34, self.lineEdit_35, self.lineEdit_36, self.lineEdit_37, self.lineEdit_38, self.lineEdit_39, self.lineEdit_40, self.lineEdit_41, self.lineEdit_42, self.lineEdit_43, self.lineEdit_44, self.lineEdit_45, self.lineEdit_46, self.lineEdit_47, self.lineEdit_48, self.lineEdit_49, self.lineEdit_50, self.lineEdit_51, self.lineEdit_52, self.lineEdit_53, self.lineEdit_54, self.lineEdit_55, self.lineEdit_56, self.lineEdit_57, self.lineEdit_58, self.lineEdit_59, self.lineEdit_60, self.lineEdit_61, self.lineEdit_62, self.lineEdit_63, self.lineEdit_64, self.lineEdit_65, self.lineEdit_66, self.lineEdit_67, self.lineEdit_68, self.lineEdit_69, self.lineEdit_70, self.lineEdit_71, self.lineEdit_72, self.lineEdit_73, self.lineEdit_74, self.lineEdit_75, self.lineEdit_76, self.lineEdit_77, self.lineEdit_78, self.lineEdit_79, self.lineEdit_80, self.lineEdit_81]
        self.solveButton.clicked.connect(partial(self.solveSudoku))
        self.resetButton.clicked.connect(partial(self.reset))
    
    def solveSudoku(self):
        i = 0
        for x in range(0, 9):
            for y in range(0, 9):
                if lineEditList[i].text() == '':
                    self.sudoku[x][y] = 0
                    i += 1
                else:
                    self.sudoku[x][y] = int(lineEditList[i].text())
                    lineEditList[i].setStyleSheet("background-color : #a0a0a0")
                    i += 1

        self.solve(self.sudoku)
        
    def printAnswer(self, p):
        j = 0
        for x in range(0, 9):
            for y in range(0, 9):
                lineEditList[j].setText(str(p[x][y]))
                j += 1

    def findNextCellToFill(self, grid, i, j):
        for x in range(i,9):
            for y in range(j,9):
                if grid[x][y] == 0:
                    return x,y
        for x in range(0,9):
            for y in range(0,9):
                if grid[x][y] == 0:
                    return x,y
        return -1,-1

    def isValid(self, grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
            columnOk = all([e != grid[x][j] for x in range(9)])
            if columnOk:
                secTopX, secTopY = 3 *(i//3), 3 *(j//3)
                for x in range(secTopX, secTopX+3):
                    for y in range(secTopY, secTopY+3):
                        if grid[x][y] == e:
                            return False
                return True
        return False
            
    def solve(self, grid, i=0, j=0):
        i,j = self.findNextCellToFill(grid, i, j)
        if i == -1:
            self.printAnswer(self.sudoku)
            return True
        for e in range(1,10):
            if self.isValid(grid,i,j,e):
                grid[i][j] = e
                if self.solve(grid, i, j):
                    return True
                grid[i][j] = 0
        return False

    def reset(self):
        for k in lineEditList:
            k.setText('')
            k.setStyleSheet('')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())