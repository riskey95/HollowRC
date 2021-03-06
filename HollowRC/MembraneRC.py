# -*- coding: utf-8 -*-
"""
Executable for the MembraneRC GUI
This code execute the GUI application

Author: Kenneth C. Kleissl
"""
# Standard library modules
import sys  # We need sys so that we can pass argv to QApplication
# Third-party library modules
from PySide2 import QtWidgets
# Local source tree modules
from MembraneWindow import MembraneWindow  # import the MainWindow class


def main():
    # Create a new instance of QApplication (PyQT5 application object).
    app = QtWidgets.QApplication(sys.argv)  # PyQT5 compatible

    # The QWidget widget is the base class of all user interface objects in PyQt4.
    window = MembraneWindow()  # We set the form to be our ExampleApp (design)
    window.show()  # Show the window/form

    # Exception handling
    sys.excepthook = my_exception_hook      # overwrite the sys exception hook with custom wrapping function

    # Execute app
    sys.exit(app.exec_())


def my_exception_hook(type_, value, traceback_):   # if QtCore.QT_VERSION >= 0x50501:
    # Print the error and traceback
    print(type_, value, traceback_)

    # window.indicate_fail(type, value)

    # Call the default exception hook
    sys.__excepthook__(type_, value, traceback_)  # no need to save original excepthook as __excepthook__ contains it
    sys.exit(1)


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function

# example with a QDialog being passed into the MainWindow class
# http://projects.skylogic.ca/blog/how-to-install-pyqt5-and-build-your-first-gui-in-python-3-4/
