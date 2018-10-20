from cross_validation import *


def main():
    cross_validation = Cross_Validation(3, "prueba")
    cross_validation.datos_normalizados = [["a"], ["b"],
                                           ["c"], ["d"], ["e"], ["f"]]
    cross_validation.cross_validation()

def maine():
    cross_validation = Cross_Validation(0,0.3, "f",[5,3])
    cross_validation.cross_validation()

if __name__ == "__main__":
    maine()
