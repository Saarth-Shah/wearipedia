import random

import numpy as np

__all__ = ["is_notebook", "seed_everything"]


def is_notebook() -> bool:
    """Check if the code is running in a notebook."""
    try:
        shell = get_ipython().__class__.__name__
        if shell == "ZMQInteractiveShell":
            return True  # Jupyter notebook or qtconsole
        elif shell == "TerminalInteractiveShell":
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False  # Probably standard Python interpreter


def seed_everything(seed):
    """Set seed for reproducibility."""
    np.random.seed(seed)
    random.seed(seed)
