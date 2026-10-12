"""
This script solves a primary responsibility listed in the job post: "Generate BOMs (Bills of Materials), piping schedules, and other project deliverables." It extracts raw component data from universal Piping Component Files (.pcf) and compiles a formatted engineering list.
"""

#

"""
Piping Component File (PCF) Bill of Materials (BOM) Generator.
Extracts component data, materials, and lengths from PCF files to generate a structured engineering BOM.
"""

import os
import re
import pandas as pd

class PCFBomGenerator:
    def __init__(self, pcf_path):
        self.pcf_path = pcf_path
        self.components = []

    def parse_pcf(self):
        if not os.path.exists(self.pcf_path):
            raise FileNotFoundError(f"Target PCF file not found: {self.pcf_path}")
        
        current_component = {}
        
        with open(self.pcf_path, 'r') as file:
            for line in file:
                line = line.strip()
                
                # Identify component start blocks
                if line in ['PIPE', 'ELBOW', 'TEE', 'FLANGE', 'VALVE', 'GASKET', 'BOLT']:
                    if current_component:
                        self.components.append(current_component)
                    current_component = {'TYPE': line, 'SIZE': '', 'SPEC': '', 'ITEM-CODE': '', 'DESCRIPTION': '', 'QTY-LENGTH': 1}
                    continue
                
                # Parse attributes using standard PCF keywords
                if line.startswith('END-POINT'):
                    # Capture size data if available
                    parts = line.split()
                    if len(parts) >= 5 and not current_component['SIZE']:
                        current_component['SIZE'] = parts[4]
                elif line.startswith('ITEM-CODE'):
                    current_component['ITEM-CODE'] = line.replace('ITEM-CODE', '').strip()
                elif line.startswith('DESCRIPTION'):
                    current_component['DESCRIPTION'] = line.replace('DESCRIPTION', '').strip()
                elif line.startswith('PIPING-SPEC'):
                    current_component['SPEC'] = line.replace('PIPING-SPEC', '').strip()
                elif line.startswith('LENGTH'):
                    try:
                        # For pipes, capture actual physical length
                        length_val = float(line.split()[1])
                        current_component['QTY-LENGTH'] = length_val
                    except (IndexError, ValueError):
                        pass

            # Append the trailing component block
            if current_component:
                self.components.append(current_component)

    def export_to_csv(self, output_path):
        if not self.components:
            return "No valid component blocks discovered in the target PCF profile."
        
        df = pd.DataFrame(self.components)
        
        # Group identical materials/components together and sum lengths or counts
        summary_bom = df.groupby(['TYPE', 'SIZE', 'SPEC', 'ITEM-CODE', 'DESCRIPTION']).sum().reset_index()
        summary_bom.to_csv(output_path, index=False)
        return f"Successfully generated technical summary BOM at: {output_path}"

if __name__ == "__main__":
    # Creates a mock PCF configuration to verify parsing automation logic
    mock_pcf_content = """
    PIPING-SPEC CS300
    PIPE
        END-POINT 0.0 0.0 0.0 4
        END-POINT 1200.0 0.0 0.0 4
        ITEM-CODE P-CS-004
        DESCRIPTION PIPE, ASME B36.10, SEAMLESS, SCH 40, ASTM A106 GR B
        LENGTH 1200.0
    ELBOW
        END-POINT 1200.0 0.0 0.0 4
        END-POINT 1200.0 300.0 0.0 4
        ITEM-CODE E-CS-004
        DESCRIPTION ELBOW, 90 DEG LONG RADIUS, BW, ASME B16.9, SCH 40, ASTM A234 GR WPB
    FLANGE
        END-POINT 1200.0 300.0 0.0 4
        ITEM-CODE F-CS-004
        DESCRIPTION FLANGE, WELD NECK, ASME B16.5, CLASS 300, RF, ASTM A105
    """
    
    mock_filename = "Line-100-2101-CS300.pcf"
    with open(mock_filename, "w") as f:
        f.write(mock_pcf_content.strip())
        
    generator = PCFBomGenerator(mock_filename)
    generator.parse_pcf()
    print(generator.export_to_csv("BOM_Output_Report.csv"))
    
    # Clean up mock file after execution
    if os.path.exists(mock_filename):
        os.remove(mock_filename)
      
