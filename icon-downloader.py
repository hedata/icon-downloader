import yaml
import requests
from PIL import Image
from io import BytesIO
import os
from bs4 import BeautifulSoup


def download_favicon(url, technology_name):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Try to find favicon link
        favicon_link = soup.find("link", rel=["icon", "shortcut icon"])

        if favicon_link and favicon_link.get("href"):
            favicon_url = favicon_link["href"]
            if not favicon_url.startswith("http"):
                # If the favicon URL is relative, make it absolute
                favicon_url = f"{url.rstrip('/')}/{favicon_url.lstrip('/')}"
        else:
            # If no favicon link found, try the default location
            favicon_url = f"{url.rstrip('/')}/favicon.ico"

        favicon_response = requests.get(favicon_url)
        img = Image.open(BytesIO(favicon_response.content))

        # Resize to 32x32
        img = img.resize((32, 32), Image.LANCZOS)

        # Save as PNG
        filename = f"{technology_name.replace(' ', '_').lower()}_icon.png"
        img.save(filename, "PNG")
        print(f"Downloaded and saved icon for {technology_name}")
        return True, filename
    except Exception as e:
        print(f"Error downloading icon for {technology_name}: {str(e)}")
        return False, None


def main():
    # Load YAML file
    with open("technologies.yaml", "r") as file:
        technologies = yaml.safe_load(file)

    # Create a directory for icons if it doesn't exist
    if not os.path.exists("icons"):
        os.makedirs("icons")

    # Change to the icons directory
    os.chdir("icons")

    # Dictionary to store report data
    report = {}

    # Download icons for each technology
    for tech_name, tech_info in technologies.items():
        success, filename = download_favicon(tech_info["url"], tech_name)
        report[tech_name] = {
            "success": success,
            "filename": filename if success else None,
        }

    # Change back to the original directory
    os.chdir("..")

    # Write report to YAML file
    with open("report.yml", "w") as file:
        yaml.dump(report, file, default_flow_style=False)

    print("Report generated: report.yml")


if __name__ == "__main__":
    main()
