import os, sys, subprocess

def open_file(filename):
    if sys.platform == "win32":
        os.startfile('h\\f\\yas.png')
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, 'h/f/yas.png'])


open_file('hej')