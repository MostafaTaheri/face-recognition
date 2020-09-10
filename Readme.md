# Face Recognition

Recognize and manipulate faces from Python or from the command line with the world's simplest face recognition library.

#

## Requirements

asyncio

aiohttp

#
## Features
#

### Find faces in pictures

Find all the faces that appear in a picture:

```python
import face_recognition
image = face_recognition.load_image_file("your_file.jpg")
face_locations = face_recognition.face_locations(image)

```

### Identify faces in pictures

Recognize who appears in each photo.

```python
import face_recognition
known_image = face_recognition.load_image_file("biden.jpg")
unknown_image = face_recognition.load_image_file("unknown.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

```
#

## Usage:
```python
from recognition import FaceRecognition


if __name__ == '__main__':
    fr = FaceRecognition()
    fr.recognition('myimage.jpg')
```