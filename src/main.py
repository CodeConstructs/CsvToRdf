import file_importer
import class_generator
import utils


def main():
    """main"""
    data = file_importer.import_files()

    rdf_classes = class_generator.get_class_json(
        data.keys()
    )  # generate the dict containing the json representation of rdf classes
    utils.dump_json(rdf_classes)  # dump for testing

    print(data.keys())
    print(type(data.keys()))


if __name__ == "__main__":
    main()
