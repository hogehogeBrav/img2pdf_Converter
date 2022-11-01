import os
import img2pdf
from natsort import natsorted
from PIL import Image

if __name__ == '__main__':
  pdf_FileName = "./output.pdf"
  png_Folder = "./png"
  extension  = ".png"
  listfolder = natsorted(os.listdir(png_Folder))

  if not listfolder:
    print("No files found in the folder")
    exit()
  else:
    with open(pdf_FileName,"wb") as f:
      f.write(img2pdf.convert([Image.open(png_Folder+j).filename for j in listfolder if j.endswith(extension)]))