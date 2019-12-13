import argparse
from subprocess import call

parser = argparse.ArgumentParser()
parser.add_argument("--mode", default="sentry", type=str, help="Desired Detection Mode")
args = parser.parse_args()

mode = args.mode

if mode == 'sentry':
    rc = call("./detect.sh")
else:
    print('Error: Detection mode not implemented')
