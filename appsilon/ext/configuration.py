from importlib import import_module


def load_extensions(app):
    for extension in app.config.get("EXTENSIONS"):
        module_name, factory = extension.split(":")
        ext = import_module(module_name)
        getattr(ext, factory)(app)


def init_app(app, config_class):
    app.config.from_object(config_class)
