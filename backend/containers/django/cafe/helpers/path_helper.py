import os


def upload_path(model_obj, filename):
    obj_name = model_obj.__class__.__name__
    if obj_name == "Menu":
        category_dir_name = model_obj.category.name.replace(" ", "_").lower()
        return os.path.join(
            "images",
            f"{model_obj.__class__.__name__.lower()}",
            f"{category_dir_name}",
            filename,
        )
    elif obj_name == "Category":
        return os.path.join(
            "images", "thumbnail", f"{model_obj.__class__.__name__.lower()}", filename
        )

    else:
        raise Exception("Unknown model object")
