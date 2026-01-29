import pandas as pd
import os

def convert_epw_to_csv(input_file):
    # EPW files have 8 lines of metadata/header information
    # The actual data starts on line 9
    try:
        # Read the file, skipping the first 8 rows of metadata
        data = pd.read_csv(input_file, skiprows=8, header=None)
        
        # Standard EPW Column Names (per EnergyPlus documentation)
        columns = [
            "Year", "Month", "Day", "Hour", "Minute", "Data Source and Uncertainty Flags",
            "Dry Bulb Temperature", "Dew Point Temperature", "Relative Humidity", 
            "Atmospheric Station Pressure", "Extraterrestrial Solar Radiation", 
            "Extraterrestrial Direct Normal Radiation", "Horizontal Infrared Radiation from Sky",
            "Global Horizontal Radiation", "Direct Normal Radiation", "Diffuse Horizontal Radiation",
            "Global Horizontal Illuminance", "Direct Normal Illuminance", "Diffuse Horizontal Illuminance",
            "Zenith Luminance", "Wind Direction", "Wind Speed", "Total Sky Cover", 
            "Opaque Sky Cover", "Visibility", "Ceiling Height", "Present Weather Observation",
            "Present Weather Codes", "Precipitable Water", "Aerosol Optical Depth", 
            "Snow Depth", "Days Since Last Snowfall", "Albedo", "Liquid Precipitation Quantity",
            "Liquid Precipitation Depth"
        ]
        
        # Assign columns (handling cases where files might have fewer/extra columns)
        data.columns = columns[:len(data.columns)]
        
        # Define output filename
        output_file = os.path.splitext(input_file)[0] + ".csv"
        
        # Save to CSV
        data.to_csv(output_file, index=False)
        print(f"Successfully converted: {output_file}")

    except Exception as e:
        print(f"Error processing {input_file}: {e}")

# Usage
file_path = "merged-Dubai_Intl_Airp_2015-2025.epw"  # Replace with your filename
convert_epw_to_csv(file_path)