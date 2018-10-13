from cross_validation import *
def main():
    cross_validation = Cross_Validation(3," ")
    cross_validation.archivo= [[3,4,5,6,1],
               [1,5,1,8,0],
               [2,3,4,3,1],
               [3,5,6,4,0],
               [1,5,1,8,0],
               [2,3,4,3,1],
               [3,5,6,4,0]]
    cross_validation.normalizar()
    cross_validation.cross_validation()
    
if __name__ == "__main__":
    main()
