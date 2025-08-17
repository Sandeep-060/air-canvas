import cv2
import numpy as np
import hand_detection as hd
import gestures as gs
import drawing as dw

cap=cv2.VideoCapture(0)
colors = [
  ((255,0,0),"Blue"),
  ((0,255,0),"Green"),
  ((0,0,255),"Red"),
  ((0,255,255),"Yellow"),
  ((255,255,255),"White"),
  ((0,165,255),"Orange"),
  ((128,0,128),"Purple"),
]

current_color=((255,255,255),"White")
canavas=None
dectobj=hd.DetectHands()
prev_pt=None
brushes = {
    "small": 8,
    "medium":15,
    "large": 25
}

while True:
  success,frame=cap.read()
  if not success:
    break

  frame=cv2.resize(frame,(1000,730))
  frame=cv2.flip(frame,1)

  frame=dectobj.findHand(frame)
  lmlist = dectobj.findPosition(frame)

  gesture = gs.gestures(lmlist,colors,w=1000,box_h=50)
  mode = gesture.get("mode")
  current_brush=gesture.get("brush_size")
  current_brush_size=brushes.get(current_brush)

  if canavas is None:
    canavas=np.zeros_like(frame)

  if mode=="Color Select":
    current_color = gesture.get("color") 
    prev_pt = None
  elif mode == "Eraser":
      current_color = ((0,0,0),"Eraser") 
      canavas, prev_pt = dw.draw_on_canvas(canavas, lmlist, current_color, prev_pt, current_brush_size)
  elif mode == "Draw":
      canavas, prev_pt = dw.draw_on_canvas(canavas, lmlist, current_color, prev_pt, current_brush_size)
  elif mode == "Clear":
    canavas = np.zeros_like(frame)  # reset to blank
    prev_pt = None
  elif mode=="Saving":
     dw.save_drawing(canavas)
     gs.last_mode="Idle"
     prev_pt=None
  else:
     prev_pt = None

  # Merge camera frame + canvas (0.5 opacity for canvas)
  merged=cv2.addWeighted(frame,0.8,canavas,1,10)
  box_w=merged.shape[1]//len(colors)
  for i,(color,name) in enumerate(colors):
    x1=i*box_w
    x2=(i+1)*box_w
    cv2.rectangle(merged,(x1,0),(x2,50),color,-1)
    cv2.putText(merged,name,(x1+10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),2)

  status_text = f"Mode: {mode}          |Color: {current_color[1]}          |Brush: {current_brush}"
  cv2.rectangle(merged, (0, 55), (1000,100), (50, 50, 50), -1)
  cv2.putText(merged, status_text, (20, 85),
              cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

  cv2.imshow("my video", frame)      # Raw camera feed
  cv2.imshow("my canavas", canavas)  # Drawing-only layer
  cv2.imshow("merged", merged)       # Final output with palette

  if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()