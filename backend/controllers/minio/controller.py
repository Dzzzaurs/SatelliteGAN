from minio import Minio
from minio.error import S3Error

class MinioController:
    def __init__(self, endpoint, access_key, secret_key, secure=True):
        self.client = Minio(
            endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=secure
        )

    def upload_image(self, image_hash, image_data, bucket_name):
        try:
            # Upload the image to MinIO
            self.client.put_object(
                bucket_name,
                image_hash,
                image_data,
                len(image_data),
                content_type="image/jpeg"  # Replace with the appropriate content type
            )
            return True
        except S3Error as e:
            # Handle the S3 error
            print("Failed to upload image to MinIO:", e)
            return False

    def get_image_by_hash(self, image_hash, bucket_name):
        try:
            # Retrieve the image from MinIO
            response = self.client.get_object(bucket_name, image_hash)
            return response.data
        except S3Error as e:
            # Handle the S3 error
            print("Failed to get image from MinIO:", e)
            return None