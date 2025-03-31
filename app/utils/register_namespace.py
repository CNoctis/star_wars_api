import os
import importlib
from flask_restx import Api

def register_namespace(api: Api, base_path: str = "app/modules") -> None:
    """
    Imports and registers all namespaces from the modules into the API.

    Args:
        api (Api): Flask-RESTx API instance where the namespaces will be registered.
        base_path (str): Base path where the modules are located. Defaults to "app/modules".
    """
    for module in os.listdir(base_path):
        module_path = os.path.join(base_path, module, "__init__.py")
        if os.path.exists(module_path):
            # Import the module dynamically
            module_name = f"app.modules.{module}"
            importlib.import_module(module_name)

            # Retrieve the namespace object (e.g., ns_module) from the module
            ns = getattr(importlib.import_module(module_name), f"ns_{module}", None)
            if ns:
                # Register the namespace with the API
                api.add_namespace(ns, path=f"/{module}")
            else:
                # Log a warning if the namespace is not found
                print(f"Namespace '{module}' not found in {module_name}.")
        else:
            # Log a warning if the module does not exist
            print(f"Module '{module}' does not exist in {base_path}.")
