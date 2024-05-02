from datetime import date
import json
import pandas as pd
baseDomain = 'www.assignment3.com/'
type_dict = {}

def processData (data, equivalent_labels):
    dp_dict = {"":[]}
    dataProperties = openJson('./DataProperties.JSON', 'r')
    for class_key in data.keys():                                                               # Iterate over each class name (key) in the dataset
        initial_DP = ''
        if not dataProperties['DataProperties'] and class_key != '':                            # Check for empty 
            if data[class_key].columns[1] in equivalent_labels.keys():
               initial_DP = equivalent_labels[data[class_key].columns[1]]
            else:
                initial_DP = data[class_key].columns[1] 
            type_dict[initial_DP] = data[class_key][initial_DP].iat[0] 
            dp_dict[initial_DP] = [class_key]                                                   # Initially add a data property (we know it's unique)
            dataProperties = appendJson(dp_dict, dataProperties)                                                                       
        if isinstance(data[class_key], pd.DataFrame):                                                     
            dataProperties = updateDataProperties(data, class_key, dataProperties, dp_dict, equivalent_labels)     # Function call to the new part to make it more readable
    dataProperties = appendJson(dp_dict, dataProperties)                                        

def updateDataProperties(data, class_key, dataProperties, dp_dict, equivalent_labels):
    for dp in data[class_key].columns:                                                          # Iterate over each data property name given a specific key     
        type_dict[dp] = data[class_key][dp].iat[0]                                              # Dictionary use to infer type
        DP_name = ''
        if dp in equivalent_labels.keys():
            DP_name = equivalent_labels[dp]
        else:
            DP_name = dp
        fullDomian = baseDomain + class_key                                                     # Create class id (for data property domain)
        for attribute in dataProperties['DataProperties']:                                      # Iterate over each attribute of a given object in the json file 
            if attribute['label'] == DP_name:                                                   # If the label attribute matches the given data property name
                dp_dict[DP_name] = None                                                         # Store the data property name and value as None (to be used later)
                if fullDomian not in attribute['domain']:                                       # Ensure the domain does not exist in the data property 
                    attribute['domain'].append(baseDomain + class_key)                          # Add the new domain to the data property
                    print('Domain: "' + fullDomian + '" added to data property: ' + DP_name)    
                else:
                    print(fullDomian + ' already exists in data property: ' + DP_name)
            else:
                if DP_name not in dp_dict.keys():                                               # If the DP name is not already in the dictionary:    
                    dp_dict[DP_name] = [class_key]                                              # Add the DP to the dictionary with the class name as the value
                elif dp_dict[DP_name] is not None:   
                    dp_dict[DP_name].append(class_key)                                          # If it is in the dictionary, append the value with the new class name 
    return dataProperties  

def appendJson(dp_dict, dataProperties):
    if dp_dict:
        for dp_name in dp_dict:                                                                 # Iterate over each DP in the dictionary
            if dp_dict[dp_name] != None and dp_name != '':                                      # Not empty or None
                newDataProperty= {                                                              # Initialize in the loop to ensure "empty" values every time 
                    "ID": "",
                    "type": "owl:DatatypeProperty ",
                    "subPropertyOf": "owl:topDataProperty ",
                    "domain": [],
                    "range": "",
                    "label": ""}
                
                for class_key in dp_dict[dp_name]:                                              # Iterate over the class names of each data property
                    newDataProperty['domain'].append(baseDomain + class_key)                    # Append the domain array
                print('Created new data property: ' + dp_name)
                newDataProperty['ID'] = baseDomain + dp_name
                newDataProperty['label'] = dp_name
                newDataProperty['range'] = inferType(dp_name)
                dataProperties['DataProperties'].append(newDataProperty)                        # Append the variable storing everything

    jsonDump(dataProperties)                                                                    # Dump into .JSON file
    return dataProperties

def inferType(dp_name):
    dataType = 'string'
    if dp_name in type_dict:
        value = str(type_dict[dp_name])

        try:
            int(value)
            dataType = "int"
        except ValueError:
            pass
        try:           
            if value.lower() in ['true', 'false']:
                dataType = "bool"
        except AttributeError:
            pass
        try:
            float(value)
            dataType = "float"
        except ValueError:
            pass

    print('...Parsing "' + str(dp_name) + ' : ' + value + '" as a : ' + dataType)
    return "xsd:" + dataType

def jsonDump (dataProperties):
    with open('./DataProperties.JSON', 'w') as file:
        json.dump(dataProperties, file, indent=4)

def openJson(file, access):
    with open(file, access) as file:
        data = json.load(file)
    return data