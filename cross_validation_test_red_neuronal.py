from cross_validation import *
def main():
    cross_validation = Cross_Validation(5, "red_neuronal")
    cross_validation.leer_archivo()
    cross_validation.normalizar()
    cross_validation.cross_validation()
    
if __name__ == "__main__":
    main()
