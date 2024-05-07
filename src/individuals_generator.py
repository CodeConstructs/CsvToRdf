import uuid


def generate_individuals_json(files: dict, equivalent_labels: dict) -> dict:
    """creates an array of individuals"""
    rdf_individuals = {"individuals": []}

    # Loop through each class.
    for (
        file_name,
        file_data,
    ) in files.items():
        # Loop through each individual within a class
        for individual_data in file_data.to_dict(orient="records"):
            temp_dict = {}
            for dp in individual_data:
                if dp in equivalent_labels:
                    temp_dict[equivalent_labels[dp]] = individual_data[dp]
                else:
                    temp_dict[dp] = individual_data[dp]
            rdf_individuals["individuals"].append(
                __create_individual_dict(file_name, temp_dict)
            )

    return rdf_individuals


def __create_individual_dict(file_name: str, individual_data: dict) -> dict:
    """creates a dict for the individual's row"""
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
