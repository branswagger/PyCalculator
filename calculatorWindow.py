#imports gi
import gi
import backgroundCalculator

#set gi version
gi.require_version("Gtk", "3.0")

#import gtk (the ui)
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

        #add ROW 1
        row1 = Gtk.Box()
        numbersBox.pack_start(row1, True, True, 0)

        #add text view
        self.m_bufferTvView = Gtk.TextBuffer()
        tvView = Gtk.TextView(buffer=self.m_bufferTvView)
        row1.pack_start(tvView, True, True, 0)

        #add ROW 2
        row2 = Gtk.Box()
        numbersBox.pack_start(row2, True, True, 0)

        #add number1 button
        button = Gtk.Button.new_with_label("1")
        button.connect("clicked", self.appBtnLbl)
        row2.pack_start(button, True, True, 0)

        #add number2 button
        button = Gtk.Button.new_with_label("2")
        button.connect("clicked", self.appBtnLbl)
        row2.pack_start(button, True, True, 0)

        #add number3 button
        button = Gtk.Button.new_with_label("3")
        button.connect("clicked", self.appBtnLbl)
        row2.pack_start(button, True, True, 0)

        #Add ROW 3
        row3 = Gtk.Box()
        numbersBox.pack_start(row3, True, True, 0)

        #add number4 button
        button = Gtk.Button.new_with_label("4")
        button.connect("clicked", self.appBtnLbl)
        row3.pack_start(button, True, True, 0)

        #add number5 button
        button = Gtk.Button.new_with_label("5")
        button.connect("clicked", self.appBtnLbl)
        row3.pack_start(button, True, True, 0)

        #add number6 button
        button = Gtk.Button.new_with_label("6")
        button.connect("clicked", self.appBtnLbl)
        row3.pack_start(button, True, True, 0)

        #add ROW 4
        row4 = Gtk.Box()
        numbersBox.pack_start(row4, True, True, 0)

        #add number7 button
        button = Gtk.Button.new_with_label("7")
        button.connect("clicked", self.appBtnLbl)
        row4.pack_start(button, True, True, 0)

        #add number8 button
        button = Gtk.Button.new_with_label("8")
        button.connect("clicked", self.appBtnLbl)
        row4.pack_start(button, True, True, 0)

        #add number9 button
        button = Gtk.Button.new_with_label("9")
        button.connect("clicked", self.appBtnLbl)
        row4.pack_start(button, True, True, 0)

        #add ROW 5
        row5 = Gtk.Box()
        numbersBox.pack_start(row5, True, True, 0)

        #add number0 button
        button = Gtk.Button.new_with_label("0")
        button.connect("clicked", self.appBtnLbl)
        row5.pack_start(button, True, True, 0)

        #add controllers box
        controllersBox = Gtk.VBox()
        outerBox.pack_start(controllersBox, True, True, 0)

        #add clear button
        button = Gtk.Button.new_with_label("c")
        button.connect("clicked", self.onClickClear)
        controllersBox.pack_start(button, True, True, 0)

        #add plus button
        button = Gtk.Button.new_with_label("+")
        button.connect("clicked", self.appBtnLbl)
        controllersBox.pack_start(button, True, True, 0)

        #add minus button
        button = Gtk.Button.new_with_label("-")
        button.connect("clicked", self.appBtnLbl)
        controllersBox.pack_start(button, True, True, 0)

        #add divide button
        button = Gtk.Button.new_with_label("/")
        button.connect("clicked", self.appBtnLbl)
        controllersBox.pack_start(button, True, True, 0)

        #add multiply button
        button = Gtk.Button.new_with_label("*")
        button.connect("clicked", self.appBtnLbl)
        controllersBox.pack_start(button, True, True, 0)

        #add open parenthesis button
        button = Gtk.Button.new_with_label("(")
        button.connect("clicked", self.appBtnLbl)
        controllersBox.pack_start(button, True, True, 0)
        button.set_sensitive(False) #disable, not ready to handle this

        #add close parenthesis button
        button = Gtk.Button.new_with_label(")")
        button.connect("clicked", self.appBtnLbl)
        controllersBox.pack_start(button, True, True, 0)
        button.set_sensitive(False) #disable, not ready to handle this

        #add equals button
        button = Gtk.Button.new_with_label("=")
        button.connect("clicked", self.btnEquals)
        controllersBox.pack_start(button, True, True, 0)

    #Quick easy way to show the UI created in __init__
    def show(self):
        #bind exit gtk event to destory
        self.connect("destroy", Gtk.main_quit)

        #function defined by pyobject to show all ui elements
        self.show_all()

        #gtk main launch
        Gtk.main()

    #quick way to append to the text view
    def append(self, textToAppend):
        end_iter = self.m_bufferTvView.get_end_iter()
        self.m_bufferTvView.insert(end_iter, textToAppend)
    
    #quick way to get the current text from the text view
    def getText(self):
        return self.m_bufferTvView.get_text(self.m_bufferTvView.get_start_iter(), self.m_bufferTvView.get_end_iter(), False)

    #an on click handler to clear to get the label of button clicked and appened it to the text view
    def appBtnLbl(self, btn):
        self.append(btn.get_label())

    #an on click handler to clear the text view
    def onClickClear(self, btn):
        self.clear()

    #a qucik way to clear the text view
    def clear(self):
        self.m_bufferTvView.set_text("")
    
    #an on click handler to solve the equation
    def btnEquals(self, btn):
        #create background Calculator
        bkgCalc = backgroundCalculator.backgroundCalculator()

        #get string to calc
        stringToCalc = self.getText()

        #get solution
        sSolution = str(bkgCalc.calculateByString(stringToCalc))

        #clear
        self.clear()

        #append solution
        self.append(sSolution)