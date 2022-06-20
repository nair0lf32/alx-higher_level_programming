#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except (ValueError, TypeError) as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
