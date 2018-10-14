from cross_validation import *


def main():
    cross_validation = Cross_Validation(3, "prueba")
    cross_validation.datos_normalizados = [["a"], ["b"],
                                           ["c"], ["d"], ["e"], ["f"]]
    cross_validation.cross_validation()

if __name__ == "__main__":
    main()
