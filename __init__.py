from .node import CustomScheduler

NODE_CLASS_MAPPINGS = {"CustomScheduler": CustomScheduler}
NODE_DISPLAY_NAME_MAPPINGS = {"CustomScheduler" : "CustomScheduler"}
WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]