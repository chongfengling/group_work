from utilities import *

if __name__ == "__main__":
    input, title= read_file(Path("input.csv"))
    res = calculate_average(input)
    save_file(input, title)