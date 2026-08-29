#!/usr/bin/env python3
"""
ChapelCloud crest — soft shield, interlocking curved plates, witness star.
Gaps are built into plate geometry (uniform width), not a radial starburst.
"""

from __future__ import annotations

import math
import subprocess
from pathlib import Path

OUT = Path(__file__).resolve().parent
EXPORTS = OUT.parent / "exports"

PRESENCE = "#2a4054"
PRESENCE_DEEP = "#1a2b3a"
COVERING = "#7a94a8"
WITNESS = "#b8923f"
CLOUD = "#f3f5f7"
INK = "#121820"
WHITE = "#ffffff"

CX, CY = 50.0, 45.5
GAP = 2.1
STAR_R = 6.5
STAR_W = 1.75
RING = STAR_R + GAP  # clear pocket around star


def f(n: float) -> str:
    s = f"{n:.3f}".rstrip("0").rstrip(".")
    return s if s not in ("", "-") else "0"


def polar(r: float, deg: float) -> tuple[float, float]:
    a = math.radians(deg)
    return (CX + r * math.cos(a), CY + r * math.sin(a))


def shield() -> str:
    return (
        "M 21,6.5 L 79,6.5 "
        "C 87,6.5 93,13 93,21.5 "
        "C 93,42 83,63 51.3,94.5 "
        "C 50.7,95.3 50.2,95.6 50,95.6 "
        "C 49.8,95.6 49.3,95.3 48.7,94.5 "
        "C 17,63 7,42 7,21.5 "
        "C 7,13 13,6.5 21,6.5 Z"
    )


def star() -> str:
    cx, cy, tip, w = CX, CY, STAR_R, STAR_W
    return (
        f"M {f(cx)},{f(cy - tip)} "
        f"L {f(cx + w)},{f(cy - w)} "
        f"L {f(cx + tip)},{f(cy)} "
        f"L {f(cx + w)},{f(cy + w)} "
        f"L {f(cx)},{f(cy + tip)} "
        f"L {f(cx - w)},{f(cy + w)} "
        f"L {f(cx - tip)},{f(cy)} "
        f"L {f(cx - w)},{f(cy - w)} Z"
    )


def plates() -> list[tuple[str, str, str]]:
    """
    Six interlocking plates + two deep anchors.
    Inner edges stop at RING so the star pocket is uniform.
    Adjacent plates leave ~GAP between facing edges.

    Returns (id, fill, path-d) for animation targeting.
    """
    r0 = RING  # inner clearance

    # Helper points around the ring for plate inner corners
    # Cardinals/diagonals used as seam aims
    N = polar(r0, 270)
    NE = polar(r0, 315)
    E = polar(r0, 0)
    SE = polar(r0, 45)
    S = polar(r0, 90)
    SW = polar(r0, 135)
    W = polar(r0, 180)
    NW = polar(r0, 225)

    return [
        # ===== Deep anchors (under) =====
        (
            "plate-anchor-bottom",
            PRESENCE_DEEP,
            # Bottom tip anchor — fills lower third under weave
            f"M 14,58 "
            f"C 18,74 32,88 48.8,94.2 "
            f"L 51.2,94.2 "
            f"C 68,88 82,74 86,58 "
            f"C 78,62 68,66 58,66 "
            f"C 54,66 52,64 {f(S[0])},{f(S[1])} "
            f"C 48,64 46,66 42,66 "
            f"C 32,66 22,62 14,58 Z",
        ),
        # ===== Primary outer mantles =====
        (
            "plate-mantle-left",
            PRESENCE,
            # Left mantle — tall plate along left wall, inner edge arcs toward ring
            f"M 9,22 "
            f"C 9,13 15,7.5 23,7.5 "
            f"L 44,7.5 "
            f"C 40,12 36,18 33.5,26 "
            f"C 30,40 29,52 31,64 "
            f"C 32,72 35,78 39,84 "
            f"C 30,76 18,64 12,52 "
            f"C 9,42 9,32 9,22 Z",
        ),
        (
            "plate-mantle-right",
            PRESENCE,
            # Right mantle
            f"M 91,22 "
            f"C 91,13 85,7.5 77,7.5 "
            f"L 56,7.5 "
            f"C 60,12 64,18 66.5,26 "
            f"C 70,40 71,52 69,64 "
            f"C 68,72 65,78 61,84 "
            f"C 70,76 82,64 88,52 "
            f"C 91,42 91,32 91,22 Z",
        ),
        # ===== Mid covering plates (the weave) =====
        (
            "plate-ribbon-ul",
            COVERING,
            # Upper-left ribbon — sweeps from top into left of star
            f"M 20,14 "
            f"C 28,9 38,8 46,10 "
            f"C 44,16 41,22 38.5,28 "
            f"C 36,36 35,42 {f(NW[0])},{f(NW[1])} "
            f"C 32,40 26,34 22,28 "
            f"C 19,22 18,17 20,14 Z",
        ),
        (
            "plate-ribbon-ur",
            COVERING,
            # Upper-right ribbon
            f"M 80,14 "
            f"C 72,9 62,8 54,10 "
            f"C 56,16 59,22 61.5,28 "
            f"C 64,36 65,42 {f(NE[0])},{f(NE[1])} "
            f"C 68,40 74,34 78,28 "
            f"C 81,22 82,17 80,14 Z",
        ),
        (
            "plate-weave-left",
            COVERING,
            # Mid-left weave plate — vertical curved band west of star
            f"M 16,34 "
            f"C 22,28 28,26 {f(W[0] - 0.2)},{f(W[1])} "
            f"C 30,40 31,48 30,56 "
            f"C 28,62 24,66 20,68 "
            f"C 14,58 12,46 16,34 Z",
        ),
        (
            "plate-weave-right",
            COVERING,
            # Mid-right weave plate
            f"M 84,34 "
            f"C 78,28 72,26 {f(E[0] + 0.2)},{f(E[1])} "
            f"C 70,40 69,48 70,56 "
            f"C 72,62 76,66 80,68 "
            f"C 86,58 88,46 84,34 Z",
        ),
        # ===== Inner aperture plates (closest to star) =====
        (
            "plate-inner-top",
            PRESENCE,
            # Top inner plate — arches over star
            f"M 32,12 "
            f"C 38,8 44,7 50,7 "
            f"C 56,7 62,8 68,12 "
            f"C 64,18 58,24 52,26.5 "
            f"C 51,26.8 50.4,{f(N[1])} {f(N[0])},{f(N[1])} "
            f"C 49.6,{f(N[1])} 49,26.8 48,26.5 "
            f"C 42,24 36,18 32,12 Z",
        ),
        (
            "plate-inner-bottom",
            PRESENCE_DEEP,
            # Bottom inner plate — under star into tip
            f"M 34,58 "
            f"C 40,54 46,52.5 {f(S[0])},{f(S[1])} "
            f"C 54,52.5 60,54 66,58 "
            f"C 62,70 56,82 50.5,90 "
            f"C 49.5,82 44,70 34,58 Z",
        ),
        (
            "plate-tuck-ll",
            PRESENCE,
            # Lower-left tuck (over deep, under covering)
            f"M 18,52 "
            f"C 24,48 30,48 {f(SW[0])},{f(SW[1])} "
            f"C 36,52 38,58 38,64 "
            f"C 32,68 24,66 18,60 "
            f"C 16,57 16,54 18,52 Z",
        ),
        (
            "plate-tuck-lr",
            PRESENCE,
            # Lower-right tuck
            f"M 82,52 "
            f"C 76,48 70,48 {f(SE[0])},{f(SE[1])} "
            f"C 64,52 62,58 62,64 "
            f"C 68,68 76,66 82,60 "
            f"C 84,57 84,54 82,52 Z",
        ),
    ]


def gap_fill(fill: str, *, with_ids: bool = True) -> str:
    """
    Star pocket + cardinal seams + curved plate seams.
    Uniform stroke width = GAP throughout.
    """

    def eid(name: str) -> str:
        return f' id="{name}"' if with_ids else ""

    els = [
        f'<circle{eid("gap-pocket")} cx="{f(CX)}" cy="{f(CY)}" '
        f'r="{f(RING)}" fill="{fill}"/>'
    ]

    # Cardinal seams (symmetric): from ring toward rim, stop short of edge
    x1, y1 = polar(RING - 0.05, 270)
    els.append(
        f'<path{eid("gap-seam-n")} fill="none" stroke="{fill}" stroke-width="{f(GAP)}" '
        f'stroke-linecap="butt" d="M {f(x1)},{f(y1)} L {f(CX)},8"/>'
    )
    x1, y1 = polar(RING - 0.05, 90)
    els.append(
        f'<path{eid("gap-seam-s")} fill="none" stroke="{fill}" stroke-width="{f(GAP)}" '
        f'stroke-linecap="butt" d="M {f(x1)},{f(y1)} L {f(CX)},91"/>'
    )
    x1, y1 = polar(RING - 0.05, 0)
    x2, y2 = polar(41.5, 0)
    els.append(
        f'<path{eid("gap-seam-e")} fill="none" stroke="{fill}" stroke-width="{f(GAP)}" '
        f'stroke-linecap="butt" d="M {f(x1)},{f(y1)} L {f(x2)},{f(y2)}"/>'
    )
    x1, y1 = polar(RING - 0.05, 180)
    x2, y2 = polar(41.5, 180)
    els.append(
        f'<path{eid("gap-seam-w")} fill="none" stroke="{fill}" stroke-width="{f(GAP)}" '
        f'stroke-linecap="butt" d="M {f(x1)},{f(y1)} L {f(x2)},{f(y2)}"/>'
    )

    # Curved seams between outer mantle and mid ribbons
    els.append(
        f'<path{eid("gap-seam-mantle-left")} fill="none" stroke="{fill}" '
        f'stroke-width="{f(GAP)}" stroke-linecap="round" '
        f'd="M 29,16 C 26,30 26,46 30,64"/>'
    )
    els.append(
        f'<path{eid("gap-seam-mantle-right")} fill="none" stroke="{fill}" '
        f'stroke-width="{f(GAP)}" stroke-linecap="round" '
        f'd="M 71,16 C 74,30 74,46 70,64"/>'
    )
    # Vault seams under top plate / above bottom plate (meet ring at N/S)
    nx, ny = polar(RING, 270)
    sx, sy = polar(RING, 90)
    els.append(
        f'<path{eid("gap-seam-vault-top")} fill="none" stroke="{fill}" '
        f'stroke-width="{f(GAP)}" stroke-linecap="round" '
        f'd="M 34,22 C 40,28 46,30.5 {f(nx)},{f(ny)} C 54,30.5 60,28 66,22"/>'
    )
    els.append(
        f'<path{eid("gap-seam-vault-bottom")} fill="none" stroke="{fill}" '
        f'stroke-width="{f(GAP)}" stroke-linecap="round" '
        f'd="M 34,60 C 40,54 46,52 {f(sx)},{f(sy)} C 54,52 60,54 66,60"/>'
    )
    return "\n    ".join(els)


def crest_colored(punch: str = CLOUD) -> str:
    plate_els = "\n".join(
        f'    <path id="{pid}" fill="{fill}" d="{d}"/>'
        for pid, fill, d in plates()
    )
    return "\n".join(
        [
            '<g id="crest">',
            f'  <path id="shield" fill="{PRESENCE_DEEP}" d="{shield()}"/>',
            '  <g id="crest-inner" clip-path="url(#shieldClip)">',
            '    <g id="plates">',
            plate_els,
            "    </g>",
            '    <g id="gaps">',
            f"    {gap_fill(punch)}",
            "    </g>",
            f'    <path id="star" fill="{WITNESS}" d="{star()}"/>',
            "  </g>",
            "</g>",
        ]
    )


def defs() -> str:
    return f"""  <defs>
    <clipPath id="shieldClip"><path d="{shield()}"/></clipPath>
  </defs>"""


def mark_field(field: str, title: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="{title}">
  <title>{title}</title>
  <desc>Geometric crest of interlocking curved panels with a central four-pointed witness star.</desc>
{defs()}
  <rect id="field" width="100" height="100" rx="18" fill="{field}"/>
  <g id="mark" transform="translate(50 51) scale(0.80) translate(-50 -45.5)">
{crest_colored()}
  </g>
</svg>
"""


def mark_alone() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="ChapelCloud mark">
  <title>ChapelCloud mark</title>
  <desc>Geometric crest of interlocking curved panels with a central four-pointed witness star.</desc>
{defs()}
{crest_colored()}
</svg>
"""


def mark_mono(ink: str, field: str | None, title: str) -> str:
    # Mask from full-color structure: white where ink should show
    # Approximate: solid shield minus gap strokes plus star
    gap = gap_fill("black", with_ids=False)
    mask = f"""    <mask id="markMask" maskUnits="userSpaceOnUse">
      <rect width="100" height="100" fill="black"/>
      <path fill="white" d="{shield()}"/>
      {gap}
      <path fill="white" d="{star()}"/>
    </mask>
"""
    field_el = (
        f'  <rect id="field" width="100" height="100" rx="18" fill="{field}"/>\n'
        if field
        else ""
    )
    if field:
        body = f'''{field_el}  <g id="mark" transform="translate(50 51) scale(0.80) translate(-50 -45.5)">
    <rect id="crest" width="100" height="100" fill="{ink}" mask="url(#markMask)"/>
  </g>'''
    else:
        body = (
            f'{field_el}  <rect id="crest" width="100" height="100" '
            f'fill="{ink}" mask="url(#markMask)"/>'
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="{title}">
  <title>{title}</title>
  <desc>Monochrome crest — interlocking panels read through uniform negative space.</desc>
  <defs>
    <clipPath id="shieldClip"><path d="{shield()}"/></clipPath>
{mask}  </defs>
{body}
</svg>
"""


def wordmark(x, y, *, fill=PRESENCE, size=40, anchor="start") -> str:
    return (
        f'<text id="wordmark" x="{f(x)}" y="{f(y)}" fill="{fill}" '
        f'font-family="Newsreader, Georgia, \'Source Serif 4\', serif" '
        f'font-size="{f(size)}" font-weight="600" letter-spacing="-0.02em" '
        f'text-anchor="{anchor}">ChapelCloud</text>'
    )


def lockup_h() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 72" role="img" aria-label="ChapelCloud lockup">
  <title>ChapelCloud horizontal lockup</title>
  <desc>Mark on the left, ChapelCloud wordmark on the right, vertically centered.</desc>
{defs()}
  <g id="mark" transform="translate(0 2) scale(0.68)">
{crest_colored()}
  </g>
  {wordmark(90, 47, size=38)}
</svg>
"""


def lockup_v() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 170" role="img" aria-label="ChapelCloud stacked lockup">
  <title>ChapelCloud stacked lockup</title>
  <desc>Mark centered above the ChapelCloud wordmark.</desc>
{defs()}
  <g id="mark" transform="translate(60 2)">
{crest_colored()}
  </g>
  {wordmark(110, 150, size=26, anchor="middle")}
</svg>
"""


def favicon() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" role="img" aria-label="ChapelCloud favicon">
  <title>ChapelCloud favicon</title>
{defs()}
  <rect id="field" width="32" height="32" rx="7" fill="{PRESENCE}"/>
  <g id="mark" transform="translate(16 16.3) scale(0.255) translate(-50 -45.5)">
{crest_colored()}
  </g>
</svg>
"""


def main() -> None:
    files = {
        "mark.svg": mark_field(PRESENCE, "ChapelCloud mark"),
        "mark-light.svg": mark_field(CLOUD, "ChapelCloud mark (light)"),
        "mark-alone.svg": mark_alone(),
        "mark-mono.svg": mark_mono(INK, None, "ChapelCloud mark (1-color)"),
        "mark-reversed.svg": mark_mono(WHITE, PRESENCE_DEEP, "ChapelCloud mark (reversed)"),
        "lockup.svg": lockup_h(),
        "lockup-stacked.svg": lockup_v(),
        "wordmark.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 64" role="img" aria-label="ChapelCloud wordmark">
  <title>ChapelCloud wordmark</title>
  {wordmark(0, 46, size=42)}
</svg>
""",
        "favicon.svg": favicon(),
    }
    for name, content in files.items():
        (OUT / name).write_text(content)
        print("wrote", name)

    EXPORTS.mkdir(exist_ok=True)
    for src, w, dst in [
        ("mark.svg", 512, "mark-512.png"),
        ("mark.svg", 1024, "mark-1024.png"),
        ("mark-alone.svg", 512, "mark-alone-512.png"),
        ("mark-alone.svg", 1024, "mark-alone-1024.png"),
        ("lockup.svg", 1024, "lockup-1024.png"),
        ("lockup-stacked.svg", 1024, "lockup-stacked-1024.png"),
        ("favicon.svg", 32, "favicon-32.png"),
        ("mark.svg", 180, "apple-touch-180.png"),
        ("mark-mono.svg", 512, "mark-mono-512.png"),
        ("mark-reversed.svg", 512, "mark-reversed-512.png"),
        ("mark-light.svg", 512, "mark-light-512.png"),
    ]:
        subprocess.run(
            ["rsvg-convert", "-w", str(w), str(OUT / src), "-o", str(EXPORTS / dst)],
            check=True,
        )
        print("export", dst)


if __name__ == "__main__":
    main()
