# The code is extracting the globalID of the column, the name and it calculates and displays the cross-sectional area.
# If there are missing details about the width and depth, it will display a message.
import ifcopenshell
from ifcopenshell.util import element

def checkRule(model):
    # Initialize a dictionary to store the GlobalID, Name, and Area of all columns
    columns_areas = {}

    # Retrieve all columns from the model
    columns = model.by_type("IfcColumn")

    # Loop through each column in the model
    for column in columns:
        # Retrieve the property sets (psets) of the column
        column_properties = ifcopenshell.util.element.get_psets(column, psets_only=True)

        # Initialize variables for Depth and Width
        depth = None
        width = None

        # Loop through property sets
        for pset_name, pset_props in column_properties.items():
            # Extract Depth and Width from properties
            if 'Depth' in pset_props:
                depth = float(pset_props['Depth'])

            if 'Width' in pset_props:
                width = float(pset_props['Width'])

        # Calculate the area if both depth and width are available
        area = None
        if depth is not None and width is not None:
            area = depth * width

        # Store the GlobalID, Name, and calculated Area in the dictionary
        columns_areas[column.GlobalId] = {
            'Name': column.Name if column.Name else "Unnamed Column",
            'Area': area if area is not None else "Not calculated (missing depth or width)"
        }

    # Output the resulting dictionary
    print("Columns with their calculated areas:")
    #for column_id, details in columns_areas.items():
        #print(f"GlobalID: {column_id}, Name: {details['Name']}, Area: {details['Area']}")

    return columns_areas
