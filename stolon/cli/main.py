import argparse
import multiprocessing
import sys

from .worker import worker_process, writer_process

from ..util.config import Config
from ..util.registry import FilterRegistry

from ..filters import *

def main():
    """main, for when name is main"""
    parser = argparse.ArgumentParser(description="Stolon, a wordlist filtering and sanitisation engine")
    parser.add_argument("--filters", default="", type=str, help="Filter chain to use when processing.")
    parser.add_argument("--list-filters", action="store_true", help="List available filters.")
    parser.add_argument("--about-filter", type=str, help="Query for more information about a filter.")
    parser.add_argument("--lang", type=str, default="en", help="Languages to load data for.")
    parser.add_argument("--processes", type=int, default=multiprocessing.cpu_count(), help="Number of processes to use. Defaults to number of logical cores.")
    parser.add_argument("--outfile", default=None, type=str, help="Output to file instead of stdout.")
    parser.add_argument("--input-encoding", default="utf-8", type=str, help="Expected file input encoding.")

    parser.add_argument("input_files", nargs="*")
    args = parser.parse_args()

    if args.list_filters:
        filters = FilterRegistry.get_available()
        print("available filters:")
        print(", ".join(sorted(filters)))
        sys.exit(0)

    if args.about_filter:
        if args.about_filter in FilterRegistry.get_available():
            print("Loading filter %s to query info..." % args.about_filter)
            instance = FilterRegistry.load(args.about_filter)
            print(instance.info())
            sys.exit(0)
        else:
            print("Cannot find filter %s" % args.about_filter)
            sys.exit(1)
    
    if len(args.filters) == 0:
        print("ERROR: You must specify filters to use. See --list-filters or --help for more information.")
        sys.exit(1)

    Config.filters = args.filters.split(",")
    if 'webpage' in Config.filters:
        sys.stderr.write("Webpage filter selected, locking to single process\n")
        Config.processes = 1
    else:
        Config.processes = args.processes
    if args.outfile:
        Config.outfile = args.outfile


    # establish the worker pool and queue
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()

    # let's push I/O to a single writer process
    writer = multiprocessing.Process(target=writer_process, args=(Config, output_queue))
    writer.start()

    workers = []
    for _ in range(Config.processes):
        proc = multiprocessing.Process(target=worker_process, args=(Config, input_queue, output_queue))
        proc.start()
        workers.append(proc)

    try:
        for input_file in args.input_files:
            with open(input_file, 'r', encoding=args.input_encoding) as fd:
                if "webpage" in Config.filters:
                    # webpage eats the whole thing at once
                    item = fd.read()
                    input_queue.put(item)
                else:
                    for line in fd:
                        input_queue.put(line)
    except (IOError, FileNotFoundError):
        raise

    for worker in workers:
        input_queue.put(None)

    print('done with main')
    
    

