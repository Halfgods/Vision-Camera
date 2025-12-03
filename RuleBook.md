---

# 📘 **AI App Rule Book (for your CV + Streamlit Camera App)**

Keep this document with your repo — it will guide every decision.

---

# **1. Purpose Rule**

**The app should feel like a toolkit, not a random collection of demos.**
Every feature must support one of these goals:

1. **Capture** (camera/scan)
2. **Enhance** (crop/brightness/filters)
3. **Analyze** (QR, contour cut, tracking)
4. **Create** (drawing, cutout, AR overlays)

If a feature doesn’t fit → remove it.

---

# **2. Visual Design Rule**

Keep your UI minimal. Avoid childish colors or gradients.

### **Use this color palette (consistent across all pages):**

**Primary**
1. Neon Aqua

#86D1DF
→ Light, cool, very “cyber city glow”.

2. Neon Magenta / Pink

#C83A5A
→ Strong accent color, perfect for buttons or highlights.

3. Midnight Indigo

#334A87
→ Deep bluish-indigo, good for card backgrounds or sections.

4. Electric Blue

#4C66C4
→ Clean blue, great for UI components, tabs, sliders.

Background (from the image)

#0C0520
→ Near-black purple — gives the whole neon theme its punch.

**Accent**

* `#3B82F6` → Highlight buttons (blue)
* `#10B981` → Success / processed indicator (green)
* `#F59E0B` → Warnings (yellow)



**Text**

* `#111827` (dark)

---

# **3. Typography Rule**

Use Streamlit recommended fonts (built-in):

* **Primary:** Sans-serif or Times New Roman
* **Headers:** Bold
* **Subtext:** Medium
* **Never use cursive, serif, or handwritten fonts.**

---

# **4. Structure Rule (VERY IMPORTANT)**

Your app must split code by responsibility:

---

## 🎛 **A) `scripts/` (Processing Layer)**

All heavy OpenCV logic lives here.

**Example structure:**

```
Scripts/
│── qr_scanner.py
│── pdf_scanner.py
│── contour_cut.py
│── brightness.py
│── crop.py
│── hand_tracking.py
│── enhancements.py
│── utils.py
```

Rules:

* No UI code allowed
* Only functions that take input → return output
* Must be reusable
* Must not import Streamlit
* Keep logic clean and documented

---

## 🖥 **B) `pages/` (UI Layer)**

Every major feature gets its own page.

Example:

```
pages/
│── 1_Camera.py
│── 2_Document_Tools.py
│── 3_Image_Tools.py
│── 4_AI_Tools.py
│── 5_AR_Showcase.py
│── 6_Playground.py
```

Rules:

* Pages only handle user interaction
* Pages call functions from `scripts/`
* No heavy processing inside UI
* All pages have same layout pattern (explained below)

---

## 🗂 **C) `assets/`**

Icons, thumbnails, sample images.
Keeps your repo clean.

---

# **5. UX Rule (Amazon-inspired Section Layout)**

The Amazon screenshot you shared uses a **grid of sections** with clean cards.

We’ll create your own version:

---

## 📐 **App Home Page Layout (Mandatory)**

Use Streamlit columns just like Amazon’s layout.

**Top Section** – *Hero Banner*

* Title: “Vision Toolkit”
* Subtitle: “Your camera, reinforced by AI.”
* One large banner (light grey background)

**Section 1 – Quick Actions**
Cards like:

* Scan QR
* Scan Document
* Capture Image
* Crop & Enhance

**Section 2 – Vision Tools**
Cards:

* Contour Cut
* Color Tracking
* Auto Align
* Virtual Drawing

**Section 3 – AI & AR (Future)**
Cards:

* Background Removal (AI)
* Face Filter
* ArUco AR Demo

**Section 4 – Utilities**
Cards:

* Gallery
* Batch Processing
* Settings

---

# **6. Card Rules**

Each card must have:

* Clean icon
* Title (short)
* One-line description
* A single button
* Soft shadow (`st.container()` + CSS)
* Proper spacing

Avoid clutter.

---

# **7. Navigation Rule**

Use Streamlit’s multipage system.
Do **NOT** use dropdowns for everything — keep things simple:

* Home
* Capture
* Document Tools
* Image Tools
* AI Tools
* AR
* Playground

---

# **8. Library Rule**

Use these libraries:

### **Mandatory**

* OpenCV (`cv2`) → all image processing
* NumPy → array operations
* Pyzbar or OpenCV DNN → QR
* Streamlit → UI
* Pillow → image I/O
* PyMuPDF → PDF generation (optional)

---

# **9. Coding Standard Rule**

* Use **snake_case functions**
* One feature = one file
* All processing functions return clean outputs
* No global variables
* Add docstrings for every function

---

# **10. What To Avoid**

Strict.

* ❌ Fancy animations
* ❌ Too many colors
* ❌ Mixing UI + logic in the same file
* ❌ Uploading 10 different image versions randomly
* ❌ Using absolute paths
* ❌ Writing 200-line pages
* ❌ Making everything “experimental”

If it looks messy → you redo it. No excuses.

---

# **11. What You MUST Do**

* ✔ Keep UI clean and consistent
* ✔ Test every script independently
* ✔ Add basic logging (print is fine for now)
* ✔ Make functions pure (input → output)
* ✔ Add thumbnails for tools
* ✔ Follow your feature categories strictly

---
