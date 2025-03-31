import os
import importlib
from typing import Optional

def import_controllers(base_path: Optional[str] = "app/modules") -> None:
    """
    Dynamically imports all controller modules from the specified base path.

    Args:
        base_path (Optional[str]): The base directory where modules are located. 
                                   Defaults to "app/modules".
    """
    for module in os.listdir(base_path):
        module_path = os.path.join(base_path, module, "controllers")
        if os.path.exists(module_path):
            # Iterate through all Python files in the controllers folder
            for filename in os.listdir(module_path):
                if filename.endswith(".py") and filename != "__init__.py":
                    # Dynamically import each controller module
                    module_name = f"app.modules.{module}.controllers.{filename[:-3]}"
                    importlib.import_module(module_name)
