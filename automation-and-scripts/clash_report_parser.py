"""
This script aligns with the requirement to: "Perform 3D model coordination and clash detection and resolve design conflicts." It ingests raw clash lists (such as Navisworks XML exports) and groups them by priority so engineering teams can focus on major line interference errors first.
"""
"""
Navisworks XML Clash Report Parser and Optimization Tool.
Filters, sorts, and organizes spatial interference reports to optimize multi-disciplinary coordination reviews.
"""

import xml.etree.ElementTree as ET
import pandas as pd
import os

class ClashReportParser:
    def __init__(self, xml_path):
        self.xml_path = xml_path
        self.clash_list = []

    def parse_clash_data(self):
        if not os.path.exists(self.xml_path):
            raise FileNotFoundError(f"Target file path does not exist: {self.xml_path}")
            
        tree = ET.parse(self.xml_path)
        root = tree.getroot()
        
        # Locate clash result tags within standard Navisworks export namespaces
        for clash in root.iter('clashresult'):
            clash_name = clash.attrib.get('name', 'Unknown-Clash')
            distance = float(clash.attrib.get('distance', 0.0))
            status = clash.attrib.get('clashstatus', 'New')
            
            # Extract names of conflicting design layers/disciplines
            left_item = clash.find('.//clashobject[1]/path')
            right_item = clash.find('.//clashobject[2]/path')
            
            left_path = left_item.text if left_item is not None else "Unknown Layer"
            right_path = right_item.text if right_item is not None else "Unknown Layer"
            
            # Categorize severity based on spatial intrusion distance
            if abs(distance) > 0.05:
                severity = "CRITICAL (Hard Clash)"
            elif abs(distance) > 0.01:
                severity = "MAJOR"
            else:
                severity = "MINOR (Clearance Issue)"

            self.clash_list.append({
                'Clash_ID': clash_name,
                'Interference_Distance': distance,
                'Status': status,
                'Severity': severity,
                'Element_1_Path': left_path,
                'Element_2_Path': right_path
            })

    def get_summary_dataframe(self):
        return pd.DataFrame(self.clash_list)

if __name__ == "__main__":
    # Create sample XML string mimicking Navisworks clash logging structure
    mock_xml = """<?xml version="1.0" encoding="UTF-8"?>
    <clashreport>
        <clashresults>
            <clashresult name="Clash_1" distance="-0.072" clashstatus="New">
                <clashobjects>
                    <clashobject><path>Project_Model.dwg/Piping/Line-100-2101</path></clashobject>
                    <clashobject><path>Project_Model.dwg/Structural/Steel_Beam_B1</path></clashobject>
                </clashobjects>
            </clashresult>
            <clashresult name="Clash_2" distance="-0.005" clashstatus="Active">
                <clashobjects>
                    <clashobject><path>Project_Model.dwg/Piping/Line-102-2101</path></clashobject>
                    <clashobject><path>Project_Model.dwg/Electrical/Cable_Tray_T4</path></clashobject>
                </clashobjects>
            </clashresult>
        </clashresults>
    </clashreport>
    """
    
    mock_filename = "temp_clashes.xml"
    with open(mock_filename, "w") as f:
        f.write(mock_xml.strip())
        
    parser = ClashReportParser(mock_filename)
    parser.parse_clash_data()
    df = parser.get_summary_dataframe()
    
    print("\n--- Processed Multi-Disciplinary Clash Summary Table ---")
    print(df[['Clash_ID', 'Severity', 'Interference_Distance', 'Element_1_Path']])
    
    if os.path.exists(mock_filename):
        os.remove(mock_filename)
      
