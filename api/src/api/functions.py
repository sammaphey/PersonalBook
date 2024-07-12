from copy import deepcopy
from typing import Any, Optional
from pydantic import BaseModel, create_model
from pydantic.fields import FieldInfo


def partial(model: type[BaseModel]) -> BaseModel:
    """
    Convert a pydantic model into a model where all fields are marked as optional.

    :param model: The model to convert
    :return: The model but with all fields marked as optional.
    """
    def make_field_optional(field: FieldInfo, default: Any = None) -> tuple[Any, FieldInfo]:
        new = deepcopy(field)
        new.default = default
        new.annotation = Optional[field.annotation]  # type: ignore
        return new.annotation, new
    return create_model(
        f'Partial{model.__name__}',
        __base__=model,
        __module__=model.__module__,
        **{
            field_name: make_field_optional(field_info)
            for field_name, field_info in model.model_fields.items()
        }
    )
