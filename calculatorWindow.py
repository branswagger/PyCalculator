#imports gi
import gi
import backgroundCalculator

#set gi version
gi.require_version("Gtk", "3.0")

#import gtk
from gi.repository import Gtk

#define calculator window
class calculatorWindow(Gtk.Window):

    #initialize -Called by python on calculatorWindow creation
    def __init__(self):
        Gtk.Window.__init__(self, title="Calculator")
        self.set_border_width(10)

        #add box as container
        outerBox = Gtk.HBox()
        self.add(outerBox)

        #add numbers box
        numbersBox = Gtk.VBox()
        outerBox.pack_start(numbersBox, True, True, 0)

        #ROW 1
        row1 = Gtk.Box()
        numbersBox.pack_start(row1, True, True, 0)

        #add test view
        self.m_bufferTvView = Gtk.TextBuffer()
        tvView = Gtk.TextView(buffer=self.m_bufferTvView)
        row1.pack_start(tvView, True, True, 0)

        #ROW 2
        row2 = Gtk.Box()
        numbersBox.pack_start(row2, True, True, 0)

        #add button
        button = Gtk.Button.new_with_label("1")
        button.connect("clicked", self.appBtnLbl)
        row2.pack_start(button, True, True, 0)

        #add button
        button = Gtk.Button.new_with_label("2")
        button.connect("clicked", self.appBtnLbl)
        row2.pack_start(button, True, True, 0)

        #add button
        button = Gtk.Button.new_with_label("3")
        button.connect("clicked", self.appBtnLbl)
        row2.pack_start(button, True, True, 0)

        #ROW 3
        row3 = Gtk.Box()
        numbersBox.pack_start(row3, True, True, 0)

        #add button
        button = Gtk.Button.new_with_label("4")
        button.connect("clicked", self.appBtnLbl)
        row3.pack_start(button, True, True, 0)

        #add button
        button = Gtk.Button.new_with_label("5")
        button.connect("clicked", self.appBtnLbl)
        row3.pack_start(button, True, True, 0)

        #add button
        button = Gtk.Button.new_with_label("6")
        button.connect("clicked", self.appBtnLbl)
        row3.pack_start(button, True, True, 0)

        #ROW 4
        row4 = Gtk.Box()
        numbersBox.pack_start(row4, True, True, 0)

        #add button
        button = Gtk.Button.new_with_label("7")
        button.connect("clicked", self.appBtnLbl)
        row4.pack_start(button, True, True, 0)

        #add button
        button = Gtk.Button.new_with_label("8")
        button.connect("clicked", self.appBtnLbl)
        row4.pack_start(button, True, True, 0)

        #add button
        button = Gtk.Button.new_with_label("9")
        button.connect("clicked", self.appBtnLbl)
        row4.pack_start(button, True, True, 0)

        #ROW 5
        row5 = Gtk.Box()
        numbersBox.pack_start(row5, True, True, 0)

        #add button
        button = Gtk.Button.new_with_label("0")
        button.connect("clicked", self.appBtnLbl)
        row5.pack_start(button, True, True, 0)

        #controllers box
        controllersBox = Gtk.VBox()
        outerBox.pack_start(controllersBox, True, True, 0)

        button = Gtk.Button.new_with_label("c")
        button.connect("clicked", self.onClickClear)
        controllersBox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("+")
        button.connect("clicked", self.appBtnLbl)
        controllersBox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("-")
        button.connect("clicked", self.appBtnLbl)
        controllersBox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("/")
        button.connect("clicked", self.appBtnLbl)
        controllersBox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("*")
        button.connect("clicked", self.appBtnLbl)
        controllersBox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("(")
        button.connect("clicked", self.appBtnLbl)
        controllersBox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label(")")
        button.connect("clicked", self.appBtnLbl)
        controllersBox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("=")
        button.connect("clicked", self.btnEquals)
        controllersBox.pack_start(button, True, True, 0)

    #show -Created by brandon to simplify the display of this class
    def show(self):
        #bind exit gtk event to destory
        self.connect("destroy", Gtk.main_quit)

        #function defined by pyobject to show all ui elements
        self.show_all()

        #gtk main launch
        Gtk.main()

    def append(self, textToAppend):
        end_iter = self.m_bufferTvView.get_end_iter()
        self.m_bufferTvView.insert(end_iter, textToAppend)
    
    def getText(self):
        return self.m_bufferTvView.get_text(self.m_bufferTvView.get_start_iter(), self.m_bufferTvView.get_end_iter(), False)

    def appBtnLbl(self, btn):
        self.append(btn.get_label())

    def onClickClear(self, btn):
        self.clear()

    def clear(self):
        self.m_bufferTvView.set_text("")
    
    def btnEquals(self, btn):
        #create background Calculator
        bkgCalc = backgroundCalculator.backgroundCalculator()

        #get string to calc
        stringToCalc = self.getText()

        #get solution
        sSolution = bkgCalc.calculateByString(stringToCalc)

        #clear
        self.clear()

        #append solution
        self.append(sSolution)