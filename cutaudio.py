from pydub import AudioSegment
import argparse
import tqdm
import math
import os
import datetime

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('src')
    parser.add_argument('-m', '--max_step', default=None, type=int)
    parser.add_argument('-i', '--interval', default=10, type=int)
    args = parser.parse_args()

    args.src = os.path.abspath(args.src)
    ext = args.src.split(".")[-1:][0]
    src_sound = AudioSegment.from_file(args.src, format=ext)
    dest_dir = os.path.join(os.getcwd(), "cutaudio_"+datetime.datetime.today().strftime('%Y%m%d%H%M%S'))
    os.makedirs(dest_dir)

    total_time = src_sound.duration_seconds
    max_step = math.ceil(math.ceil(total_time) / args.interval)

    if (args.max_step and args.max_step < max_step):
        max_step = args.max_step

    print("\nsource path : "+args.src)
    print("destination path : "+dest_dir)
    print("total time(s) : "+str(total_time))
    print("max_step : "+str(max_step))
    print("interval(s) : "+str(args.interval))
    print("=========================================")

    for i in tqdm.tqdm(range(max_step)):
        start = i * 1000 * args.interval
        end = (i+1) * 1000 * args.interval
        cur_sound = src_sound[start:end]
        cur_sound.export(os.path.join(dest_dir, str(i)+"."+ext), format=ext)

    print("Successfully\n")

if __name__=='__main__':
    main()
