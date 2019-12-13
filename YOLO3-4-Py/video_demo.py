import time

from pydarknet import Detector, Image
import cv2

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process a video.')
    parser.add_argument('path', metavar='video_path', type=str,
                        help='Path to source video')

    args = parser.parse_args()
    print("Source Path:", args.path)
    cap = cv2.VideoCapture(args.path)


    average_time = 0

    net = Detector(bytes("cfg/yolov3.cfg", encoding="utf-8"), bytes("weights/yolov3.weights", encoding="utf-8"), 0,
                   bytes("cfg/coco.data", encoding="utf-8"))

    out = cv2.VideoWriter('output_video.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (640,360))

    while True:
        r, frame = cap.read()
        if r:
            start_time = time.time()

            # Only measure the time taken by YOLO and API Call overhead

            dark_frame = Image(frame)
            results = net.detect(dark_frame)
            del dark_frame

            end_time = time.time()
            average_time = average_time * 0.8 + (end_time-start_time) * 0.2

            pets = 0
            humans = 0

            # print("Total Time:", end_time-start_time, ":", average_time)

            for cat, score, bounds in results:
                if cat in [b'cat', b'dog'] and score >= 0.9:
                    pets += 1
                elif cat == b'person' and score >- 0.9:
                    humans += 1
                else:
                    continue


                x, y, w, h = bounds
                cv2.rectangle(frame, (int(x-w/2),int(y-h/2)),(int(x+w/2),int(y+h/2)),(0,0,255))
                #cv2.putText(frame, str(cat.decode("utf-8")), (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0))
            outputstring = "humans: " + str(humans) + ", pets: " + str(pets)
            cv2.putText(frame, outputstring, (20, 330), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
            out.write(frame)
            print(outputstring)
            cv2.imshow("preview", frame)


        k = cv2.waitKey(1)
        if k == 0xFF & ord("q"):
            break
    cap.release()
    out.release()
