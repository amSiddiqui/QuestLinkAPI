from sqlalchemy.inspection import inspect
from strawberry.types import Info
import re

def convert_camel_case(name):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    name = pattern.sub('_', name).lower()
    return name

def get_valid_data(modal_data_object, model_class) -> dict:
    data_dict = {}
    for column in model_class.__table__.columns:
        for column in model_class.__table__.columns:
            try:
                data_dict[column.name] = getattr(modal_data_object, column.name)
            except AttributeError:
                pass
    return data_dict


def get_only_selected_fields(model_class_name, info: Info):
    db_relations_fields = inspect(model_class_name).relationships.keys()
    selected_fields = [convert_camel_case(field.name) for field in info.selected_fields[0].selections if field.name not in db_relations_fields]
    return selected_fields
