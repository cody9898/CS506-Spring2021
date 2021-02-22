def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    matrix = []
    
    with open(csv_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            strings = line.strip('\n').split(",")
            row = []
            for s in strings:
                try:
                    v = int(s)
                except ValueError:
                    try:
                        v = float(s)
                    except ValueError:
                        v = str(s).strip('\"')
                row.append(v)
            matrix.append(row)
    
    return matrix
