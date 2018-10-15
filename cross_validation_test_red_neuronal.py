from cross_validation import *


def main():
    cross_validation = Cross_Validation(3, "red_neuronal", "prueba.csv")
    cross_validation.cross_validation()

if __name__ == "__main__":
    main()
