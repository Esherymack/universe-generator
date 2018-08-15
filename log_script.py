# Logger script for AAWQ universe gen
import sys
# class Logger allows a log to be generated as the console prints as well
# stolen from here: https://stackoverflow.com/questions/14906764/how-to-redirect-stdout-to-both-file-and-console-with-scripting
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("genlog.txt", "w")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        # flush method is for python 3 compatibility
        # handles flush command by doing Nothing
        # extra behaviour may be specified here
        pass
