# Tools Layer  
Operational instruments used by the system for creation, execution, automation and visualization.  
This layer does not contain decision logic — only tools that execute tasks.

---

## 1. Visualization & Design Tools
- AutoCAD — scheme generation, automation scripts, DWG processing.  
- Visio — diagrams, block-schemes, cross-functional process visualization.  
- Draw.io / Excalidraw — lightweight diagramming tools.

---

## 2. Automation Tools
- n8n actions (execution level only).  
- Python scripts for AutoCAD, CAD operations, batch processing.  
- Power Automate / Office Scripts.  
- GitHub Actions for document building, formatting and PDF export.

---

## 3. Multimodal Tools
- Image generation.  
- Audio transcription / voice processing.  
- Video scene breakdown tools.  
- Sensor data adapters.

These tools provide inputs or outputs but never control decision-making.

---

## 4. Data Tools
- CSV/JSON/YAML processors.  
- Local database adapters (LiteDB, SQLite).  
- Cloud storage connectors.

---

## 5. Boundaries & Safety
- No tool executes autonomous decisions.  
- All actions are triggered through orchestration layer.  
- Execution is sandboxed where possible.  
- Logs stored externally.

---

## Status
Draft. Will be expanded with more detailed tooling integrations and automation pipelines.