from fastapi import FastAPI, Query
from controllers.minio_controller import MinioController
from controllers.sentry_controller import SentryController
from controllers.triton_controller import TritonController

app = FastAPI()

# Initialize the controllers
minio_controller = MinioController()
sentry_controller = SentryController()
triton_controller = TritonController()

@app.route('/image', methods=['GET'])
def generate_image():
    seed = request.args.get('seed')
    landscape_type = request.args.get('landscape')

    try:
        # Generate the image using Triton
        generated_image = triton_controller.generate_image(seed, landscape_type)
        
        if generated_image is None:
            raise Exception("Failed to generate image")

        # Upload the generated image to MinIO
        filename = hash(generated_image)  # Generate a unique filename based on the image data
        upload_success = minio_controller.upload_image(filename, generated_image)
        
        if not upload_success:
            raise Exception("Failed to upload image to MinIO")

        return jsonify({
            'filename': filename,
            'message': 'Image generated and uploaded successfully'
        })
    except Exception as e:
        # Log the exception to Sentry
        sentry_controller.log_exception(e)
        
        return jsonify({
            'error': str(e),
            'message': 'Failed to generate and upload image'
        }), 500

if __name__ == '__main__':
    app.run()
