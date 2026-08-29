# Logos

Master SVG marks for ChapelCloud.

**Concept:** soft geometric crest (protective covering) built from interlocking curved plates, with a central four-pointed gold star as quiet witness. Durable, architectural, timeless — no fluffy clouds, SaaS gradients, or literal religious icons.

| File | Contents |
|------|----------|
| [`mark.svg`](mark.svg) | Full-color crest on `presence` field (avatars / dark-ready) |
| [`mark-light.svg`](mark-light.svg) | Full-color crest on `cloud` field (light UI) |
| [`mark-alone.svg`](mark-alone.svg) | Crest only, transparent background |
| [`mark-mono.svg`](mark-mono.svg) | 1-color solid ink `#121820` (negative-space panels) |
| [`mark-reversed.svg`](mark-reversed.svg) | Solid white on `presenceDeep` field |
| [`wordmark.svg`](wordmark.svg) | “ChapelCloud” in Newsreader (live text, weight 600) |
| [`lockup.svg`](lockup.svg) | Horizontal — mark left, wordmark right |
| [`lockup-stacked.svg`](lockup-stacked.svg) | Stacked — mark above wordmark |
| [`favicon.svg`](favicon.svg) | 32×32-friendly field mark |
| [`_generate_mark.py`](_generate_mark.py) | Regenerates SVG masters + PNG exports |

## Anatomy

1. **Shield / mantle** — flat top, sides sweep to a soft blunted tip.
2. **Interlocking plates** — `presence` / `presenceDeep` / `covering` panels weave over and under.
3. **Witness star** — `witness` gold, only on the central four-pointed star.
4. **Negative space** — uniform `#f3f5f7` gaps between plates (legible at 24px).

## Clear space & size

- Clear space ≥ **width of the central star** on all sides of the lockup.
- Mark minimum 24px; lockup minimum ~120px wide.
- Prefer SVG; rasterize to PNG only when a platform requires it (`../exports/`).

## Color rules

| Role | Token | Hex |
|------|-------|-----|
| Outer / primary panels | `presence` | `#2a4054` |
| Deep anchor panels | `presenceDeep` | `#1a2b3a` |
| Mid interlocking panels | `covering` | `#7a94a8` |
| Central star only | `witness` | `#b8923f` |
| Gaps / light field | `cloud` | `#f3f5f7` |
| 1-color ink | `ink` | `#121820` |

No gradients, glows, or drop shadows.

## Don’t

- Stretch, rotate, or add effects.
- Recolor the witness star to neon or purple.
- Separate the star from the crest as a “new logo.”
- Place the mark on busy photography without a `cloud` or `presence` scrim.

## Regeneration

```bash
nix-shell -p python3 librsvg --run 'python3 brand/logos/_generate_mark.py'
```

Live-text lockups use Newsreader via `font-family`. For outlined (paths) masters, convert text after installing the font (e.g. fonttools / Illustrator).
