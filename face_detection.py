import cv2

cam = cv2.VideoCapture(0)

face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

color = None

while True:

    ret, img = cam.read()

    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray, 1.3, 5)

    show = img.copy()

    if color != None:
        show = cv2.applyColorMap(show, color)

    for (x, y, w, h) in faces:
        cv2.rectangle(show, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(show, "Face Detected", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.putText(show, "Press 0-9 to Change Filters", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.putText(show, "Press Q to Quit", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.putText(show, "Faces : " + str(len(faces)), (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    cv2.imshow("Camera", show)

    key = cv2.waitKey(1)

    if key == ord('0'):
        color = None

    elif key == ord('1'):
        color = cv2.COLORMAP_AUTUMN

    elif key == ord('2'):
        color = cv2.COLORMAP_BONE

    elif key == ord('3'):
        color = cv2.COLORMAP_JET

    elif key == ord('4'):
        color = cv2.COLORMAP_WINTER

    elif key == ord('5'):
        color = cv2.COLORMAP_RAINBOW

    elif key == ord('6'):
        color = cv2.COLORMAP_OCEAN

    elif key == ord('7'):
        color = cv2.COLORMAP_SUMMER

    elif key == ord('8'):
        color = cv2.COLORMAP_PINK

    elif key == ord('9'):
        color = cv2.COLORMAP_HOT

    elif key == ord('s'):
        cv2.imwrite("filtered_image.jpg", show)
        print("Image Saved")

    elif key == ord('q') or key == ord('Q'):
        break

cam.release()
cv2.destroyAllWindows()