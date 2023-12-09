from tkinter import *
import webbrowser

window = Tk()
window.geometry('500x300')
window.resizable(0, 0)
window.title("Soukaina's Website Blocker")
window.configure(bg='lightblue')

# Create and pack the first label
Label(window, text='WEBSITE BLOCKER', font='arial 20 bold', bg='lightblue').pack()

# Create and pack the second label at the bottom
Label(window, text='SGR', font='arial 20 bold', bg='lightblue').pack(side=BOTTOM)

# Create a Text widget for entering websites
Websites = Text(window, font='arial 10', height=2, width=40, wrap=WORD, padx=4, pady=4)
Websites.place(x=140, y=60)

host_path = r'C:\Windows\System32\drivers\etc\hosts' 
ip_address = '127.0.0.1'

def Blocker():
    try:
        website_lists = Websites.get(1.0, END)
        Website = list(website_lists.split(","))
        
        with open(host_path, 'a') as host_file:
            for website in Website:
                if website not in open(host_path).read():
                    host_file.write(ip_address + " " + website + '\n')

        Label(window, text="Blocked", font='arial 12 bold').place(x=230, y=200)
        if Website:
            print(f"Opening blocked website: {Website[0]}")
            webbrowser.open(Website[0])  
    except Exception as e:
        print(f"An error occurred: {e}")

block_button = Button(window, text='Block Websites', command=Blocker)
block_button.place(x=200, y=250)

window.mainloop()
