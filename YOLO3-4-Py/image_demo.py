from pydarknet import Detector, Image
import cv2
import os

if __name__ == "__main__":
    # net = Detector(bytes("cfg/densenet201.cfg", encoding="utf-8"), bytes("densenet201.weights", encoding="utf-8"), 0, bytes("cfg/imagenet1k.data",encoding="utf-8"))

    net = Detector(bytes("cfg/yolov3.cfg", encoding="utf-8"), bytes("weights/yolov3.weights", encoding="utf-8"), 0, bytes("cfg/coco.data",encoding="utf-8"))
    
    for name in ["data/dog.jpg", "data/giraffe.jpg", "data/horses.jpg", "data/person.jpg"]:
        img = cv2.imread(os.path.join(os.environ["DARKNET_HOME"],name))
        img2 = Image(img)

        results = net.detect(img2)
        # print(results)
        pets = 0
        humans = 0

        for cat, score, bounds in results:
            print(cat)
            if cat in [b'cat', b'dog'] and score >= 0.9:
                pets += 1
            if cat == b'person' and score >- 0.9:
                humans += 1

        print("Humans: " + str(humans) + ", Pets: " + str(pets))
            # x, y, w, h = bounds
            # cv2.rectangle(img, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), (255, 0, 0), thickness=2)
            # cv2.putText(img,str(cat.decode("utf-8")),(int(x),int(y)),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0))

        # cv2.imshow("output", img)

        # cv2.waitKey(0)
