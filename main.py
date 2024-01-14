out = """#include "imagedata.h"

const unsigned char gImage_1[] = {
    """


from PIL import Image
import io
import sys

if len(sys.argv) > 1:
    # The second element in sys.argv is the first argument
    image_path = sys.argv[1]
    print("First argument:", image_path)
else:
    print("No argument provided.")


import cv2

im = cv2.imread(image_path)
im_resize = cv2.resize(im, (500, 500))

is_success, im_buf_arr = cv2.imencode(".jpg", im_resize)
img_byte_arr = im_buf_arr.tobytes()

print(img_byte_arr)
for i in range(0, len(img_byte_arr)):
    if i > 0:
        out += ", "
    out += str("0x{:02x}".format(img_byte_arr[i]))
out += """
};
"""

# img_byte_arr is now a bytearray containing the resized image


# with open(image_path, "rb") as image:
#     f = image.read()
#     b = bytearray(f)
#     for i in range(0, len(b)):
#         if i > 0:
#             out += ", "
#         out += str("0x{:02x}".format(b[i]))
#         print(i)
# out += """
# };
# """

# print(out)

with open("imagedata.cpp", "w") as file:
    file.write(out)
