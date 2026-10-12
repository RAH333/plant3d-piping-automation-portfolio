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
