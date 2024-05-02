import file_importer 
import class_generator

def main():
    data = file_importer.importFiles()
    print(data.keys())

if __name__ == "__main__":
    main()
