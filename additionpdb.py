import pdb 

pdb.set_trace() # Start debugging here
def add(a, b):
    answer = a + b
    return answer 

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))  
    sum = add(a, b)
    print(sum)

if __name__ == "__main__":
    main()