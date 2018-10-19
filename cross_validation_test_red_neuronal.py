from cross_validation import *

def main():
    cross_validation = Cross_Validation(1, 0.6, "data_set.csv", [10, 4, "softmax"])
    cross_validation.cross_validation()

if __name__ == "__main__":
    main()
