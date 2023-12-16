from tkinter import * 
from tkinter import filedialog
from tkinter import font



#WINDOW CREATION 
window= Tk()
window.title("TEXT & STUFF")
window.iconbitmap("contract.ico")
# window.geometry("900x600+100+50")
window.maxsize(width=900, height= 600)

global open_file_status
open_file_status= None
   
#_______________________________________________________
#Frames

#creating the Vertical button Frame 
frame_btns= LabelFrame(window, text="Menu",padx=10)
frame_btns.grid(row= 0, column= 0, rowspan=4 ,sticky="ns", padx= 15, pady= 5)


#Creating horizontal button frame 
horizontal_frame = LabelFrame(window, padx= 5, pady= 10, text="Edit Text",borderwidth=5)
horizontal_frame.grid(row=0, column=1,columnspan=4, sticky= "ew")

#Creating TEXT BOX FRAME
frame_txt= Frame (window, padx= 5, pady= 10,borderwidth=5 )
frame_txt.grid(row=1, column=1, columnspan= 4)

#creating text box itself 
txt_box= Text(frame_txt,
               padx= 5, 
               pady= 10, 
               selectbackground="cyan", 
               selectforeground="black",
               undo= True)
txt_box.pack(expand=True)


#Creating Status Bar 
status_bar= Label(window,text= "Ready For Writing ....", padx= 5, pady=10 )
status_bar.grid(row= 5, column=0, columnspan= 5, sticky="ew")

#_______________________________________________________
#Creating The Scroll BAr 
scroll_bar= Scrollbar(window)
#link the txt box to scroll bar
txt_box['yscrollcommand']= scroll_bar.set
#link the scroll bar to the text box
scroll_bar['command']= txt_box.yview

# packing the scroll Bar 
scroll_bar.grid(row= 1, column= 6, rowspan=4, sticky="ns")



#____________Main Functionalities ___________________________________________
# Start New File From Scratch 
def new_file():
    txt_box.delete("1.0", END)
    status_bar.config(text="You are writing a new file...")
    window.title("New Text File")
####################################
#  Open File 
def open_file():

    global open_file_status
        #Delete what in the text box
    txt_box.delete("1.0", END)
         # Creating The File Dialogue    
    txt_file= filedialog.askopenfilename(initialdir="/", title="Open File To Program", filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("All Files","*.*"),))
   
   #check if the opened file has a name 
    if txt_file:
        
        with open(txt_file, "r") as txt_file_opened:
            text_in_file = txt_file_opened.read()
            txt_box.insert(END, text_in_file)
            open_file_status = txt_file
 
        #updating the Status bar 
        status_bar.config(text=f"Opening: {txt_file}")
######################################
# save File  
def save_file(): 
    global open_file_status
    if open_file_status:
        #save the file 
        with open(open_file_status, "w") as txt_file:
            txt_file.write(txt_box.get(1.0, END))
        
           #updating status bar 
        status_bar.config(text=f"Saved Successfully!...")
    else:
       save_as_file()       




#####################################
#save a new file 
def  save_as_file():
    global open_file_status

    txt_file= filedialog.asksaveasfilename(defaultextension=".*", initialdir="/", title= "Save A New File",filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("All Files","*.*"),))   
    if txt_file:
      #updating the Status bar 
        status_bar.config(text=f"Your File Saved in Path: {txt_file}")
        window.title(f"Saved As {txt_file}")
        #Save the file 
        with open(txt_file, "w") as txt_file:
            txt_file.write(txt_box.get(1.0, END))

        #updating the status variable 
        open_file_status=txt_file    
################################################



# Clear text box 
def clear_file():
    txt_box.delete("1.0", END)

############################################################

def make_bold():
    bold_font = font.Font(txt_box, txt_box.cget("font"))
    bold_font.configure(weight="bold")

    txt_box.tag_configure("bold", font = bold_font)

    current_tags = txt_box.tag_names("sel.first") 

    if "bold" in current_tags:
        #remove bold
        txt_box.tag_remove("bold", "sel.first", "sel.last")
    else:
        #add bold 
        txt_box.tag_add("bold", "sel.first", "sel.last")

#####################################################################
def make_italic():
    italic_font = font.Font(txt_box, txt_box.cget("font"))
    italic_font.configure(slant="italic")

    txt_box.tag_configure("italic", font= italic_font)

    current_tags = txt_box.tag_names("sel.first") 

    if "italic" in current_tags:
        #remove bold
        txt_box.tag_remove("italic", "sel.first", "sel.last")
    else:
        #add bold 
        txt_box.tag_add("italic", "sel.first", "sel.last") 

#########################################

def undo():
    txt_box.edit_undo()

def redo():
    txt_box.edit_redo()    

#________________The Layout _______________________________________
#creating the Vertical buttons 
# open File buttons  
btn_open = Button(frame_btns, text="Open", width= 6, height=2, command= open_file)
btn_open.pack(pady= 5)

# New File Buttons 
btn_new = Button(frame_btns, text="New",width= 6, height=2,command= new_file)
btn_new.pack(pady= 5)

# save File Buttons 
btn_save = Button(frame_btns, text="Save",width= 6, height=2,command= save_file)
btn_save.pack(pady= 5)

# Save AS File Buttons 
btn_save_as = Button(frame_btns, text="Save As",width= 6, height=2,command= save_as_file)
btn_save_as.pack(pady= 5)

# Clear text File Buttons 
btn_clear = Button(frame_btns, text="Clear",width= 6, height=2,command= clear_file)
btn_clear.pack(pady= 5)

# Exit program Buttons 
btn_exit = Button(frame_btns, text="Exit",width= 6, height=2 ,command=window.quit)
btn_exit.pack(pady= 5)

#_______________________________________________________
#Creating the Horizontal buttons

# Bold Button
btn_bold = Button(horizontal_frame, text="B",width= 3, height=1, command=make_bold)
btn_bold.grid(row= 0, column=1, padx= 5)

# italic Button
btn_italic = Button(horizontal_frame, text="i",width= 3, height=1, command= make_italic)
btn_italic.grid(row= 0, column=2, padx= 5)

# Redo Button 
btn_redo = Button(horizontal_frame, text= "R", width = 3, height=1 ,command=redo)
btn_redo.grid(row= 0, column=3, padx= 5)

# Undo Button 
btn_undo = Button(horizontal_frame, text= "U", width = 3, height=1 , command= undo)
btn_undo.grid(row= 0, column=4, padx= 5)



window.mainloop()