from pydantic import BaseModel


def get_env_var_names(settings: BaseModel, prefix=""):
    """
    Get a dict of environment variable names and values from a pydantic settings
    instance.
    """
    env_var_names = {}
    for field_name, value in settings.dict().items():
        model_field = settings.__fields__[field_name]
        # env_name = list(model_field.field_info.extra["env_names"])[0]
        env_name = model_field.name if not prefix else f"{prefix}_{model_field.name}"
        if issubclass(model_field.type_, BaseModel):
            env_var_names.update(
                get_env_var_names(settings=model_field.type_(**value), prefix=env_name)
            )
        else:
            env_var_names[env_name.upper()] = value
    return env_var_names
