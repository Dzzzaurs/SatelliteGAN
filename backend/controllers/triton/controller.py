from nvidia import Triton

class TritonController:
    def __init__(self, endpoint):
        self.client = Triton(endpoint)

    def generate_image(self, seed, landscape_type):
        # Prepare the input data for the Triton inference request
        input_data = {
            "seed": seed,
            "landscape_type": landscape_type
        }

        try:
            # Make the inference request to Triton
            response = self.client.infer("image_generation_model", input_data)
            
            # Retrieve the generated image from the response
            generated_image = response["output_image"]
            
            return generated_image
        except Exception as e:
            # Handle the exception
            print("Failed to generate image using Triton:", e)
            return None