out = """#include "imagedata.h"

const unsigned char gImage_1[] = {
    """


from PIL import Image
import pdb
import io


import sys

if len(sys.argv) > 1:
    # The second element in sys.argv is the first argument
    image_path = sys.argv[1]
    print("First argument:", image_path)
else:
    print("No argument provided.")

with Image.open(image_path) as img:
    # Resize the image
    img = img.resize((800, 600))

    # Convert image to byte array
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="JPEG")
    img_byte_arr = img_byte_arr.getvalue()
    # pdb.set_trace()
    # f = image.read()
    # img_byte_arr = bytearray(f)
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
# out += """
# };
# """

# print(out)

with open("imagedata.cpp", "w") as file:
    file.write(out)
