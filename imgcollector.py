import main
import os
import cv2
from main import HandImageCapture

flag = True
while flag:        
    choice = int(input("Existing(0) or New Sign(1): "))
    if choice == 0:   
        folder_name = input("Enter the name of the folder: ")
        flag = False
    elif choice == 1:
        print("Creating new folder")
        folder_name = input("Enter the name of the folder: ")
        parent_folder = "Signs"
        folder_path = os.path.join(parent_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        flag = False
    else:
        print("Wrong input")

if __name__ == "__main__":
    image_capture = HandImageCapture(folder_name)
    image_capture.capture_images()
    image_capture.cap.release()
    cv2.destroyAllWindows()
