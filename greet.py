import argparse
parser = argparse.ArgumentParser(description='A friendly greeting script.')
parser.add_argument('--name', help='The name of the person to greet.')
args = parser.parse_args()
print(f"Hello, {args.name}!")