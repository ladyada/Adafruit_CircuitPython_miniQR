import sys
import adafruit_miniqr

# For drawing filled rectangles to the console:
out = sys.stdout
WHITE = "\x1b[1;47m  \x1b[40m"
BLACK = "  "

def print_QR(matrix):
    # white 4-pixel border at top
    for _ in range(4):
        for _ in range(matrix.width+8):
            out.write(WHITE)
        print()
    for y in range(matrix.height):
        out.write(WHITE*4)   # 4-pixel border to left
        for x in range(matrix.width):
            if matrix[x, y]:
                out.write(BLACK)
            else:
                out.write(WHITE)
        out.write(WHITE*4)   # 4-pixel bporder to right
        print()
    # white 4-pixel border at bottom
    for _ in range(4):
        for _ in range(matrix.width+8):
            out.write(WHITE)
        print()

qr = adafruit_miniqr.QRCode(qr_type=3,error_correct=adafruit_miniqr.L)
qr.addData(b'https://www.adafruit.com')
qr.make()
matrix = qr.matrix

import hashlib
matrix_s = str(matrix)
print(matrix_s)
hashed = hashlib.md5(matrix_s.encode('utf-8')).hexdigest()
print(hashed)
if hashed != "0b8bf742f2286bc360bf585076aa39ac":
    raise Exception("wrong hash")

print_QR(qr.matrix)
