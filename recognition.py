import face_recognition
from PIL import Image


class FaceRecognition(object):
    """Recognize faces from Python with the world’s simplest face recognition library.
    
    To use:
    >>> fr = FaceRecognition()
    >>> fr.recognition('picture.png')    
    >>> fr.compare('first-picture.png', 'second-picture.png')
    true
    """

    def recognition(self, image_url: str) -> None:
        """Identify faces in pictures.

        Parameters:
            image_url: The url of image location.        
        """
        image = face_recognition.load_image_file("2.jpg")
        face_locations = face_recognition.face_locations(
            image, number_of_times_to_upsample=0, model="cnn")

        for face_location in face_locations:
            top, right, bottom, left = face_location
            face_image = image[top:bottom, left:right]
            pill_image = Image.fromarray(face_image)
            pill_image.show()

    def compare(self, first_image_url: str, second_image_url: str) -> bool:
        """See if the face is a match for the known face.
        
        Parameters:
            first_image_url: The url of image location.
            second_image_url: The url of image location.
        """
        first_image = face_recognition.load_image_file(first_image_url)
        second_image = face_recognition.load_image_file(second_image_url)
        first_encoding = face_recognition.face_encodings(first_image)[0]
        second_encoding = face_recognition.face_encodings(second_image)[0]
        return face_recognition.compare_faces([first_encoding],
                                              second_encoding)[0]