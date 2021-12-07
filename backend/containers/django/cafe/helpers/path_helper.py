import os


def upload_path(menu_instance, filename):
    category_dir_name = menu_instance.category.name.replace(" ", "_").lower()

    return os.path.join(
        "images",
        f"{menu_instance.__class__.__name__.lower()}",
        f"{category_dir_name}",
        filename,
    )
