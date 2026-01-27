"""
My reusable functions fro data analytics
By Ayushi Gupta

"""
def parse_header(header_line):
    return header_line.strip().split(',')

def  parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if item == '':   #handle missing values
            values.append(0.0)
        else:
            try:
                values.append(float(item))
            except ValueError:
                values.append(item)
    return values

def create_item_dict(values, headers):
    result = {}
    for value, header in zip(values, headers):
        result[header] = value
    return result

def read_csv(path):
    result = []
    # Open the file in read mode
    with open(path, 'r') as f:
        # Get a lsit of lines
        lines = f.readlines()

        # Parse the headers
        headers = parse_header(lines[0])

        # Loop over the remaining lines
        for data_line in lines[1:]:
           # Parse the values
           values = parse_values(data_line)

           # Create a dictionary using values and headers
           item_dict = create_item_dict(values, headers)

           # Add the dictionary to the result
           result. append(item_dict)
    return result


def write_csv(items, path):
    # Open the file in write mode
    with open(path, 'w') as f:
        # Return if theres nothing to write
        if len(items) == 0:
            return
        
        # Write the headers in the first line
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')

        # Write one item per line
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write('.'.join(values) + "\n")