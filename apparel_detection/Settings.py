import os

from common.logging.console_logger import ConsoleLogger


class Settings:
    sep = None
    if os.name == 'nt':
        sep = "\\"
    else:
        sep = "/"

    PROJECT_NAME = 'Warehouse_Apparel_Detection'

    root_path = os.getcwd().split(PROJECT_NAME)[0] + PROJECT_NAME + sep
    # print(APPLICATION_PATH)
    # setting up logs path
    LOGS_DIRECTORY = root_path + "logs" + sep + "logs.txt"

    input_image_path = "./apparel_detection/yolo_detector/inference/images/"
    weights_path = "./apparel_detection/yolo_detector/weights/best.pt"
    output_path = "./apparel_detection/yolo_detector/inference/output/"
    input_image_name = "input_image.jpg"
    output_image_name = "output_image.jpg"
    color_image = 'color_img.jpg'

    # setting up logger
    logger = ConsoleLogger(filename=LOGS_DIRECTORY)
