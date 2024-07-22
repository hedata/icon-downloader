# Technology Icon Downloader

This project provides a Python script that automates the process of downloading and resizing favicon icons for a list of technologies specified in a YAML file. It's useful for creating a consistent set of icons for technology stacks or project dependencies.

## Features

- Reads a list of technologies and their URLs from a YAML file
- Attempts to download the favicon for each technology
- Resizes icons to 32x32 pixels
- Saves icons as PNG files
- Generates a report of successful and failed downloads

## Requirements

- Python 3.9+
- Conda (for environment management)

## Setup

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/technology-icon-downloader.git
   cd technology-icon-downloader
   ```

2. Create the Conda environment:

   ```
   conda env create -f environment.yml
   ```

3. Activate the environment:
   ```
   conda activate icon-downloader
   ```

## Usage

1. Prepare your `technologies.yaml` file with the following structure:

   ```yaml
   Technology Name:
     url: https://technology-website.com
     tags:
       - tag1
       - tag2
   ```

2. Place the `technologies.yaml` file in the same directory as the script.

3. Run the script:

   ```
   python icon_downloader.py
   ```

4. After execution, you'll find:
   - An `icons` directory containing the downloaded icons
   - A `report.yml` file detailing the results of each download attempt

## Output

The script generates two main outputs:

1. Icon files:

   - Located in the `icons` directory
   - Named in the format `technology_name_icon.png`
   - All icons are 32x32 pixels in PNG format

2. Report file (`report.yml`):
   ```yaml
   Technology Name:
     success: true/false
     filename: technology_name_icon.png / null
   ```

## Troubleshooting

- If a download fails, check the technology's URL and ensure it's accessible.
- Some websites may use non-standard methods for favicon delivery, which might cause failures.
- Ensure you have internet connectivity when running the script.

## Legal Considerations

Please note that downloading and using favicons may be subject to copyright restrictions. Ensure you have the right to use these icons for your intended purpose.

## Contributing

Contributions to improve the script or documentation are welcome. Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

MIT
