import fileImporter
def main():
    data = fileImporter.importFiles()
    print(data.keys())

if __name__ == "__main__":
    main()