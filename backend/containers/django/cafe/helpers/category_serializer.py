def category_serialize(bulk: list) -> list:

    for parent_dicts in bulk:
        for parent_v in parent_dicts.values():
            if isinstance(parent_v, dict):
                parent_v.pop("date_created")
                parent_v.pop("date_modified")
            elif isinstance(parent_v, list):
                for child_dicts in parent_v:
                    for child_v in child_dicts.values():
                        if isinstance(child_v, dict):
                            child_v.pop("date_created")
                            child_v.pop("date_modified")
    return bulk
