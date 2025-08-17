# detecting hand landmarks
import cv2
import mediapipe as mp

class DetectHands():
   def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mpDraw = mp.solutions.drawing_utils
   def findHand(self,frame,draw=True):
      rgbframe=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
      self.res=self.hands.process(rgbframe) 
      if self.res.multi_hand_landmarks:
        for handlms in self.res.multi_hand_landmarks:
          if draw:
            self.mpDraw.draw_landmarks(frame,handlms,self.mpHands.HAND_CONNECTIONS)
      return frame
   def findPosition(self, frame, handNo=0):
      lmList = []
      if self.res.multi_hand_landmarks:
          myHand = self.res.multi_hand_landmarks[handNo]
          for id, lm in enumerate(myHand.landmark):
              h, w, c = frame.shape
              cx, cy = int(lm.x * w), int(lm.y * h) 
              lmList.append((id, cx, cy))
      return lmList
#  lmlist=[
#   (0, 520, 680),   # Wrist
#   (1, 540, 600),   # Thumb_CMC
#   (2, 560, 560),
#   ...
#   (8, 640, 300),   # Index fingertip
#   ...
#   (20, 720, 200)   # Pinky tip
# ]

def main():
  cap=cv2.VideoCapture(0)
  detobj=DetectHands()
  while True:
    success,frame=cap.read()
    frame=cv2.flip(frame,1)
    if not success:
      break
    frame=detobj.findHand(frame)
    cv2.imshow("video",frame)
    li=detobj.findPosition(frame)
    if len(li)!=0:
       print(li[20])
    if cv2.waitKey(1) &0xFF == ord("q"):
      break

  cap.release()
  cv2.destroyAllWindows()

if __name__=="__main__":
  main()