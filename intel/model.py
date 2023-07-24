import yaml
from intel.definitions import SOURCE_EXTENSION_YAML
from intel.source.yaml_functions import save_to_yaml

model_source = {
    'callsign': {
        'required': True,
        'min length': 2,
        'max length': 16
    },
    'invited by': {
        'required': True
    },
    'tags': {
        'required': False
    }
}


save_to_yaml(model_source, 'source_model')

with open('model_source' + SOURCE_EXTENSION_YAML, 'w', encoding='utf-8') as file:
    yaml.dump(model_source, file)
