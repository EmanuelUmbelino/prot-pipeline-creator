import sys
from example.example import Example

def main(file_path: str | None):
    try:
        if file_path == None:
            print('Type the dataset path:')
            file_path = input()
        Example.run_example(file_path)
    except:
        print('Aplication finished.')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1]:
        main(sys.argv[1])
    else:
        main(None)