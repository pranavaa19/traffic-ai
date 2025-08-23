# AI-Based Traffic Flow Estimator + Smart Signal Controller

This repository contains a student project that detects vehicles from traffic videos and
drives an adaptive traffic light controller (Arduino demo).

## Team
- Pranavaa — Data curation, documentation, utility scripts
- Praanesh — Detection model (YOLO) training & optimization
- Akash — Metrics + adaptive signal logic + integration
- Tam — Hardware demo (Arduino LEDs) + testing

## Quick Start (Windows)
```powershell
# 1) Create and activate a virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 2) Upgrade pip and install minimal requirements
python -m pip install --upgrade pip
pip install -r requirements.txt
```

> Note: Large raw videos are **not** tracked in Git to keep the repo small.
> Store them in a shared Google Drive/OneDrive folder and copy locally into `data/raw_videos/`
> when you need to work with them.

## Project Structure
```
traffic-ai/
 ├─ data/
 │   ├─ raw_videos/   # store .mp4/.avi here (ignored by Git)
 │   ├─ frames/       # extracted frames (ignored by Git)
 │   ├─ labels/       # YOLO txt labels (optional commit)
 │   └─ splits/       # train/val/test file lists
 ├─ docs/
 │   ├─ report/       # report markdown/notes
 │   └─ slides/       # slide outlines
 ├─ diagrams/         # draw.io or images for block diagrams
 ├─ scripts/          # small helper scripts
 ├─ results/          # evaluation outputs, screenshots
 ├─ dataset.yaml      # dataset definition (edit names as needed)
 ├─ requirements.txt  # minimal deps for light tasks
 ├─ .gitignore
 └─ README.md
```

## License
MIT (see LICENSE file).

---
*Generated scaffold on 2025-08-23T05:14:29.753955Z*
