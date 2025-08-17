# drawing logic
import cv2
import os

def draw_on_canvas(canvas, lmlist, color,prev_pt, brush_size):
    if not lmlist:#len(lmlist)==0
        return canvas,prev_pt
    x = lmlist[8][1]
    y = lmlist[8][2]
    if prev_pt is None:
        prev_pt=(x,y)
    canvas=cv2.line(canvas,prev_pt,(x,y),color[0],brush_size)
    prev_pt=(x,y)
    return canvas,prev_pt




save_count = 0

# make sure folder exists
if not os.path.exists("saved_drawings"):
    os.makedirs("saved_drawings")

def save_drawing(canvasonly,folder="saved_drawings"):
    global save_count
    if not os.path.exists(folder):
        os.makedirs(folder)
    save_count += 1 
    filename = f"saved_drawings/drawing_{save_count}.png"
    cv2.imwrite(filename, canvasonly)
    print(f"Drawing saved as drawing_{save_count}.png")


