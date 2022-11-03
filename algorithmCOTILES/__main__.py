from algorithmCOTILES.alg.COTILES import COTILES
from algorithmCOTILES.alg.eCOTILES import eCOTILES
import sys
import argparse

__author__ = "Nikolaos Sachpenderis"
__contact__ = "sachpenderis@uom.edu.gr"
__website__ = "users.uom.gr/~sachpenderis/"
__license__ = "BSD"
# COTILES algorithm extends TILES in order to take into account the content of the network as well.
# TILES written by Giulio Rossetti (giulio.rossetti@gmail.com) can be found in https://github.com/GiulioRossetti/TILES

if __name__ == "__main__":

    sys.stdout.write("------------------------------------\n")
    sys.stdout.write("              COTILES                 \n")
    sys.stdout.write("------------------------------------\n")
    sys.stdout.write("Author: " + __author__ + "\n")
    sys.stdout.write("Email:  " + __contact__ + "\n")
    sys.stdout.write("WWW:    " + __website__ + "\n")
    sys.stdout.write("------------------------------------\n")

    parser = argparse.ArgumentParser()

    parser.add_argument('filename', type=str, help='filename')
    parser.add_argument('-o', '--obs', type=int, help='observation (days)', default=7)
    parser.add_argument('-p', '--path', type=str, help='path', default="")
    parser.add_argument('-t', '--ttl', type=int, help='Edge Time To Leave (optional)', default=float('inf'))
    parser.add_argument('-m', '--mode', type=str, help='TTL or Explicit', default="TTL")

    args = parser.parse_args()

    if args.mode == 'TTL':
        an = COTILES(filename=args.filename, obs=args.obs, path=args.path, ttl=args.ttl)
        an.execute()
    elif args.mode == 'Explicit':
        an = eCOTILES(filename=args.filename, obs=args.obs, path=args.path)
        an.execute()
    else:
        sys.stdout.write("Unsupported mode\n")
        sys.stdout.flush()


