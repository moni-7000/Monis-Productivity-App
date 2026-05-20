import customtkinter as ctk

def showFrame(frame):
    frame.tkraise()
    
#this makes the window i think
root = ctk.CTk()
root.title("MoniMode")
root.geometry("500x500+900+300")

#this allows for the window stretching
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

#use grid to allow overlapping, nsew to cover whole window
start_frame = ctk.CTkFrame(root)
start_frame.grid(row=0, column=0, sticky="nsew")
main_menu_frame = ctk.CTkFrame(root)
main_menu_frame.grid(row=0, column=0, sticky="nsew")
    
#pack stuff onto start frame
showFrame(start_frame)
startLabel = ctk.CTkLabel(start_frame, text="Welcome to moniMode!!!! :3")
startLabel.pack()
startButton = ctk.CTkButton(start_frame, command=main_menu_frame.tkraise, text="Click this to start!")
startButton.pack()

#pack stuff on main menu 
menuLabel = ctk.CTkLabel(main_menu_frame, text="MAIN MENU\n")
menuLabel.pack()
calcButton = ctk.CTkButton(main_menu_frame, text="♡  CALCULATOR ♡")
calcButton.pack()
todoButton = ctk.CTkButton(main_menu_frame, text="♡  TO-DO LIST  ♡")
todoButton.pack()
focusButton = ctk.CTkButton(main_menu_frame, text="♡  FOCUS TIMER  ♡" )
focusButton.pack()



root.mainloop()

