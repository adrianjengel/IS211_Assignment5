#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK5 Assignment - Network request simulation."""

import csv, urllib2, argparse


def main():
    """The main function of the program. Launches with a default file location, unless noted otherwise."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--servers",help = "The number of servers that can handle the requests.")
    parser.add_argument("--file", default="http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv",
                        help = "The URL to fetch the request data.")
    args = parser.parse_args()

    if not args.servers:
        simulateOneServer(args.file)

    else:
        simulateManyServers(args.file, args.servers)


class Queue:
    # copied from the reading material
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Server:
    # copied from the book / same as the Printer class
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self,new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


class Request:
    # copied from the book / same as the Task class.
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulateOneServer(csv_file):
    # do something
    pass


def simulateManyServers(csv_file, num_servers):
    # do something
    pass


if __name__ == '__main__':
    main()