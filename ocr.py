# install teseract
# sudo apt-get install tesseract-ocr
# install espeak
# sudo apt-get install espeak

import cv2
import pytesseract
import RPi.GPIO as GPIO
import subprocess

# Pin number for the button
button_pin = 25

# Set up the GPIO pin 24 as an input
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Open the webcam

cap = cv2.VideoCapture(0)

# Set the Tesseract OCR engine to LSTM-based recognition
pytesseract.pytesseract.tesseract_cmd = r'/user/bin/tesseract'
config = ('-l eng --oem 1 --psm 7')

while True:
    # Check if the button is pressed
    button_state = GPIO.input(button_pin)
    if button_state == False:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Convert the image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Pass the image to Tesseract for text recognition
        boxes = pytesseract.image_to_data(gray, config=config)
        for i, line in enumerate(boxes.splitlines()):
            if i != 0:
                data = line.split()
                if len(data) == 12:
                    x, y, w, h = int(data[6]), int(data[7]), int(data[8]), int(data[9])
                    text = data[11]
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(frame, text, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (0, 0, 255), 2, cv2.LINE_AA)
		    subprocess.run(["espeak", "-v", "en-us", text])


        # Display the frame
        cv2.imshow("Webcam OCR", frame)

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()

# Clean up the GPIO settings
GPIO.cleanup()

