import argparse

args = argparse.ArgumentParser()
args.add_argument("--device")
out = args.parse_args()
print(out)