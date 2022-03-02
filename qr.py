import base64
import random
from datetime import datetime

from MyQR import myqr
from PIL import Image

from pyzbar.pyzbar import decode

import pyqrcode

import pandas as pd

import os

# randomNum = f"{datetime.date.today()}"

students = pd.read_excel('students.xlsx')
sts = []

for row in students['names']:
    sts.append(row)


def generating_qr_codes():
    for n in range(0, len(sts)):
        data = sts[n].encode()
        name = base64.b64encode(data)
        version, level, qr_name = myqr.run(
            str(name),
            level="H",
            version=1,
            colorized=True,
            contrast=1.0,
            brightness=1.0,
            save_name=str(sts[n] + '.bmp'),
            save_dir=os.getcwd()
        )


#generating_qr_codes()
st_qrs = [x for x in os.listdir(os.getcwd()) if 'bmp' in str(x)]

im = Image.open('Hana Ziad .bmp')
imm = decode(im)

print(imm[0].data.decode('utf-8') == "b'SGFuYSBaaWFkIA=='")





