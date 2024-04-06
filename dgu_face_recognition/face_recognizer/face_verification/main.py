from deepface import DeepFace
# import json


class FaceVerificator:
    def __init__(self, first_image, second_image):
        self.first_image_path = first_image
        self.second_image_path = second_image

    def do_verify_face(self):
        try:
            return DeepFace.verify(img1_path=self.first_image_path, img2_path=self.second_image_path, model_name='Facenet512')
        except Exception as e:
            return e
