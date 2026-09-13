"""
backend/app/routers/presets.py
────────────────────────────────
GET /api/v1/presets          — list all available presets
GET /api/v1/presets/{id}     — single preset detail with GCP counts
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.models.db import get_gcps, get_preset, list_presets

log = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1", tags=["presets"])


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _row_to_dict(row: Any) -> dict:
    """Convert sqlite3.Row to a plain dict."""
    return dict(row)


def _enrich_preset(row: Any) -> dict:
    """
    Add derived / frontend-friendly fields to a raw preset row.

      • bbox_parsed  — parsed list [min_lon, min_lat, max_lon, max_lat]
      • has_dem      — whether a reference DEM file is present on disk
      • thumbnail_url — URL for the static optical tile (served by main.py)
      • gcp_counts   — { train: N, holdout: N }
    """
    d = _row_to_dict(row)

    # Parse bbox JSON string → list
    try:
        d["bbox_parsed"] = json.loads(d["bbox"])
    except (TypeError, json.JSONDecodeError):
        d["bbox_parsed"] = None

    # Check DEM presence
    dem_path = d.get("dem_path")
    d["has_dem"] = bool(dem_path and Path(dem_path).exists())

    # Build thumbnail URL (static files mounted at /static/presets/<id>/optical.png)
    d["thumbnail_url"] = f"/static/presets/{d['id']}/optical.png"

    # GCP counts (train / holdout)
    all_gcps = get_gcps(d["id"])
    d["gcp_counts"] = {
        "train":   sum(1 for g in all_gcps if g["split"] == "train"),
        "holdout": sum(1 for g in all_gcps if g["split"] == "holdout"),
        "total":   len(all_gcps),
    }

    return d


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@router.get("/presets", summary="List all available presets")
def list_all_presets() -> JSONResponse:
    """
    Return metadata for all bundled preset regions.

    Response fields (per preset):
    - id, name, bbox_parsed, gsd, thumbnail_url, has_dem, gcp_counts
    """
    rows = list_presets()
    presets = [_enrich_preset(r) for r in rows]
    return JSONResponse(content={"presets": presets, "count": len(presets)})


@router.get("/presets/{preset_id}", summary="Single preset detail")
def get_preset_detail(preset_id: str) -> JSONResponse:
    """
    Return detailed metadata for a single preset, including GCP split counts
    and whether a reference DEM is available for tactical (calibrated) mode.
    """
    row = get_preset(preset_id)
    if row is None:
        raise HTTPException(status_code=404, detail=f"Preset '{preset_id}' not found.")

    return JSONResponse(content=_enrich_preset(row))
