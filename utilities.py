from pathlib import Path
import numpy as np

def read_file(path: Path) -> "np.array":
    """
    Reads a CSV file.
    
    Inputs
    ------
    Path: Path object

    Returns
    -------
    np. array

    """
    pass

def calculate_average(array: "np.array") -> "np.array":
    """
    Calculates the average over the columns.

    Parameters
    ----------
    array : (m,n) "np.array"

    Returns
    -------
    (1,n) np.array

    """
    return np.mean(array, axis=0)

def save_file(array: "np.array") -> None:
    """
    Saves the file to a csv file.

    Parameters
    ----------
    array : "np.array"
        DESCRIPTION.

    Returns
    -------
    None

    """
    pass