"""Define a function that prints a progress bar of percent p completion."""
import sys


def print_progress(p):
    """Print a progress bar with %p finished."""
    toolbar_len = 50
    num_done = int(toolbar_len*p)
    num_remain = toolbar_len - num_done

    sys.stdout.flush()
    sys.stdout.write("\r[{}{}] %{}".format("="*num_done,
                     " "*num_remain, int(p*100)))
