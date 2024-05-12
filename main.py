import qrcode
import os
import shutil

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

print("請輸入選擇的檔案")
image_name=input("")

while image_name!="-1":
    print("請輸入選擇的Gmail")
    Gmail=input("")
    match Gmail:
        case "1" :
            UPLOAD_FOLDER = '1yhnJ6jdJM88pGXjq_SgbPLnIjoHXwLv2'
            print(UPLOAD_FOLDER)
        case "2" :
            UPLOAD_FOLDER= '1o7cYPbNpPi53OCEdaED0iCkpz_1kjLVa'
            print(UPLOAD_FOLDER)
        case _ :
            UPLOAD_FOLDER="ERROR"
            print(UPLOAD_FOLDER)

    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = 'Key.json'  # 金鑰檔案

    # 建立憑證物件
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)
    
    # 上傳檔的名字
    filename = image_name +".jpg"    
    media = MediaFileUpload(filename)
    file = {'name': filename, 'parents': [UPLOAD_FOLDER]}

    #上傳雲端
    print("正在上傳檔案...")
    file_id = service.files().create(body=file, media_body=media).execute()
    print('雲端檔案ID：' + str(file_id['id']))

    #建立QRcode
    code="https://drive.google.com/file/d/"+str(file_id['id'])+"/view"
    img = qrcode.make(code)
    img.save(image_name+".png")

    #將圖檔移置指定路徑
    f_src=os.path.join("./",image_name+".png")
    if not os.path.exists("./qrcode/"):
        os.makedirs("./qrcode/")
    f_dst=os.path.join("./qrcode/",image_name+".png")
    shutil.move(f_src,f_dst)

    os.system("cls")
    print("請輸入選擇的檔案")
    image_name=input("")