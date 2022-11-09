import os
import img2pdf
from natsort import natsorted
from PIL import Image

# フォルダ内拡張子チェック
def extCheck(list, ext):
  for filename in list:
    if not filename.endswith(ext):
      return False
  return True

if __name__ == '__main__':
  # 許可するファイル拡張子
  extension  = ".png", ".jpg", ".jpeg" # tuple 拡張子

  # PDFファイル名入力
  pdf_FileName = "./" + input('Please type generate PDF filename:') + ".pdf"

  # 画像格納フォルダ
  png_Folder = "./png"
  # 隠しファイル以外をファイル名昇順に格納
  listfolder = [filename for filename in natsorted(os.listdir(png_Folder)) if not filename.startswith('.')]


  print(listfolder)

  if not listfolder: # フォルダ内にファイルがない場合
    print("!! No files found in the folder !!")
    exit()
  elif not extCheck(listfolder, extension): # フォルダ内に許可する拡張子のファイルがない場合
    print("!! Only image files should be stored in the folder (Example...[.png, .jpg, .jpeg]) !!")
    exit()
  else:
    with open(pdf_FileName,"wb") as f:
      f.write(img2pdf.convert([Image.open(png_Folder + "/" + j).filename for j in listfolder if j.endswith(extension)]))

      print("-----------------")
      print("|    Success!   |")
      print("-----------------")