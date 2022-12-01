from utilities import *

if __name__ == "__main__":
    input = read_file(Path("input.csv"))
    res = calculate_average(input)
    print(res.shape)
    save_file(calculate_average(input))