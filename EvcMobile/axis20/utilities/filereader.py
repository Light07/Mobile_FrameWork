def read(file_path, mode="r"):
    """
        Read content of the file.
    :param file_path: the file path
    :param mode: the read mode
    :return: the file content
    """
    with open(file_path, mode=mode) as f:
        return "".join(f.readlines())
