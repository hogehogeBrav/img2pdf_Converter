import os
import img2pdf
from natsort import natsorted
from PIL import Image

if __name__ == '__main__':
    pdf_FileName = "./output.pdf"
    png_Folder = "./png"
    extension  = ".png"
    listfolder = os.listdir(png_Folder)
    sortfolder = natsorted(listfolder)

    with open(pdf_FileName,"wb") as f:

        f.write(img2pdf.convert([Image.open(png_Folder+j).filename for j in sortfolder if j.endswith(extension)]))