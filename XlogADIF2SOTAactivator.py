#!/usr/bin/env python
#
# XlogADIF2SOTAactivator.py
# Copyright (C) 2013 Aaron Melton <aaron(at)aaronmelton(dot)com>
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


import re           # Required for REGEX operations
import os           # Required to determine OS of host

from re             import search
from os             import name, system


__author__ = "Aaron Melton <aaron@aaronmelton.com>"
__date__ = "(2014-01-20)"
__description__ = "Xlog ADIF to SOTA Activator Log"
__title__ = "XlogADIF2SOTAactivator.py"
__url__ = ""
__version__ = "v0.0.1-alpha"

def clear_screen():
    """clear_screen()
    This function will determine the host operating system and send the
    appropriate command to clear the screen.
    """
    if name == "nt": system("cls")
    else: system("clear")

def confirm(prompt="", defaultAnswer="y"):
    """confirm(prompt="", defaultAnswer="y")
    This function prompts the user to answer "y" for yes or "n" for no
    Returns true if the user answers Yes, false if the answer is No
    The user will not be able to bypass this function without entering valid 
    input: y/n
    """

    while True:
        # Convert response to lower case for comparison
        response = raw_input(prompt).lower()
    
        # If no answer provided, assume Yes
        if response == '':
            return defaultAnswer
    
        # If response is Yes, return True
        elif response == 'y':
            return True
    
        # If response is No, return False
        elif response == 'n':
            return False
    
        # If response is neither Yes or No, repeat the question
        else:
            print "Please enter y or n."
            print


def main():
    """main()
    """
    
    # Clear screen before running application
    clear_screen()
    
    # Print application banner
    print __title__+" "+__version__+" "+__date__
    print "-"*(len(__title__+__version__+__date__)+2)
    
    # Continue to ask user questions until they confirm values are correct
    confirmInput = False
    while confirmInput == False:
        print
        activatingCallsign = ''
        while activatingCallsign == '':
            activatingCallsign = raw_input("Enter the activating callsign: ")
        
        summitReference = ''
        while summitReference == '':
            summitReference = raw_input("Enter the summit reference (e.g. GM/WS-001): ")

        xlogExportFile = ''
        while xlogExportFile == '':
            xlogExportFile = raw_input("Enter the path/filename of your Xlog TSV export file: ")
        
        outputFileName = ''
        while outputFileName == '':
            outputFileName = raw_input("Enter the path/filename for your new SOTA Activation log file: ")
        
        # Show user input for visual confirmation
        print
        print "Callsign   : ", activatingCallsign
        print "Summit     : ", summitReference
        print "Input File : ", xlogExportFile
        print "Output File: ", outputFileName
        print
        confirmInput = confirm("Are these values correct? [Y/n] ")
    
    # Attempt to open Xlog export file; Return error if it does not exist.
    with open(xlogExportFile, "r") as inputFile:
        try:
            with open(outputFileName, "w") as outputFile:
                try:
                    for line in inputFile:
                        # REGEX for ADIF tags borrowed from 
                        # http://web.bxhome.org/blog/ok4bx/2012/05/adif-parser-python
                        QSO_DATE = search(r"<QSO_DATE:(\d+).*?>([^<\t\n\r\f\v\Z]+)", line)
                        TIME_ON = search(r"<TIME_ON:(\d+).*?>([^<\t\n\r\f\v\Z]+)", line)
                        CALL = search(r"<CALL:(\d+).*?>([^<\t\n\r\f\v\Z]+)", line)
                        FREQ = search(r"<FREQ:(\d+).*?>([^<\t\n\r\f\v\Z]+)", line)
                        MODE = search(r"<MODE:(\d+).*?>([^<\t\n\r\f\v\Z]+)", line)
                        if QSO_DATE: outputFile.write(activatingCallsign+","
                                                      +QSO_DATE.group(2).rstrip()+","
                                                      +TIME_ON.group(2).rstrip()+","
                                                      +summitReference+","
                                                      +FREQ.group(2).rstrip()+"MHz,"
                                                      +MODE.group(2).rstrip()+","
                                                      +CALL.group(2).rstrip()+'\n')
                #with open(outputFileName, "w") as outputFile:
                except IOError:
                    print
                    print "--> An error occurred opening "+outputFileName+"."
            print
            print "--> Results written to "+outputFileName
        #with open(xlogExportFile, "r") as inputFile:
        except IOError:
            print
            print "--> An error occurred opening "+xlogExportFile+"."
    
    
if __name__ == "__main__":
    main()
