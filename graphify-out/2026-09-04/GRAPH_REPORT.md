# Graph Report - DepthWizard  (2026-09-04)

## Corpus Check
- 39 files · ~90,196 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 319 nodes · 484 edges · 26 communities (14 shown, 3 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- db.py
- build_presets.py
- dependencies
- devDependencies
- DepthWizard — Product Requirements Document
- calibrate
- reconstruct.py
- level_water_body
- _OnnxSession
- export_geotiff
- smoke_test.py
- main.py
- App.jsx
- React + Vite
- AGENTS.md
- rules/graphify.md
- workflows/graphify.md

## God Nodes (most connected - your core abstractions)
1. `DepthWizard — Product Requirements Document` - 17 edges
2. `reconstruct()` - 15 edges
3. `calibrate()` - 12 edges
4. `get_connection()` - 11 edges
5. `level_water_body()` - 11 edges
6. `build_preset()` - 11 edges
7. `get_preset()` - 10 edges
8. `infer_depth()` - 9 edges
9. `get_gcps()` - 8 edges
10. `export_glb_route()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `main()` --calls--> `ensure_data_dirs()`  [EXTRACTED]
  DepthWizard_B/scripts/build_presets.py → DepthWizard_B/backend/app/core/config.py
- `lifespan()` --calls--> `init_db()`  [EXTRACTED]
  DepthWizard_B/backend/app/main.py → DepthWizard_B/backend/app/models/db.py
- `lifespan()` --calls--> `initialise()`  [EXTRACTED]
  DepthWizard_B/backend/app/main.py → DepthWizard_B/backend/app/services/inference.py
- `build_preset()` --calls--> `get_connection()`  [EXTRACTED]
  DepthWizard_B/scripts/build_presets.py → DepthWizard_B/backend/app/models/db.py
- `main()` --calls--> `init_db()`  [EXTRACTED]
  DepthWizard_B/scripts/build_presets.py → DepthWizard_B/backend/app/models/db.py

## Import Cycles
- None detected.

## Communities (26 total, 3 thin omitted)

### Community 0 - "db.py"
Cohesion: 0.11
Nodes (29): _db_path(), get_connection(), get_gcps(), get_preset(), init_db(), insert_elevation_profile(), list_presets(), Connection (+21 more)

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

### Community 5 - "calibrate"
Cohesion: 0.20
Nodes (18): calibrate(), CalibrationResult, GCPAnchor, _ols_affine(), _pearson_r(), ndarray, _ransac_affine(), backend/app/services/calibrator.py ──────────────────────────────────── Robust… (+10 more)

### Community 6 - "reconstruct.py"
Cohesion: 0.08
Nodes (39): insert_reconstruction(), Insert a new reconstruction log row., _decode_raw_height_matrix(), _downsample(), _encode_height_matrix(), export_geotiff_route(), export_glb_route(), _gcps_from_rows() (+31 more)

### Community 7 - "level_water_body"
Cohesion: 0.21
Nodes (16): _apply_luminance_gate(), _clamp_water_regions(), _clean_mask(), _compute_luminance(), _compute_vwi(), level_water_body(), _otsu_water_mask(), ndarray (+8 more)

### Community 8 - "_OnnxSession"
Cohesion: 0.20
Nodes (7): initialise(), _OnnxSession, Path, Forward pass — input must be float32 NCHW (1,3,518,518)., Load the ONNX model (or enter dummy mode). Should be called once at application…, Lazy-loaded, process-level ONNX Runtime session., Attempt to load the ONNX model once. Sets _dummy_mode=True if the file is…

### Community 9 - "export_geotiff"
Cohesion: 0.25
Nodes (10): _build_mesh_geometry(), export_geotiff(), export_glb(), Any, ndarray, Path, backend/app/services/export.py ─────────────────────────────── Export helpers…, Build vertices, faces, and UV coordinates for a height-field mesh. The mesh is… (+2 more)

### Community 10 - "smoke_test.py"
Cohesion: 0.29
Nodes (9): assert_height_matrix(), check(), _make_dummy_png(), scripts/smoke_test.py ────────────────────── End-to-end smoke test. Uses…, Start uvicorn in a subprocess and wait until it is ready., Decode and validate the base64 height matrix., run_tests(), _start_server() (+1 more)

### Community 11 - "main.py"
Cohesion: 0.13
Nodes (12): ensure_data_dirs(), _env_path(), Path, backend/app/core/config.py ────────────────────────── Centralised settings for…, Create all required runtime data directories (idempotent)., Immutable runtime settings loaded once at import time. Import the singleton:…, Settings, create_app() (+4 more)

### Community 12 - "App.jsx"
Cohesion: 0.11
Nodes (19): App(), initPresets(), Canvas3D(), ElevationRuler(), extractElevationIntersection(), FlythroughController(), SPLINE_WAYPOINTS, HYPSO_STOPS (+11 more)

### Community 13 - "React + Vite"
Cohesion: 0.50
Nodes (3): Expanding the ESLint configuration, React Compiler, React + Vite

## Knowledge Gaps
- **57 isolated node(s):** `name`, `private`, `version`, `type`, `dev` (+52 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 160 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `level_water_body()` connect `level_water_body` to `reconstruct.py`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Why does `calibrate()` connect `calibrate` to `reconstruct.py`?**
  _High betweenness centrality (0.027) - this node is a cross-community bridge._
- **Why does `reconstruct()` connect `reconstruct.py` to `db.py`, `calibrate`, `level_water_body`?**
  _High betweenness centrality (0.023) - this node is a cross-community bridge._
- **What connects `name`, `private`, `version` to the rest of the system?**
  _57 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `db.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10967741935483871 - nodes in this community are weakly interconnected._
- **Should `build_presets.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1268939393939394 - nodes in this community are weakly interconnected._
- **Should `dependencies` be split into smaller, more focused modules?**
  _Cohesion score 0.06896551724137931 - nodes in this community are weakly interconnected._