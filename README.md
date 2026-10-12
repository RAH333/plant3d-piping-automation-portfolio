![]()
# Plant 3D Piping Design & Automation Portfolio

Professional portfolio showcasing production engineering workflows, automated design data processes, custom specifications management, and multi-disciplinary model coordination strategies for complex industrial plant environments.

## Software & Technical Competencies
* **3D Plant Modeling & Detail Design:** AutoCAD Plant 3D, Autodesk Revit, Navisworks Manage.
* **Engineering Standards & Piping Codes:** ASME B31.3 (Process Piping), ASME B16.5 (Flanges), ASME B16.9 (BW Fittings), API 600 (Valves).
* **Deliverables Production:** Piping Isometrics (ISO generation config), Pipe Spool Maps, Custom Bills of Materials (BOM), General Arrangements (GAs).
* **BIM & Automation Integration:** Python automation scripts parsing PCF engineering formats, custom SQLite spec/catalog modification, and multi-discipline clash remediation.

---

## Key Projects & Portfolio Highlights

### 1. High-Pressure Process Specification Control (ASME B31.3 Compliance)
* **Directory Reference:** `/specs-and-catalogs/`
* Built customized piping specification templates (`.pspc`) utilizing structural components adhering strictly to Class 300 pressure structures.
* Implemented parameter matching rule-sets within `components_config.json` to systematically map vendor catalogs to Plant 3D routing specs.

### 2. PCF Data Parsing & Automatic BOM Extraction
* **Directory Reference:** `/automation-and-scripts/bom_generator.py`
* Developed an engineering script executing data parsing against standard Piping Component Files (`.pcf`). 
* Aggregates length metrics, material types, and specific wall schedule variables from nested code lines to output instant procurement lists, bypassing native generation bottlenecks.

### 3. Spatial Conflict Optimization & Clash Auditing
* **Directory Reference:** `/automation-and-scripts/clash_report_parser.py`
* Engineered a pipeline system converting verbose XML output documents from Navisworks into manageable, prioritized data matrices. 
* Automatically isolates critical piping-to-structural interferences, speeding up resolution timelines during interdisciplinary design reviews.

---

## Professional Deliverables Architecture
Sample structural design artifacts are managed inside the `/coordination-and-bim/standard-drawings/` layout directory:
* **Process-Isometric.pdf:** Detailed piping layout detailing automated dimensional tagging, precise coordinate lists, orientation annotations, and weld map allocation blocks.
* **Sample-Spool-Drawing.pdf:** Prefabrication routing document displaying component fabrication breakdowns, shop weld specifications, and precise cut lengths.




# plant3d-piping-automation-portfolio
AutoCAD Plant 3D workflows, custom catalogs/specs, script-based modeling automation, clash resolution, and multidisciplinary coordination.  underlying engineering data structures, Python scripts for component automation, custom specifications, and structured documentation.

```
plant3d-piping-automation-portfolio/
│
├── .github/
│   └── workflows/
│       └── validate-specs.yml       # CI/CD action to validate JSON spec formatting
│
├── specs-and-catalogs/
│   ├── ASME-B16.5-Flanges.pcat      # Placeholder binary custom catalog file
│   ├── CS300-Process-Spec.pspc      # Custom 300# Carbon Steel specification file
│   └── scripts/
│       ├── generate_spec_json.py    # Python script parsing catalog data into JSON schemas
│       └── components_config.json   # Parameter mappings for custom valves and inline fittings
│
├── automation-and-scripts/
│   ├── bom_generator.py             # Automates structured Excel BOM creation from PCF exports
│   ├── clash_report_parser.py      # Parses Navisworks XML/CSV clash reports to sort by priority
│   └── pid_tag_validator.py         # Validates P&ID data tags against 3D model databases
│
├── coordination-and-bim/
│   ├── nwd-coordination-matrix.md   # Clash matrix layout and multi-disciplinary workflow rules
│   ├── standard-drawings/
│   │   ├── Sample-Spool-Drawing.pdf # Exported production-ready piping spool drawing
│   │   └── Process-Isometric.pdf    # Sample ISO sheet showing BOM, cut-piece lists, and weld maps
│   └── test-pcfs/
│       └── Line-100-2101-CS300.pcf  # Sample Piping Component File (PCF) for stress/ISO validation
│
├── data/
│   ├── sample_clash_report.xml      # Mock clash detection export from Navisworks
│   └── mock_model_data.db           # SQLite database simulating a Plant 3D project data backend
│
├── .gitignore
├── LICENSE
└── README.md                        # Master documentation showcasing your design expertise
```
