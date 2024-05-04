import os
import json


def dump_json(
    data_to_dump: dict, path: str = os.getcwd(), file_name: str = "json_dump"
) -> None:
    """
    Takes as input a dict to be dumped to a json in the specified directory.
    If no directory is specified, it is dumped to the current directory.
    If no filename is specified, it is defaulted to 'json_dump'
    """
    print(path)
    with open(f"{path}/{file_name}.json", "w", encoding="utf-8") as json_file:
        json.dump(data_to_dump, json_file, indent=2)
