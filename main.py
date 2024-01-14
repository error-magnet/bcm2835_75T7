out = """#include "imagedata.h"

const unsigned char gImage_1[] = {
    """


import sys

if len(sys.argv) > 1:
    # The second element in sys.argv is the first argument
    first_argument = sys.argv[1]
    print("First argument:", first_argument)
else:
    print("No argument provided.")


with open(first_argument, "rb") as image:
    f = image.read()
    b = bytearray(f)
    for i in range(0, len(b)):
        if i > 0:
            out += ", "
        out += str("0x{:02x}".format(b[i]))
out += """
};
"""

# print(out)

with open("imagedata.cpp", "w") as file:
    file.write(out)
