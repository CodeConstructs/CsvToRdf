import uuid


def generate_individuals_json(files: dict) -> dict:
    """ """
    rdf_individuals = {"individuals": []}

    # Loop through each class.
    for (
        file_name,
        file_data,
    ) in files.items():
        # Loop through each individual within a class
        for individual_data in file_data.to_dict(orient="records"):
            rdf_individuals["individuals"].append(
                __create_individual_dict(file_name, individual_data)
            )

    return rdf_individuals


def __create_individual_dict(file_name: str, individual_data: dict) -> dict:
    """ """

    # TODO:
    # 1. Get the unique id for each individual
    # 2. for each row, for each column name, make a data property dict: {"data_property":"data_value"}
    # Consideration after: Do we need to handle the type we give it?
    unique_id = __unique_id_generator()

    return {
        "ID": f"{file_name}_{unique_id}",
        "rdf:type": file_name,
        "data_properties": individual_data,
    }


def __unique_id_generator() -> str:
    """
    Generates a unique id for each individual.
    """
    return str(uuid.uuid4())
