
import face_recognition

known_image = face_recognition.load_image_file("./me2.jpeg")
me_encoding = face_recognition.face_encodings(known_image)[0]

unknown_image = face_recognition.load_image_file("./me.jpeg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([me_encoding], unknown_encoding)

print("[results] %r", results)

# Face profile Log
# print("[me_encoding] %r", str(me_encoding))
