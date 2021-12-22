def convert_simple(csv):
    """
    csv should be a string that meets the RFC 4180 specification,
    with the additional requirement of a header line.
    This function returns a list of dictionaries.
    """
    csv = csv.rstrip().strip()
    lines = csv.splitlines()
    # fetch the first line
    header = lines.pop(0).split(",")

    # the list that will be returned from the function
    return_list = []

    for line in lines:
        # a temporary dictionary which will be used to
        # aggregate the key/value pairs before adding
        # them to the return_list
        tmp_dict = {}

        # a variable to track whether the char being read is between double quote marks
        quoted = False

        # value to keep track of the index in the line
        i = 0

        # variable to keep track of the index of the header to
        # be used as the key in tmp_dict
        header_indx = 0

        # variable to keep track of a string of
        # characters before you add them to tmp_dict with the appropriate header
        text_buffer = ""

        # iterate through the line
        while i < len(line):
            # if you find a double quote
            if line[i] == "\"":
                if quoted:
                    # if you have two double quote marks next to each other
                    # it signifies a literal double quote mark
                    if i+1 < len(line) and line[i+1] == "\"":
                        text_buffer += "\""
                        i += 1
                    # otherwise, turn the quoted flag to false
                    else:
                        quoted = False
                # if this is the beginning quote mark
                else:
                    quoted = True
            # if this is a comma delimiter
            elif line[i] == "," and not quoted:
                tmp_dict[header[header_indx]] = text_buffer
                text_buffer = ""
                header_indx += 1
            # normal text, add it to the buffer
            else:
                text_buffer += line[i]
            # increment the index
            i += 1
        # add the final dictionary buffer to the list
        tmp_dict[header[header_indx]] = text_buffer
        return_list.append(tmp_dict)

    # return the list
    return return_list
