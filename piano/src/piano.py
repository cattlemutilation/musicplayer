#!/usr/bin/python

##########################################################
# Piano.py, when run, creates a window that simulates a  #
# two-octave piano. This program was originally created  #
# for the final project of CS 214 at Calvin College.     #
#                                                        #
# Created by: Tanya Agrawal                              #
##########################################################

try:
    from Tkinter import Tk, Frame, BOTH, Label, Button, Entry
except ImportError:
    from tkinter import Tk, Frame, BOTH, Label, Button, Entry
# Import the package that allows me to play sounds.
import pygame as pygame
# Import the package that allows me to keep track of time.
import time
# Import the package that allows me to concurrently run operations.
from _thread import start_new_thread

# These two lines wipe the file.
file = open('songs/song.txt', 'w')
file.close()

file = open('songs/ascii.txt', 'w')
file.close()

recording = False
pygame.init()


##########################################################
# Description: play is a method used in the method       #
# playback that contains the code for opening a file,    #
# reading it and playing each note that the file         #
# contains in time.                                      #
#                                                        #
# Accepts: file_name, which contains a string with the   #
# name of the file that holds to song that is to be      #
# played.                                                #
##########################################################
def play(file_name):
    song_file = open(file_name, 'r')
    print("Playback Started")
    first_line = song_file.readline().split()
    note = first_line[0]
    for line in song_file:
        wave_obj = pygame.mixer.Sound('sounds/' + note + '.wav')
        wave_obj.play()
        time.sleep(1)
        line_elements = line.split()
        note = line_elements[0]
    wave_obj = pygame.mixer.Sound('sounds/' + note + '.wav')
    wave_obj.play()
    print("Playback Stopped")


##########################################################
# Description: playback is a driver method for the       #
# method play and checks what is clicked to tell what    #
# song to play back.                                     #
#                                                        #
# Accepts: event, the mouse event that is tied to the    #
# Label that is clicked.                                 #
##########################################################
def play_back(event):
    start_new_thread(play, ('songs/song.txt',))


##########################################################
# Description: record_on_off is a method that changes    #
# the global variable recording to its opposite and      #
# presses down the record_button Label if the program    #
# is currently recording, and releases it if it is not.  #
#                                                        #
# Accepts: event, the mouse event that is tied to the    #
# Label that is clicked.                                 #
##########################################################
def record_on_off(event):
    global recording
    recording = not recording
    print('Recording: ', recording)
    if recording is False:
        file = open('songs/ascii.txt','a')
        file.write('@')
        file.close()
    


##########################################################
# Description: record is a method used in key_pressed    #
# and button_pressed that opens a file and writes note   #
# to that file, as well as the current time elapsed.     #
#                                                        #
# Accepts: file_name, the name of the file that is to be #
# written to; note, the note that is to be written to    #
# the file.                                              #
##########################################################
def record(file_name, note):
    song_file = open(file_name, 'a')
    song_file.write(note + ' ')
    song_file.write('\n')


def generate_ascii(file_name, note):
    song_file = open(file_name, 'a')
    key = NOTES_TO_KEYS.get(note, None)
    song_file.write(key)
    
def generate_ascii_number(file_name, num):
    song_file = open(file_name, 'a')
    number = str(num)
    song_file.write(number)

##########################################################
# Description: key_pressed is a method bound to each of  #
# the keyboard keys in the dictionary KEYS_TO_NOTES that #
# plays the note associated with the key pressed,        #
# records that note and changes the image to the         #
# 'pressed' or darkened version of that image.           #
#                                                        #
# Accepts: event, the keyboard event that is tied to the #
# key that is pressed.                                   #
##########################################################
def key_pressed(event):
    # This is so that if a key that is not in KEYS_TO_NOTES
    # is pressed, it will not return an error.
    note = KEYS_TO_NOTES.get(event.char, None)
    if note:
        wave_obj = pygame.mixer.Sound('sounds/' + note + '.wav')
        wave_obj.play()
        print(note)
        if recording:
            record('songs/song.txt', note)
            generate_ascii('songs/ascii.txt', note)
        
def number_key_pressed(event):
    # This is so that if a key that is not in KEYS_TO_NOTES
    # is pressed, it will not return an error.
    if recording:
        generate_ascii_number('songs/ascii.txt', event.widget.name)

##########################################################
# Description: button_pressed is a method bound to each  #
# of the keys, or Labels, on the piano that plays the    #
# sound tied to the Label passed in through event,       #
# records that note to the file 'song.txt' and calls     #
# label_pressed for that Label.                          #
#                                                        #
# Accepts: event, the mouse event that is tied to the    #
# Label that is clicked.                                 #
##########################################################
def button_pressed(event):
    wave_obj = pygame.mixer.Sound('sounds/' + event.widget.name + '.wav')
    wave_obj.play()
    print(event.widget.name)
    if recording:
        record('songs/song.txt', event.widget.name)
        generate_ascii('songs/ascii.txt', event.widget.name)
    #label_pressed(event)

def tempo_feed(e1):
    if recording:
        ascii_file = open('songs/ascii.txt','w')
        ascii_file.write(chr(int(e1)))
        print('Tempo entered: ', e1)
        ascii_file.close()
    return e1
    
def number_button_pressed(event):
    print(event.widget.name)
    if recording:
        generate_ascii_number('songs/ascii.txt', event.widget.name)
# KEYS_TO_NOTES is a dictionary that ties note
# names to certain keys on the keyboard.
KEYS_TO_NOTES = {
    'a': 'C4',
    'b': 'C#D4',
    'c': 'D4',
    'd': 'D#E4',
    'e': 'E4',
    'f': 'F4',
    'g': 'F#G4',
    'h': 'G4',
    'i': 'G#A4',
    'j': 'A4',
    'k': 'A#B4',
    'l': 'B4',
    'm': 'C5',
    'n': 'C#D5',
    'o': 'D5',
    'p': 'D#E5',
    'q': 'E5',
    'r': 'F5',
    's': 'F#G5',
    't': 'G5',
    'u': 'G#A5',
    'v': 'A5',
    'w': 'A#B5',
    'x': 'B5',
    'y': 'C6'
}
NOTES_TO_KEYS = {
    'C4': 'a',
    'C#D4': 'b',
    'D4': 'c',
    'D#E4': 'd',
    'E4': 'e',
    'F4': 'f',
    'F#G4': 'g',
    'G4': 'h',
    'G#A4': 'i',
    'A4': 'j',
    'A#B4': 'k',
    'B4': 'l',
    'C5': 'm',
    'C#D5': 'n',
    'D5': 'o',
    'D#E5': 'p',
    'E5': 'q',
    'F5': 'r',
    'F#G5': 's',
    'G5': 't',
    'G#A5': 'u',
    'A5': 'v',
    'A#B5': 'w',
    'B5': 'x',
    'C6': 'y'
}


##########################################################
# Description: Piano is a class that initializes the     #
# window and populates it with all of the necessary      #
# Labels needed to play the piano.                       #
#                                                        #
# Accepts: Frame, which contains the Tkinter window      #
# object.                                                #
##########################################################
class Piano(Frame):

    ##########################################################
    # Description: __init__ is a method that creates         #
    # the window, colors it and calls init_user_interface.   #
    #                                                        #
    # Accepts: self, which contains the window; parent,      #
    # which is a reference to the window.                    #
    ##########################################################
    def __init__(self, parent):

        # This is the initialization of the window along with the
        # coloring of the background.
        Frame.__init__(self, parent, background='LightBlue')

        # So that the parent reference does not go out of scope.
        self.parent = parent
        self.parent.title("Piano")

        # A call to the init_user_interface method.
        self.init_user_interface()

    ##########################################################
    # Description: init_user_interface is a method that      #
    # populates the window passed in all of the Labels,      #
    # sizes the window, titles it, centers it on the screen  #
    # and binds various methods to it.                       #
    #                                                        #
    # Accepts: self, which contains the window.              #
    ##########################################################
    def init_user_interface(self):

        # The 2-dimensional array keys holds the locations, names and after the
        # for loops are executed below, the Labels that are needed
        # to create each key, both white and black.
        keys = [
            [0, 'C4'],
            [35, 'C#D4'],
            [50, 'D4'],
            [85, 'D#E4'],
            [100, 'E4'],
            [150, 'F4'],
            [185, 'F#G4'],
            [200, 'G4'],
            [235, 'G#A4'],
            [250, 'A4'],
            [285, 'A#B4'],
            [300, 'B4'],
            [350, 'C5'],
            [385, 'C#D5'],
            [400, 'D5'],
            [435, 'D#E5'],
            [450, 'E5'],
            [500, 'F5'],
            [535, 'F#G5'],
            [550, 'G5'],
            [585, 'G#A5'],
            [600, 'A5'],
            [635, 'A#B5'],
            [650, 'B5'],
            [700, 'C6']
        ]
        

        # This for loop populates the window with the white key Labels
        # and appends a Label to each slot in keys.
        for key in keys:
            if len(key[1]) == 2:
                colour = "white"
                key.append(self.create_key(colour, key))

        # This for loop populates the window with the black key Labels
        # and appends a Label to each slot in keys.
        for key in keys:
            if len(key[1]) > 2:
                colour = "black"
                key.append(self.create_key(colour, key))

        num = 1
        placement = 750
        place = 0
        for x in range(6):
            label = Button(bg = 'white', text = num,height = 3, width = 6)
            label.name = num
            if x % 3 == 0:
                if x != 0:
                    placement = placement + 50
                    place = 0
            label.place(x=placement, y=place)
            place = place + 50
            num = num + 1
            label.bind('<KeyPress>', number_key_pressed)
            label.bind('<Button-1>', number_button_pressed)

        # This group of lines creates the record Label.
        record_button = Label(self, bg = 'red', height = 3, width = 6, text = 'record')
        record_button.place(x=850, y=0)
        record_button.name = 'red_button'
        record_button.bind('<Button-1>', record_on_off)

        # This group of lines creates the play Label.
        play_button = Label(self, bg = 'green', text = 'play', height = 3, width = 6)
        play_button.place(x=850, y=100)
        play_button.name = 'green_button'
        play_button.bind('<Button-1>', play_back)

        Tempo = Label(text = "Tempo", height = 3, width = 6)
        Tempo.place(x = 900, y = 0)
        e1 = Entry(self)
        e1.pack(fill = BOTH)
        e1.place(x = 900, y = 55)
        buttonCal = Button(self,height = 3, width = 6, command = lambda : tempo_feed(e1.get()), text="Enter")
        buttonCal.place(x = 900, y = 80)


        # This group of lines centers the window on the screen
        # and specifies the size of the window.
        w = 950
        h = 150
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # This group of lines saves a reference to keys so that
        # it does not go out off scope and binds the presses and
        # releases of keys to their respective methods
        self.parent.keys = keys
        self.parent.bind('<KeyPress>', key_pressed)


        # This line packs all elements bound to the window.
        self.pack(fill=BOTH, expand=1)

    ##########################################################
    # Description: create_key is a method that creates and   #
    # returns a Label with an image, a location, a name and  #
    # multiple bindings.                                     #
    #                                                        #
    # Accepts: self, the Piano class; img, the image that    #
    # the Label will be displayed as; key, the element of    #
    # the 2-dimensional array passed in.                     #
    ##########################################################
    def create_key(self, colour, key):
        if colour == 'white':
            label = Button(bg=colour,fg = 'black',text= key[1] ,height = 10, width = 6)
        elif colour == 'black':
            label = Button(bg=colour,fg = 'white',text= key[1] ,height = 4, width = 4)
        label.place(x=key[0], y=0)
        label.name = key[1]
        label.text = key[1]
        label.bind('<Button-1>', button_pressed)
        return label


# The main method creates an instance of the Piano class
# and keeps it running until termination.
def main():
    root = Tk()
    app = Piano(root)
    app.mainloop()

if __name__ == '__main__':
    main()
