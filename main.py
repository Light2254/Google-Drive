import os
import qrcode
import shutil
import tkinter as tk

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from tkinter import filedialog, ttk

root = tk.Tk()
root.title('oxxo.studio')
root.geometry('300x300')

text = tk.StringVar()   # 設定 text 為文字變數
text.set('')            # 設定 text 的內容


def Gmail():
    a=box.get()
    global UPLOAD_FOLDER
    match a:
        case "1" :
            UPLOAD_FOLDER = '17RuRvT-e3n7Z850mtx1spSJo2Lw7nNt3'
            print(UPLOAD_FOLDER)
        case "2" :
            UPLOAD_FOLDER= '1o7cYPbNpPi53OCEdaED0iCkpz_1kjLVa'
            print(UPLOAD_FOLDER)
        case _ :
            UPLOAD_FOLDER="ERROR"
            print(UPLOAD_FOLDER)
def choose():
    print(UPLOAD_FOLDER)
    filename = filedialog.askopenfilename()
    image_name=filename[27:]
    print(filename)
    # 上傳檔的名字   
    media = MediaFileUpload(filename)
    file = {'name': image_name, 'parents': [UPLOAD_FOLDER]}

    #上傳雲端
    print("正在上傳檔案...")
    file_id = service.files().create(body=file, media_body=media).execute()
    print('雲端檔案ID：' + str(file_id['id']))

    #建立QRcode
    print('正在建立QRcode')
    code="https://drive.google.com/file/d/"+str(file_id['id'])+"/view"
    img = qrcode.make(code)
    img.save(image_name)

    #將圖檔移置指定路徑
    f_src=os.path.join("./",image_name)
    if not os.path.exists("./qrcode/"):
        os.makedirs("./qrcode/")
    f_dst=os.path.join("./qrcode/",image_name)
    shutil.move(f_src,f_dst)
    print('QRcode建立完成')
    print('請重新選擇檔案')

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'Key.json'  # 金鑰檔案

# 建立憑證物件
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=creds)
    
box = ttk.Combobox(root,
                width=20,
                values=['1','2','3','4','5'])
box.pack()
# Button 設定 command 參數
btn1 = tk.Button(root,
            text='選擇 Gmail',
            font=('Arial',20,'bold'),
            command=Gmail)
btn1.pack()

btn2 = tk.Button(root,
            text='選擇 檔案',
            font=('Arial',20,'bold'),
            command=choose)
btn2.pack()


root.mainloop()