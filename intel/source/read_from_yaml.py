import yaml


def read_from_yaml(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        read_data: object = yaml.safe_load(file)
        return read_data


file_name = 'test.yaml'
print(read_from_yaml(file_name))
