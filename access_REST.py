import json
import requests
import argparse


def get_args():
    parser = argparse.ArgumentParser(description="parse arguments for REST request")
    parser.add_argument('--data', type=str)
    parser.add_argument('--out', type=str, default="response.out")
    parser.add_argument('--ip', type=str, default="")
    parser.add_argument('--port', type=int, default=5017)
    return parser.parse_args()


def main():
    args = get_args()
    response = requests.post("http://%s:%s/api/american"%(args.ip, args.port), json={'text': args.data})
    with open(args.out,'w') as f:
        json.dump(response.json(), f)
    print(response.json())


if __name__ == '__main__':
    main()