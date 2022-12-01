from pathlib import Path
import numpy as np
import csv

def read_file(path: Path) -> np.array:
    """
    Reads a CSV file and outputs a numpy array with the data in the CSV file.
    Detects whether there is a heading and skips over it if this is the case.
    
    Inputs
    ------
    Path: Path object that links to the csv file.

    Returns
    -------
    np.array: Data inside the CSV file.
    
    Examples
    --------
    (bash)
    echo -e "2, 10, 200, 2\n0, 20, -200, 5" >> input.csv
   
    >>> print(read_file(Path("input.csv")))
    [[   2   10  200    2]
     [   0   20 -200    5]]

    """
    with open(path, 'r') as csvfile:
        # Read the text
        csv_text = csvfile.read()
        # Rewind to beginning
        csvfile.seek(0)
        
        # Try to find whether it has a heading
        has_header = csv.Sniffer().has_header(csv_text)
        # Detects delimiters, etc.
        dialect = csv.Sniffer().sniff(csv_text)
        
        # Now read the file with csv.reader
        inputreader = csv.reader(csvfile, dialect)
        if has_header:
            # Skip the header if we have one.
            next(inputreader)
        csv_list = [row for row in inputreader]
        return np.array(csv_list, dtype=int)

def calculate_average(array: "np.array") -> np.array:
    """
    Calculates the average over the columns.

    Parameters
    ----------
    array : (m,n) "np.array"

    Returns
    -------
    (1,n) np.array

    Examples
    --------

    >>> calculate_average(np.array([[1, 2], [3, 4]]))
    array([[2., 3.]])

    """
    res = np.mean(array, axis=0)
    return res.reshape((1, res.shape[0]))

def save_file(array: "np.array", title: str=None) -> None:
    """
    Saves the file to a csv file.

    Parameters
    ----------
    array : "np.array"
        DESCRIPTION.
    title : str
        title in the input data
        
    Returns
    -------
    None

    """

    if title:
        np.savetxt("output.csv",array, delimiter =",", header=title, fmt ='%s',comments='')
    else:
        np.savetxt("output.csv",array, delimiter =",", fmt ='%s',comments='')
