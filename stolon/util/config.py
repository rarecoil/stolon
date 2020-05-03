import multiprocessing

class _ConfigData(object):
    """A struct used to hold configuration data."""
    
    filters = []
    lang = ["en"]
    processes = multiprocessing.cpu_count()
    outfile = None


Config = _ConfigData()