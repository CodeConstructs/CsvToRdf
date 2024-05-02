import fileImporter
import dataPropExporter
def main():
    equivalent_labels = {
        "Division": "Division name",
        "Department": "Department name",
        "Course": "Course name",
        "Programme": "Programme name",
        "Academic year": "Academic Year",
        "Study period": "Study Period",
        "Teacher id": "Teacher Id"}
    
    data = fileImporter.importFiles()
    # print(data.keys())
    dataPropExporter.processData(data, equivalent_labels)

if __name__ == "__main__":
    main()