def convert_to_class_name(input_string: str, 
                          splitter: str = '_', 
                          suffix: str = '', 
                          prefix: str = '') -> str:

    parts = input_string.split(splitter)
    camel_case = ''.join(part.capitalize() for part in parts)
    class_name = prefix + camel_case + suffix
    
    return class_name