import math 
import time
def distance(p1, p2):
    return math.hypot(p2[0]-p1[0], p2[1]-p1[1])

def fingersUp(lmlist):
  if not lmlist:
    return [0,0,0,0,0]
  fingers=[]
  if lmlist[4][1]<lmlist[3][1]:
    fingers.append(1)
  else:
    fingers.append(0)

  for tipid in (8,12,16,20):
    if lmlist[tipid][2]<lmlist[tipid-2][2]:
      fingers.append(1)
    else:
      fingers.append(0)
  return fingers

def brushSize(lmlist):
   if not lmlist :
        return {"brush_size": "medium"} 
   thumb_tip=lmlist[4][1:3]
   index_tip=lmlist[8][1:3]
   dist = distance(thumb_tip, index_tip)
   if dist < 90:         
        return {"brush_size": "small"}
   elif 90 <= dist <= 120:   
        return {"brush_size": "medium"}
   else:                 
        return {"brush_size": "large"}


last_mode = "Idle"
current_brush_size = "medium"
last_color = ((255, 255, 255), "White")
mode_counter = 0
last_fist_time = 0
last_clear_time = 0
saved = False 

def gestures(lmlist,colors,w,box_h):
  global last_mode,current_brush_size,last_color,mode_counter,last_fist_time,saved

  result = {"mode": last_mode, "brush_size": current_brush_size, "color":last_color}
  
  if not lmlist:
    last_mode="idle"
    return result
  
  fingers=fingersUp(lmlist)
  current_mode = "Idle"

  if fingers==[0,1,0,0,0]:
      current_mode = "Draw"
  elif fingers == [0,1,1,0,0]:
      current_mode = "Color Select"
  elif fingers == [0,1,1,1,0]:
      current_mode = "Eraser"
  elif fingers == [0,1,1,1,1]:
      current_mode = "Select Brush"
  elif fingers == [1,1,1,1,1]:
      current_mode = "Clear"
  elif fingers == [0,0,0,0,0]:
    current_time = time.time()
    if last_fist_time == 0:  # start timer
        last_fist_time = current_time 
        saved=False
    elif current_time - last_fist_time > 3 and not saved: # hold fist 3s
          current_mode = "Saving"
          saved=True    
          last_fist_time = float('inf')   # reset after save
  else:
        last_fist_time = 0
        saved=False


  if current_mode == "Saving":
    last_mode = "Saving"
    mode_counter = 0
  else:
    if current_mode == last_mode:
        mode_counter = 0
    else:
        mode_counter += 1
        if mode_counter > 5:  
            last_mode = current_mode
            mode_counter = 0

  if last_mode == "Select Brush":
        current_brush_size = brushSize(lmlist)["brush_size"]
  
  if current_mode=="Color Select" and lmlist:
    if fingers[1] == 1 and fingers[2] == 1:
      if lmlist[8][2]<box_h:
        indexfinger_x = lmlist[8][1]  
        box_width = w / len(colors)
        color_index = min(int(indexfinger_x // box_width), len(colors)-1)
        last_color = colors[color_index]

  result["mode"] = last_mode
  result["brush_size"] = current_brush_size
  result["color"]=last_color
  return result
  

# def gestures(lmlist, colors, w, box_h):
#     global last_mode, current_brush_size, last_color, mode_counter, last_fist_time, saved, last_clear_time

#     result = {"mode": last_mode, "brush_size": current_brush_size, "color": last_color}

#     if not lmlist:
#         last_mode = "Idle"
#         return result

#     fingers = fingersUp(lmlist)
#     current_mode = "Idle"


#     if fingers == [0, 1, 0, 0, 0]:
#         current_mode = "Draw"
#     elif fingers == [0, 1, 1, 0, 0]:
#         current_mode = "Color Select"
#     elif fingers == [0, 1, 1, 1, 0]:
#         current_mode = "Eraser"
#     elif fingers == [0, 1, 1, 1, 1]:
#         current_mode = "Select Brush"
#     elif fingers == [1, 1, 1, 1, 1]:
#         if last_clear_time == 0:
#             last_clear_time = time.time()
#         elif time.time() - last_clear_time > 1.5:
#             current_mode = "Clear"
#             last_clear_time = 0
#     elif fingers == [0, 0, 0, 0, 0]:
#         if last_fist_time == 0:
#             last_fist_time = time.time()
#             saved = False
#         elif time.time() - last_fist_time > 3 and not saved:
#             current_mode = "Saving"
#             saved = True
#             last_fist_time = 0
#     else:
#         last_fist_time = 0
#         last_clear_time = 0


#     if current_mode == "Saving":
#         last_mode = "Saving"
#         mode_counter = 0
#     else:
#         if current_mode == last_mode:
#             mode_counter = 0
#         else:
#             mode_counter += 1
#             if mode_counter > 5:
#                 last_mode = current_mode
#                 mode_counter = 0

#     if last_mode == "Select Brush":
#         current_brush_size = brushSize(lmlist)["brush_size"]

#     if current_mode == "Color Select" and fingers[1] == 1 and fingers[2] == 1:
#         if lmlist[8][2] < box_h:  # only select from top area
#             indexfinger_x = lmlist[8][1]
#             box_width = w / len(colors)
#             color_index = min(int(indexfinger_x // box_width), len(colors) - 1)
#             last_color = colors[color_index]

#     result["mode"] = last_mode
#     result["brush_size"] = current_brush_size
#     result["color"] = last_color
#     return result