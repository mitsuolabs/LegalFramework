import json
import os
from datetime import datetime

def generate_license_files(config_path='project_config.json'):
    """
    Generates all necessary license and EULA files based on a JSON configuration.

    This script reads a configuration file to get project-specific details
    and then populates the MRSL-1.0 and MMPEULA-1.0 templates with this
    information, saving them to the appropriate output files.

    Args:
        config_path (str): The path to the JSON configuration file.
    """
    print(f"--- Starting License Generation ---")

    # --- 1. Load Configuration ---
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        print(f"Successfully loaded configuration from {config_path}")
    except FileNotFoundError:
        print(f"FATAL: Configuration file not found at {config_path}")
        print("Please create a 'project_config.json' file.")
        return
    except json.JSONDecodeError:
        print(f"FATAL: Invalid JSON in {config_path}. Please check the file syntax.")
        return

    placeholders = {
        "[[YEAR]]": str(datetime.now().year),
        "[[LICENSOR_NAME]]": config.get("licensorName", "LICENSOR_NAME_MISSING"),
        "[[ORCID_ID]]": config.get("orcidId", "ORCID_ID_MISSING"),
        "[[DESIGNATED_JURISDICTION]]": config.get("designatedJurisdiction", "JURISDICTION_MISSING"),
        "[[source-license]]": config.get("sourceLicense", "SOURCE_LICENSE_MISSING"),
        "[[product-name]]": config.get("productName", "PRODUCT_NAME_MISSING"),
        "[[licensor-name]]": config.get("licensorName", "LICENSOR_NAME_MISSING"),
        "[[license-fee-schedule]]": config.get("licenseFeeSchedule", "FEE_SCHEDULE_MISSING"),
        "[[project-family-name]]": config.get("projectFamilyName", "PROJECT_FAMILY_NAME_MISSING"),
        "[[source-license-reference]]": config.get("sourceLicenseReference", "SOURCE_LICENSE_REFERENCE_MISSING"),
        "[[licensor-contact-address]]": config.get("licensorContactAddress", "CONTACT_ADDRESS_MISSING"),
        "[[designated-jurissiction]]": config.get("designatedJurisdiction", "JURISDICTION_MISSING"), # Typo in original
        "[[consumer-declaration-address]]": config.get("consumerDeclarationAddress", "CONSUMER_ADDRESS_MISSING"),
    }

    print("\n--- Placeholders Set ---")
    for key, value in placeholders.items():
        print(f'{key} => "{value}"')

    templates = {
        "mrsl-1.0.txt": "mrsl-1.0.txt",
        "mrsl-1.0.html": "mrsl-1.0.html",
        "mmpeula-1.0.txt": "mmpeula-1.0.txt",
        "mmpeula-1.0.html": "mmpeula-1.0.html"
    }

    output_dir = config.get("outputDir", "generated_licenses")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"\nCreated output directory: {output_dir}")

    # --- 2. Process Templates ---
    print("\n--- Processing Templates ---")
    for template_file, output_file_name in templates.items():
        try:
            with open(template_file, 'r', encoding='utf-8') as f:
                content = f.read()
            print(f"Read template: {template_file}")

            # Substitute placeholders
            for placeholder, value in placeholders.items():
                content = content.replace(placeholder, value)

            output_path = os.path.join(output_dir, output_file_name)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Successfully generated ==> {output_path}")

        except FileNotFoundError:
            print(f"Warning: Template file not found: {template_file}. Skipping.")
        except Exception as e:
            print(f"Error processing {template_file}: {e}")

    print("\n--- License Generation Complete ---")
    print(f"All files have been generated in the '{output_dir}' directory.")

if __name__ == "__main__":
    generate_license_files()
