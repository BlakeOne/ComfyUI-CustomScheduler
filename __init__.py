# Comfy mappings
from .node import CustomScheduler

NODE_CLASS_MAPPINGS = {"CustomScheduler": CustomScheduler}
NODE_DISPLAY_NAME_MAPPINGS = {"CustomScheduler" : "CustomScheduler"}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# Copy extension to comfy
import folder_paths
import shutil
import os

cwd_path = os.path.dirname(os.path.realpath(__file__))
comfy_path = folder_paths.base_path
web_extension_path = os.path.join(comfy_path, "web", "extensions", "CustomScheduler")
widgets_js_file = os.path.join(cwd_path, "extension.js")

if not os.path.exists(web_extension_path):
    os.makedirs(web_extension_path)
else:
    try:
        shutil.rmtree(web_extension_path)
        os.makedirs(web_extension_path)
    except:
        print("Unable to remove old web extension.")
        pass
        
shutil.copy(widgets_js_file, web_extension_path)
