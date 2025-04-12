# !/usr/bin/python
#
# Example code to go through the hokuyo_30m.bin file, read timestamps and the hits
# in each packet, and plot them.
#
# To call:
#
#   python read_hokuyo_30m.py hokuyo_30m.bin
#

import sys
import struct
import numpy as np
import csv

def convert(x_s):
    scaling = 0.005  # 5 mm
    offset = -100.0
    x = x_s * scaling + offset
    return x

def main(args):
    if len(sys.argv) < 2:
        print("Please specify input bin file")
        return 1

    # hokuyo_30m always has 1081 hits
    num_hits = 1081

    # angles for each range observation
    rad0 = -135 * (np.pi / 180.0)
    radstep = 0.25 * (np.pi / 180.0)
    angles = np.linspace(rad0, rad0 + (num_hits - 1) * radstep, num_hits)

    input_file = sys.argv[1]
    output_file = input_file.replace(".bin", ".csv")

    f_bin = open(input_file, "rb")
    f_csv = open(output_file, "w", newline='')
    writer = csv.writer(f_csv)
    writer.writerow(["utime", "x", "y"])

    try:
        while True:
            utime_bytes = f_bin.read(8)
            if utime_bytes == b'':
                break 

            utime = struct.unpack('<Q', utime_bytes)[0]

            r = np.zeros(num_hits)
            for i in range(num_hits):
                s_bytes = f_bin.read(2)
                if len(s_bytes) < 2:
                    break
                s = struct.unpack('<H', s_bytes)[0]
                r[i] = convert(s)

            x = r * np.cos(angles)
            y = r * np.sin(angles)

            for i in range(num_hits):
                writer.writerow([utime, x[i], y[i]])

    except Exception as e:
        print("Error:", e)

    f_bin.close()
    f_csv.close()
    print(f"Finished writing to {output_file}")
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
