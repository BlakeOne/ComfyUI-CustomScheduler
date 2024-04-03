import torch

class CustomScheduler:
    @classmethod
    def INPUT_TYPES(s):
        inputs = {
            "required": {                
                "steps": ("INT", {"default": 4, "min": 1, "max": 25}),
            },
            "optional": {},             
        }

        defaults = [4.12, 1.62, 0.7, 0.04]
        for i in range(0, 26):
            default = defaults[i] if i < len(defaults) else 0.0
            inputs["optional"][f"sigma_{i}"] = ("FLOAT", {"default": default, "min": 0.0, "max": 100.0, "step": 0.01, "round": 0.0001})
        
        return inputs
        
    RETURN_TYPES = ("SIGMAS",)
    CATEGORY = "sampling/custom_sampling/schedulers"
    FUNCTION = "get_sigmas"

    def get_sigmas(self, steps, **kwargs):
        sigmas = []
        for i in range(0, steps + 1):
            sigma = kwargs[f"sigma_{i}"]
            sigmas.append(sigma)

        sigmas = torch.FloatTensor(sigmas).cpu()
        return (sigmas,)
