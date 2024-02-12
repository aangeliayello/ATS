def read_keywords_from_file(file_path):
    """Read keywords from a text file, each on a new line."""
    with open(file_path, 'r') as file:
        keywords = [line.strip() for line in file.readlines()]
    return keywords