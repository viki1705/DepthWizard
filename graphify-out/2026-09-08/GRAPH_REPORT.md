# Graph Report - DepthWizard  (2026-09-07)

## Corpus Check
- 69 files · ~1,174,627 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 423 nodes · 624 edges · 33 communities (20 shown, 3 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 7 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- calibrate
- build_presets.py
- dependencies
- devDependencies
- DepthWizard — Product Requirements Document
- inference.py
- reconstruct.py
- level_water_body
- DepthWizard — Frontend Controls & Judge Demonstration Guide
- backend/generate_scientific_presets.py
- smoke_test.py
- config.py
- App.jsx
- React + Vite
- Canvas3D.jsx
- AGENTS.md
- rules/graphify.md
- workflows/graphify.md
- DepthWizard_B/backend/generate_scientific_presets.py
- export_glb
- backend/ingest_accurate_presets.py
- download_real_presets.py
- DepthWizard_B/backend/ingest_accurate_presets.py

## God Nodes (most connected - your core abstractions)
1. `reconstruct()` - 17 edges
2. `DepthWizard — Product Requirements Document` - 17 edges
3. `DepthWizard — Frontend Controls & Judge Demonstration Guide` - 16 edges
4. `infer_depth()` - 13 edges
5. `calibrate()` - 12 edges
6. `get_connection()` - 11 edges
7. `level_water_body()` - 11 edges
8. `build_preset()` - 11 edges
9. `get_preset()` - 10 edges
10. `get_gcps()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `main()` --calls--> `ensure_data_dirs()`  [EXTRACTED]
  DepthWizard_B/scripts/build_presets.py → DepthWizard_B/backend/app/core/config.py
- `lifespan()` --calls--> `initialise()`  [EXTRACTED]
  DepthWizard_B/backend/app/main.py → DepthWizard_B/backend/app/services/inference.py
- `build_preset()` --calls--> `get_connection()`  [EXTRACTED]
  DepthWizard_B/scripts/build_presets.py → DepthWizard_B/backend/app/models/db.py
- `main()` --calls--> `init_db()`  [EXTRACTED]
  DepthWizard_B/scripts/build_presets.py → DepthWizard_B/backend/app/models/db.py
- `_gcps_from_rows()` --calls--> `GCPAnchor`  [EXTRACTED]
  DepthWizard_B/backend/app/routers/reconstruct.py → DepthWizard_B/backend/app/services/calibrator.py

## Import Cycles
- None detected.

## Communities (33 total, 3 thin omitted)

### Community 0 - "calibrate"
Cohesion: 0.20
Nodes (18): calibrate(), CalibrationResult, GCPAnchor, _ols_affine(), _pearson_r(), ndarray, _ransac_affine(), backend/app/services/calibrator.py ──────────────────────────────────── Robust… (+10 more)

### Community 1 - "build_presets.py"
Cohesion: 0.13
Nodes (32): build_preset(), _dem_to_optical_floodplain(), _dem_to_optical_mountain(), _dem_to_optical_urban(), _extract_gcps(), _generate_dem(), _generate_floodplain_dem(), _generate_mountain_dem() (+24 more)

### Community 2 - "dependencies"
Cohesion: 0.07
Nodes (28): clsx, dependencies, clsx, lucide-react, react, react-dom, @react-three/drei, @react-three/fiber (+20 more)

### Community 3 - "devDependencies"
Cohesion: 0.08
Nodes (25): autoprefixer, devDependencies, autoprefixer, eslint, @eslint/js, eslint-plugin-react-hooks, eslint-plugin-react-refresh, globals (+17 more)

### Community 4 - "DepthWizard — Product Requirements Document"
Cohesion: 0.08
Nodes (23): 10. AI Pipeline, 11. UI Principles, 12. Folder Structure, 13. Environment Variables, 14. Non-Functional Requirements, 15. Future Scope (Out of Scope for Hackathon), 16. Final Product Flow, 1. Vision (+15 more)

### Community 5 - "inference.py"
Cohesion: 0.10
Nodes (28): dummy_mode(), _edge_snap(), infer_depth(), initialise(), _OnnxSession, _percentile_stretch(), _preprocess(), ndarray (+20 more)

### Community 6 - "reconstruct.py"
Cohesion: 0.05
Nodes (63): ensure_data_dirs(), Create all required runtime data directories (idempotent)., create_app(), lifespan(), backend/app/main.py ──────────────────── FastAPI application entry point for…, Application lifespan handler. Startup sequence: 1. Create data directories…, _db_path(), get_connection() (+55 more)

### Community 7 - "level_water_body"
Cohesion: 0.21
Nodes (16): _apply_luminance_gate(), _clamp_water_regions(), _clean_mask(), _compute_luminance(), _compute_vwi(), level_water_body(), _otsu_water_mask(), ndarray (+8 more)

### Community 8 - "DepthWizard — Frontend Controls & Judge Demonstration Guide"
Cohesion: 0.05
Nodes (42): 10. Top-Right: Tactical Validation HUD, 11. Bottom Drawer: Elevation Cross-Section Profile, 12. Top-Left: Recon Drone Telemetry Badge, 13. Winning Demo Script (Step-by-Step for Judges), 14. Judge Q&A Defense & Common Trap Questions, 1. Core Pitch & System Concept, 2. Quick Reference Cheat Sheet, 3. Left Sidebar: Target Region & Presets (+34 more)

### Community 9 - "backend/generate_scientific_presets.py"
Cohesion: 0.31
Nodes (10): generate_assam(), generate_hyderabad(), generate_leh(), make_grid(), Brahmaputra floodplain: Wide flat braidplain, river channel, sandbars., Synchronize GCP ground-truth elevations in depthwizard.db if present., Alpine high-relief terrain with dendritic ridgelines and U-valleys., Deccan plateau: Flat structural tableland with isolated granite hills and urban… (+2 more)

### Community 10 - "smoke_test.py"
Cohesion: 0.29
Nodes (9): assert_height_matrix(), check(), _make_dummy_png(), scripts/smoke_test.py ────────────────────── End-to-end smoke test. Uses…, Start uvicorn in a subprocess and wait until it is ready., Decode and validate the base64 height matrix., run_tests(), _start_server() (+1 more)

### Community 11 - "config.py"
Cohesion: 0.22
Nodes (5): _env_path(), Path, backend/app/core/config.py ────────────────────────── Centralised settings for…, Immutable runtime settings loaded once at import time. Import the singleton:…, Settings

### Community 12 - "App.jsx"
Cohesion: 0.15
Nodes (15): App(), initPresets(), DiagnosticDrawer(), MAGMA_STOPS, paintDepthToCanvas(), sampleMagma(), TopoCrossSection(), ValidationHUD() (+7 more)

### Community 13 - "React + Vite"
Cohesion: 0.50
Nodes (3): Expanding the ESLint configuration, React Compiler, React + Vite

### Community 14 - "Canvas3D.jsx"
Cohesion: 0.21
Nodes (8): Canvas3D(), ElevationRuler(), extractElevationIntersection(), FlythroughController(), SPLINE_WAYPOINTS, HYPSO_STOPS, sampleHypsoGradient(), TerrainMesh()

### Community 19 - "DepthWizard_B/backend/generate_scientific_presets.py"
Cohesion: 0.31
Nodes (10): generate_assam(), generate_hyderabad(), generate_leh(), make_grid(), Brahmaputra floodplain: Wide flat braidplain, river channel, sandbars., Synchronize GCP ground-truth elevations in depthwizard.db if present., Alpine high-relief terrain with dendritic ridgelines and U-valleys., Deccan plateau: Flat structural tableland with isolated granite hills and urban… (+2 more)

### Community 29 - "export_glb"
Cohesion: 0.27
Nodes (10): _build_mesh_geometry(), export_geotiff(), export_glb(), Any, ndarray, Path, backend/app/services/export.py ─────────────────────────────── Export helpers…, Build vertices, faces, and UV coordinates for a height-field mesh. The mesh is… (+2 more)

### Community 30 - "backend/ingest_accurate_presets.py"
Cohesion: 0.48
Nodes (6): deg2num(), fetch_highres_tile(), get_http_session(), Synchronize GCP ground-truth elevations in depthwizard.db if present., run(), update_db_gcps()

### Community 31 - "download_real_presets.py"
Cohesion: 0.47
Nodes (5): clean_stale_precomputed_arrays(), fetch_satellite_image(), main(), Fetch genuine satellite imagery from the public ESRI World Imagery MapServer.…, Remove stale precomputed depth and height matrices so that the backend…

### Community 32 - "DepthWizard_B/backend/ingest_accurate_presets.py"
Cohesion: 0.48
Nodes (6): deg2num(), fetch_highres_tile(), get_http_session(), Synchronize GCP ground-truth elevations in depthwizard.db if present., run(), update_db_gcps()

## Knowledge Gaps
- **89 isolated node(s):** `name`, `private`, `version`, `type`, `dev` (+84 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 213 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `infer_depth()` connect `inference.py` to `DepthWizard_B/backend/ingest_accurate_presets.py`, `reconstruct.py`?**
  _High betweenness centrality (0.023) - this node is a cross-community bridge._
- **Why does `level_water_body()` connect `level_water_body` to `reconstruct.py`?**
  _High betweenness centrality (0.019) - this node is a cross-community bridge._
- **Why does `reconstruct()` connect `reconstruct.py` to `calibrate`, `inference.py`, `level_water_body`?**
  _High betweenness centrality (0.018) - this node is a cross-community bridge._
- **What connects `name`, `private`, `version` to the rest of the system?**
  _89 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `build_presets.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1268939393939394 - nodes in this community are weakly interconnected._
- **Should `dependencies` be split into smaller, more focused modules?**
  _Cohesion score 0.06896551724137931 - nodes in this community are weakly interconnected._
- **Should `devDependencies` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._