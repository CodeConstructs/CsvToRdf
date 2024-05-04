from rdflib import Graph, Namespace, RDF, RDFS, XSD, Literal, URIRef


def compile_rdf(data_properties, classes):
    
    # Load existing RDF file into RDF graph
    g = Graph()
    g.parse('./files/data.ttl', format='turtle')

    # Define namespaces
    owl = Namespace("http://www.w3.org/2002/07/owl#")

    # Add properties to the graph
    for prop_id, prop_info in data_properties.items():
        
        # Create URIRef for property ID
        prop_uri = URIRef(prop_id)

        # Add datatype property
        g.add((prop_uri, RDF.type, owl.DatatypeProperty))

        # Add domain
        for domain_class in prop_info['rdfs:domain']:
            domain_uri = URIRef(domain_class)
            g.add((prop_uri, RDFS.domain, domain_uri))
        
        # Check and add range
        dp_range = prop_info['rdfs:range']
        if  dp_range == 'xsd:string':
            range_datatype = XSD.string
        elif dp_range == 'xsd:int':
            range_datatype = XSD.int
        elif dp_range == 'xsd:float':
            range_datatype = XSD.float
        elif dp_range == 'xsd:bool':
            range_datatype = XSD.boolean
        else:
            range_datatype = RDFS.Literal  # Default to generic Literal

        g.add((prop_uri, RDFS.range, range_datatype))

        # Add label
        g.add((prop_uri, RDFS.label, Literal(prop_info['rdfs:label'])))

        # Add subPropertyOf
        g.add((prop_uri, RDFS.subPropertyOf, owl.topDataProperty))

    # Add classes to the graph
    for class_info in classes['classes']:

        # Create URIRef for class ID
        class_uri = URIRef(class_info['ID'])

        # Add class
        g.add((class_uri, RDF.type, owl.Class))

        # Add label
        g.add((class_uri, RDFS.label, Literal(class_info['rdfs:label'])))

    # Serialize to Turtle format and save to the same file
    g.serialize(destination='./files/data.ttl', format='turtle')