import pandas as pd


def get_data_property(data: dict, equivalent_labels: dict, class_abbreviations: dict) -> dict:
    type_dict = {}
    dp_name = ""
    data_properties = {}
    for class_key in data.keys():
        for data_property in data[class_key]:
            type_dict[data_property] = data[class_key][data_property].iat[0]
            if data_property in equivalent_labels.keys():
                dp_name = equivalent_labels[data_property]
            else:
                dp_name = data_property
            if class_key in class_abbreviations:
                dp_name = dp_name + "_" + class_abbreviations[class_key]

            data_properties[dp_name] = __create_new_data_property(
                class_key, dp_name, type_dict
            )

    return data_properties


def __create_new_data_property(class_key: str, dp_name: str, type_dict: dict) -> dict:
    newDataProperty = {
        "ID": "",
        "rdf:type": "owl:DatatypeProperty ",
        "rdfs:subPropertyOf": "owl:topDataProperty ",
        "rdfs:domain": [],
        "rdfs:range": "",
        "rdfs:label": "",
    }
    newDataProperty["ID"] = dp_name
    newDataProperty["rdfs:domain"].append(class_key)
    newDataProperty["rdfs:range"] = __infer_type(dp_name, type_dict)
    newDataProperty["rdfs:label"] = dp_name

    return newDataProperty


def __infer_type(dp_name: str, type_dict: dict) -> str:
    if dp_name in type_dict:
        value = str(type_dict[dp_name])

        try:
            int(value)
            return "xsd:int"
        except ValueError:
            pass
        try:
            if value.lower() in ["true", "false"]:
                return "xsd:bool"
        except AttributeError:
            pass
        try:
            float(value)
            return "xsd:float"
        except ValueError:
            pass

    return "xsd:string"
