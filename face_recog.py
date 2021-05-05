
import face_recognition

# Face profile Log
# print("[me_encoding] %r", str(me_encoding))

def Load_and_compare_face(unknown_img_url, known_img_url):
  known_image = face_recognition.load_image_file(known_img_url)
  me_encoding = face_recognition.face_encodings(known_image)[0]

  unknown_image = face_recognition.load_image_file(unknown_img_url)
  unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
  print("[unknown_encoding] %r", unknown_encoding)

  results = face_recognition.compare_faces([me_encoding], unknown_encoding)
  print("[results] %r", results)

  return results

Load_and_compare_face("./me.jpeg", "./me2.jpeg")