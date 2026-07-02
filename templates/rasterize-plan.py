#!/usr/bin/env python3
"""
Rasterize a plan PDF page (or a cropped region) to a high-res PNG for use as the
background of a takeoff diagram.  Part of the standard takeoff-diagram workflow.

Setup (once per environment):
    pip install pymupdf

Usage:
    # whole first page at 3x
    python3 rasterize-plan.py plan.pdf out.png --page 0 --zoom 3

    # crop to the floor-plan region (PDF points x0 y0 x1 y1) at 3.2x
    python3 rasterize-plan.py plan.pdf out.png --page 0 --zoom 3.2 --clip 470 135 2560 1770

Tip: render once with --zoom 1 and no clip, open the PNG, read off the pixel box
of the floor plan, divide by the zoom to get PDF points, then re-run with --clip.
"""
import argparse, fitz  # PyMuPDF

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf"); ap.add_argument("out")
    ap.add_argument("--page", type=int, default=0)
    ap.add_argument("--zoom", type=float, default=3.0)
    ap.add_argument("--clip", type=float, nargs=4, metavar=("X0", "Y0", "X1", "Y1"),
                    default=None, help="crop rectangle in PDF points")
    a = ap.parse_args()
    doc = fitz.open(a.pdf); page = doc[a.page]
    m = fitz.Matrix(a.zoom, a.zoom)
    clip = fitz.Rect(*a.clip) if a.clip else None
    pix = page.get_pixmap(matrix=m, clip=clip)
    pix.save(a.out)
    print(f"wrote {a.out}  {pix.width}x{pix.height}px  page={page.rect}  clip={clip}")

if __name__ == "__main__":
    main()
