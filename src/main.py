import file_importer
import data_property_generator
import class_generator
import pprint
import utils


def main():
    """main"""

    equivalent_labels = {
        "Division": "Division_name",
        "Department": "Department_name",
        "Course": "Course_name",
        "Programme": "Programme_name",
        "Academic_year": "Academic_Year",
        "Study_period": "Study_Period",
        "Teacher_id": "Teacher_Id",
    }

    data = file_importer.import_files()
    # Used to format output but keep in mind that underscores may not be visible
    pprint.pprint(data_property_generator.get_data_property(data, equivalent_labels))

    rdf_classes = class_generator.get_class_json(
        data.keys()
    )  # generate the dict containing the json representation of rdf classes
    utils.dump_json(rdf_classes)  # dump for testing

    print(data.keys())
    print(type(data.keys()))


if __name__ == "__main__":
    main()
