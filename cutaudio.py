#!/usr/bin/python
from pydub import AudioSegment
import argparse
import tqdm
import math
import os
import datetime


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Simple audio file cutting command.")
    parser.add_argument('src', help="Source file for cutting.")
    parser.add_argument('-m', '--max_step', default=None,
                        type=int, help="Max number of files to cut.")
    parser.add_argument('-i', '--interval', default=10,
                        type=int, help="Video time per piece.")
    parser.add_argument('-e', '--ext', default=None,
                        type=str, help="Output file extension.")
    args = parser.parse_args()

    args.src = os.path.abspath(args.src)
    args.ext = args.ext or args.src.split(".")[-1:][0]

    print("loading...")

    src_sound = AudioSegment.from_file(args.src, format=args.ext)
    dest_dir = os.path.join(os.getcwd(), "cutaudio_" +
                            datetime.datetime.today().strftime('%Y%m%d%H%M%S'))
    os.makedirs(dest_dir)

    total_time = src_sound.duration_seconds
    max_step = math.ceil(math.ceil(total_time) / args.interval)

    if (args.max_step and args.max_step < max_step):
        max_step = args.max_step

    print("\nsource path : "+args.src)
    print("destination path : "+dest_dir)
    print("output extension : "+args.ext)
    print("total time(s) : "+str(total_time))
    print("max_step : "+str(max_step))
    print("interval(s) : "+str(args.interval))
    print("=========================================")

    for i in tqdm.tqdm(range(max_step)):
        start = i * 1000 * args.interval
        end = (i+1) * 1000 * args.interval
        cur_sound = src_sound[start:end]
        cur_sound.export(os.path.join(
            dest_dir, str(i)+"."+args.ext), format=args.ext)

    print("Successfully\n")


if __name__ == '__main__':
    main()
