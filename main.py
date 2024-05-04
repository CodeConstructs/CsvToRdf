import file_importer
import data_property_generator
import pprint

def main():
    equivalent_labels = {
        "Division": "Division_name",
        "Department": "Department_name",
        "Course": "Course_name",
        "Programme": "Programme_name",
        "Academic_year": "Academic_Year",
        "Study_period": "Study_Period",
        "Teacher_id": "Teacher_Id"}
    
    data = file_importer.importFiles()
    # Used to format output but keep in mind that underscores may not be visible 
    pprint.pprint(data_property_generator.get_data_property(data, equivalent_labels))
if __name__ == "__main__":
    main()