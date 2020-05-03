from ..util.registry import FilterRegistry

from multiprocessing import Queue
import sys

def worker_process(configuration, input_queue, output_queue):
    """Multiprocessing worker process wrapper."""
    
    # precache filter chain instances
    filters = []
    for key in configuration.filters:
        try:
            filters.append(FilterRegistry.load(key))
        except NameError:
            sys.stderr.write("Warning: Cannot load filter for %s" % key)

    # pull work off the queue and process with filter chain
    for line in iter(input_queue.get, None):
        tmp = line
        for FilterInstance in filters:
            tmp = FilterInstance.filter_line(line)
        print('put to queue')
        output_queue.put(tmp)
    
    # put a "None" on the queue for this worker, telling them we are done
    # and will not be submitting more work for output
    output_queue.put(None)
    
    return True


def writer_process(configuration, output_queue):
    """Multiprocessing writer process. Writes to stdout or outfile."""

    nones = 0
    fd = None

    total_lines = 0
    lines = 0
    FLUSH_STDOUT_AT = 100

    if configuration.outfile:
        fd = open(configuration.outfile, 'w')

    for line in iter(output_queue.get, None):
        # there is no sentinel. from config, we will know
        # how many "Nones" we should expect
        if line == None:
            nones += 1
            if nones == configuration.processes:
                # close the file descriptor, if we opened one
                # we are done because all workers have returned a None
                # to us, which means we can stop.
                if fd:
                    fd.close()
                else:
                    sys.stdout.flush()
                return True
        else:
            if fd:
                fd.write("%s\n" % line)
            else:
                sys.stdout.write("%s\n" % line)
                lines += 1
                if lines > FLUSH_STDOUT_AT:
                    sys.stdout.flush()
                    lines = 0

            total_lines += 1