import webget
import sys


if __name__ == '__main__':

	#data = sys.stdin.read().split('\n')
	data = sys.argv[1:]
	for url in data:
		webget.download(url, "./downloads/")
