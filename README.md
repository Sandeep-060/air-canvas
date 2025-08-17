# Air Canvas (OpenCV + MediaPipe)

A real-time drawing application that lets you **draw in the air** using just your hand — no mouse, no touch, just gestures.

Built entirely with **Python, OpenCV, and MediaPipe**, this project turns your webcam into a canvas, powered by computer vision and AI-based hand tracking.


> Built with: Python, OpenCV, MediaPipe, NumPy

---

## 🎯 Features

- **Draw** by pointing your **index finger**.
- **Pick colors** by hovering **index + middle fingers** over the top palette bar.
- **Eraser mode** with **index + middle + ring fingers**.
- **Select brush size** with **index + middle + ring + pinky**.
- **Clear everything** with **all five fingers open**.
- **Auto‑save** by making a **fist** for ~3 seconds → saves to `saved_drawings/`.

> Internally, finger states are read as `[thumb, index, middle, ring, pinky]` and mapped to modes:
>
> - `[0,1,0,0,0]` → **Draw**
> - `[0,1,1,0,0]` → **Color Select**
> - `[0,1,1,1,0]` → **Eraser**
> - `[0,1,1,1,1]` → **Select Brush**
> - `[1,1,1,1,1]` → **Clear**
> - `[0,0,0,0,0]` held ~3s → **Saving**

---

## 🖼️ Demo

Add a short demo GIF or image here (optional but great for LinkedIn/README):

```
```
![Air Canvas demo](/demo/aircanvas_layout.png)
![Air Canvas demo](/demo/savedimg.png)

---



---

## ⚙️ Installation

> Works on Windows / macOS / Linux with Python 3.10–3.12.

1) **Clone or download** the repo
```bash
git clone https://github.com/Sandeep-060/air-canvas.git
cd air-canvas
```

2) **Create a virtual environment** (pick one)

**Windows (PowerShell):**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

**macOS / Linux (bash/zsh):**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3) **Install dependencies**
```bash
pip install -r requirements.txt
```


4) **Run**
```bash
python main.py
```

---

## How to use

- A color **palette bar** appears at the **top** of the window.
- **Draw**: Show only your **index** finger; move to draw.
- **Color Select**: Show **index + middle** fingers and hover over a color in the palette.
- **Select Brush**: Show **index + middle + ring + pinky**; brush size cycles between `small`, `medium`, `large` (see on‑screen status).
- **Eraser**: Show **index + middle + ring** fingers; erases using the current brush size.
- **Clear**: Show **all five fingers**.
- **Save**: Make a **fist** (no fingers up) and hold for ~3 seconds — saved to `saved_drawings/drawing_#.png`.

> Window shortcuts: Press `q` to quit.

