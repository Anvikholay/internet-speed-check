from tkinter import*
import speedtest

root = Tk()
root.config(bg="#f2545b")
root.title("Internet Speed Test")
root.geometry("500x300")

label = Label(root,text="Internet Speed Check") , font=("Lucinda Sams Unicode",18,"bold","itlic"),fg="#a40e4c",bg="#c7ede4")
label.place(relx=0.5,rely=0.1,achor=CENTER)

label_download = Label(root, text="download speed",font=("Segoe Print",18,"bold"),fg="#242038",bg"#eaf7cf")
label_download.place(relx=0.25,rely=0.5,anchor=CENTER)

label_upload = Label(root, text="upload speed",font=("Segoe Print",18,"bold"),fg="#242038",bg"#eaf7cf")
label_upload.place(relx=0.75,rely=0.5,anchor=CENTER)

label_download_speed = Label(root,font=("Yu Gothic Light",14,"bold"),bg="#a63a50",fg="#898952")
label_download_speed.place(relx=0.25,rely=0.6,anchor=CENTER)

label_upload_speed = Label(root,font=("Yu Gothic Light",14,"bold"),bg="#a63a50",fg="#898952")
label_upload_speed.place(relx=0.75,rely=0.6,anchor=CENTER)

def speedCheck():
    st=speedtest.Speedtest()
    download_speed = round(st.download()/1000000,2)
    label_download_speed['text'] = str(download_speed) + "mbps"
    upload_speed = round(st.upload()/1000000,2)
    label_upload_speed['text']=str(upload_speed) + "mbps"
    
    btn_speed = Button(root,text="Check Speed",
                       command=speedCheck,bg="#3891a6",fg="#050505",relif=FLAT)
btn_speed.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()