import file_importer
import data_property_generator
import class_generator
import rdf_generator
import pprint
import utils
import individuals_generator


def main():
    """main"""

    equivalent_labels = {
        "Division": "Division_name",
        "Department": "Department_name",
        "Course": "Course_name",
        "Programme": "Programme_name",
        "Academic_Year": "Academic_year",
        "Study_Period": "Study_period",
        "Teacher_Id": "Teacher_id",
    }

    data = file_importer.import_files()
    # Used to format output but keep in mind
    # that underscores may not be visible

    data_properties = data_property_generator.get_data_property(data, equivalent_labels)

    rdf_classes = class_generator.get_class_json(
        data.keys()
    )  # generate the dict containing the json representation of rdf classes

    

    utils.dump_json(rdf_classes)  # dump for testing

    individuals = individuals_generator.generate_individuals_json(data, equivalent_labels)
    utils.dump_json(individuals, file_name="individuals_json")

    rdf_generator.compile_rdf(data_properties, rdf_classes, individuals)
    #    print(data.keys())
    # print(type(data.keys()))


if __name__ == "__main__":
    main()
