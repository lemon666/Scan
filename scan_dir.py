# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys
import optparse
import socket
from urllib import urlopen
import threading


def webreq(server, resource):
    try:
        s = socket.socket()
        s.settimeout(5)
        url = server + resource
        request = urlopen(url)
        if request.getcode() != 404:
            print "[+] URL: " + url + "[" + str(request.getcode()) + "]"
    except:
        print "error"


def main():
    parse = optparse.OptionParser(sys.argv[0] + ' -i <such:https://www.baidu.com/> -r <file>')
    parse.add_option('-i', dest='server', type='string')
    parse.add_option('-r', dest='resources', type='string')
    (options, args) = parse.parse_args()
    server = options.server
    resources = options.resources
    if(server == None) and (resources == None):
        print parse.usage
        sys.exit(0)
    threads = []
    resource = []
    for item in open(resources, 'r'):
        resource.append(item.strip())
    for item in resource:
        threads.append(threading.Thread(target=webreq, args=(server, item,)))
    for t in threads:
        t.start()
    for k in threads:
        k.join()


if __name__ == '__main__':
    main()
