# Brand guidelines

Canonical how-to for ChapelCloud. Foundation (scripture & meaning): [`foundation.md`](foundation.md). Voice detail: [`voice.md`](voice.md). Tokens: [`../colors/`](../colors/). Logos: [`../logos/`](../logos/).

---

## Positioning

**One line:** Technology care for churches — covering, clear, calm.

**Longer:** ChapelCloud is a family-owned, Christian-operated company that helps ministries steward hosting, giving, bookkeeping integrations, and remote IT — so people can focus on the Gospel, not Sunday-morning panic.

We are fully Christian in ethics and excellence; public surfaces stay welcoming. A non-believer should feel respected, not recruited into a cult aesthetic.

---

## Name & lockups

| Correct | Incorrect |
|---------|-----------|
| ChapelCloud | Chapel Cloud, Chapelcloud, chapelcloud (in prose) |
| chapel.cloud | chapelcloud.com (unless redirecting) |

- **Wordmark:** “ChapelCloud” as one word; both C’s capital.
- **Hero rule:** On branded pages, **ChapelCloud** is the hero-level brand signal. No headline should overpower the name. Do not clutter the first viewport with stats, service grids, or verse stickers.

---

## Voice (summary)

Mission-first, clear, calm. Prefer plain language (“remote technology care”) over jargon (“MSP”) in headlines. Honesty about year-1 limits (remote-first, no travel reno). Full guide: [`voice.md`](voice.md).

---

## Visual idea

**Covering presence.** Soft cloud light over a simple sanctuary arch — guidance without spectacle. Real ministry atmosphere (chapel interiors, sky, quiet rooms) over abstract gradients. Accent light (witness amber) is the *pillar of fire* note: sparse, purposeful, never neon glow spam.

Avoid: purple SaaS gradients, cream + terracotta “AI church” looks, broadsheet newspaper layouts, emoji, multi-layer glow shadows, rounded-full pill clusters.

---

## Color

| Token | Hex | Role |
|-------|-----|------|
| `ink` | `#121820` | Primary text |
| `inkMuted` | `#5c6672` | Secondary text |
| `cloud` | `#f3f5f7` | Page / light surface (covering) |
| `mist` | `#e6eaef` | Soft panels, subtle bands |
| `stone` | `#b4bec9` | Borders, rules |
| `presence` | `#2a4054` | Brand primary (dusk cloud / sanctuary slate) |
| `presenceDeep` | `#1a2b3a` | Hover / deep brand |
| `covering` | `#7a94a8` | Mid cloud, icons, secondary UI |
| `witness` | `#b8923f` | Accent only — light / CTA emphasis |
| `witnessSoft` | `#e8d4a8` | Soft highlight washes |

Full definitions: [`../colors/tokens.json`](../colors/tokens.json) · [`../colors/tokens.css`](../colors/tokens.css).

**Usage:** Large fields use `cloud` / `mist` / `presence`. `witness` is salt, not the meal — CTAs, focus rings, small marks of light. Never default the whole UI to amber.

---

## Typography

| Role | Family | Use |
|------|--------|-----|
| Display | **Newsreader** | Brand wordmark treatment, headlines |
| Sans | **Source Sans 3** | Body, UI, docs |

Newsreader carries quiet editorial gravity (bulletin / reading room). Source Sans 3 stays clear for technical honesty. Load from Google Fonts or self-host per [`../fonts/`](../fonts/).

**Scale (suggested):** Display 2.5–3.5rem / body 1–1.125rem / tracking normal; avoid ultra-tight tech display tracking.

---

## Logo

Geometric crest: interlocking covering plates + central witness star. See [`../logos/README.md`](../logos/README.md).

| File | Use |
|------|-----|
| `mark.svg` / `mark-light.svg` | Field marks (avatars, app icon seed) |
| `mark-alone.svg` | Crest only (transparent) |
| `mark-mono.svg` / `mark-reversed.svg` | 1-color ink / white on deep |
| `wordmark.svg` | Name alone (Newsreader) |
| `lockup.svg` / `lockup-stacked.svg` | Horizontal / stacked |
| `favicon.svg` | 32-friendly mark |

**Clear space:** ≥ width of the central star on all sides.  
**Minimum:** mark ≥ 24px; lockup ≥ 120px wide.  
**Don’t:** stretch, rotate, add drop shadows / glow, place on busy photos without a `cloud`/`presence` scrim, recolor outside token set.

On dark: `mark-reversed.svg` or white wordmark. On light: full-color or `mark-mono.svg`.

---

## Imagery

Prefer: soft sky, stone and wood interiors, cable-tidy booths, people serving (hands, not stock “praying stock photo” clichés).  
Avoid: neon servers, purple fog, cartoon angels, oversized cross watermarks on product UI.

---

## Offers language (business plan)

| Offer | Public wording |
|-------|----------------|
| SaaS | Hosting, giving, live stream/restream, video archive, podcasts, transcripts, bookkeeping, integrations |
| MSP | Remote technology care / Care |
| Hardware | Campus display management & e-paper (later — be honest) |

Flywheel tone: invitation and stewardship, never pressure.

---

## Related

- Business plan: `company/plans/business-plan.md`
- Christian operating principles: `company/decisions/0002-christian-operating-principles.md`
- MSP site brief: `company/plans/home-site-msp-brief.md`
