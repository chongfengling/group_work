from pathlib import Path
import numpy as np
import csv
import json

def read_file(path: Path) -> (np.array, str):
    """
    Reads a file and outputs a numpy array with the data in the file. The file
    can be in CSV or JSON format.
    
    If it's a CSV file, detects whether there is a heading and skips over it if
    this is the case, and returns the heading in a string.
    
    If it's a JSON file, returns array of the records stored in the
    opening dictionary. If the record is a dictionary, return array of
    dictionary values, and return the dictionary keys as a header.
    
    Inputs
    ------
    path: Path
        Path object that links to the csv file.

    Returns
    -------
    array: np.array
        Data inside the CSV file.
    header: str
        String containing the header file, if there is one. Otherwise this
        is None.
    
    Examples
    --------
    (bash)
    echo -e '2, 10, 200, 2\n0, 20, -200, 5' >> input.csv
   
    >>> from pathlib import Path
    >>> from utilities import read_file
    >>> print(read_file(Path("input.csv"))[0])
    [[   2   10  200    2]
     [   0   20 -200    5]]
    
    (bash)
    echo '{"record1":[2,10,200,2],"record2":[0,20,-200,5]}' >> input2.json
    
    >>> from pathlib import Path
    >>> from utilities import read_file
    >>> print(read_file(Path("input2.json"))[0])
    [[   2   10  200    2]
     [   0   20 -200    5]]
    
    (bash)
    echo '{"record1":{"temperature":2,"mass":10,"pressure":200,"volume":2},
           "record2":{"temperature":0,"mass":20,"pressure":-200,"volume":5}}'
           >> input3.json
    
    >>> from pathlib import Path
    >>> from utilities import read_file
    >>> print(read_file(Path("input3.json"))[0])
    [[   2   10  200    2]
     [   0   20 -200    5]]
    >>> print(read_file(Path("input3.json"))[1])
    ['temperature', 'mass', 'pressure', 'volume']

    """
    with open(path, 'r') as file:
        if path.suffix == ".csv":
            # Read the text
            csv_text = file.read()
            # Rewind to beginning
            file.seek(0)
            
            # Try to find whether it has a heading
            has_header = csv.Sniffer().has_header(csv_text)
            # Detects delimiters, etc.
            dialect = csv.Sniffer().sniff(csv_text)
            
            # Now read the file with csv.reader
            inputreader = csv.reader(file, dialect)
            if has_header:
                # If we have a header, get it as a string
                header = next(inputreader)
            else:
                header = None
        
            out_list = [row for row in inputreader]
        elif path.suffix == ".json":
            # Load the json file and read it.
            json_text = file.read()
            json_file = json.loads(json_text)
            
            # Check if dict entries are dict
            if all([type(i) == dict for i in json_file.values()]):
                # Get record values.
                records = [i.values() for i in json_file.values()]
                out_list = [list(i) for i in records]
                # Get record keys. The header will be the keys of the first
                # entry.
                record_header = [i.keys() for i in json_file.values()][0]
                header = [i for i in record_header]
            # Check if dict entries are lists
            elif all([type(i) == list for i in json_file.values()]):  
                # Get record values
                records = json_file.values()
                out_list = [i for i in records]
                # No header it's a list.
                header = None
            else:
                raise ValueError("Unknown format of .json file. Make sure" +\
                                 "records are all of the same type.")
        else:
            raise TypeError("Only accepts csv and json files. Make sure" +\
                            "file extension is correct.")
        
        return np.array(out_list, dtype=int), header

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
    >>> from utilities import calculate_average
    >>> calculate_average(np.array([[1, 2], [3, 4]]))
    array([2., 3.])
    
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

    Returns
    -------
    None

    """

    if title:
        np.savetxt("output.csv",array, delimiter =",", header=title, fmt ='%s',comments='')
    else:
        np.savetxt("output.csv",array, delimiter =",", fmt ='%s',comments='')
