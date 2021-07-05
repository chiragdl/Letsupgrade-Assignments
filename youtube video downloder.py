from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #pip install putube

Folder_Name=""

#file location:
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if (len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please choose Folder!!..",fg="red")

#downlode video:
def DownlodeVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if (len(url) > 1):
        ytdError.config(text="")
        yt = YouTube(url)

        if choice == choices[0]:
            select =yt.streams.filter(progessive=True).first()

        elif choice == choices[1]:
            select =yt.streams.filter(progressive=True, file_extension='mp4').last()

        elif choice == choices[2]:
            select =yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link Again!!",fg='red')

    #Downlode function:
    select.download(Folder_Name)
    ytdError.config(text="Downlode Completed!!")

root = Tk()
root.title("YouTube Downloder")
root.geometry("400x450") #setting window
root.columnconfigure(0,weight=1) # helps all the content in content in center.

# link lable
ytdLable = Label(root,text="Enter the URL of the Video:",font=("jost",18))
ytdLable.grid()

#entry url box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#error message
ytdError = Label(root,text="Error Message",fg="red",font=("jost",12))
ytdError.grid()

#saving videos
saveLable = Label(root,text="Save the Video File:",font=("jost",18,"bold"))
saveLable.grid()

#button of save file
saveEntry = Button(root, width=12,bg="red",fg="white",text="Choose Path", command=openLocation)
saveEntry.grid()

#location  error msg
locationError = Label(root,text="Error message of path:", fg="red", font=("jost",10))
locationError.grid()

#downlode Quality
ytdQuality = Label(root,text="Select Downlode Quality:",font=("jost",18))
ytdQuality.grid()

#Quality choices
choices = ["720p","!44p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#Downlide btn:
downlodebtn = Button(root,text="DOWNLODE",width=12,bg="red",fg="white",command=DownlodeVideo)
downlodebtn.grid()

#devoloper lable:
devoloperlable = Label(root,text="CHIRAG D L",font=("jost,18"))
devoloperlable.grid()

root.mainloop()
