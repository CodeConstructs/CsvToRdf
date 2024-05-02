def get_class_json(file_names: list[str]) -> dict:
    """
    Takes a list of file names and returns a dict
    representing the rdf classes
    """
    rdf_classes = {"classes": []}

    for file_name in file_names:
        rdf_classes["classes"].append(__create_dict(file_name))

    return rdf_classes


def __create_dict(file_name: str) -> dict:
    """
    Takes the file name and returns a dict representing the
    json representation of a class in rdf
    """
    return {
        "ID": f"www.assignment3.com/{file_name}",
        "type": "rdf:type owl:Class ;",
        "label": file_name,
    }
