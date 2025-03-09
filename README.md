# Time Zone App

A simple web application built with **Streamlit** to display current time in multiple time zones and convert time between them, featuring country flags for a visual touch.

## Overview

This app allows users to:
- View the current time in selected time zones with corresponding country flags.
- Convert a specific time from one time zone to another.

The app uses the `datetime` and `zoneinfo` libraries for time handling and fetches flag images from `flagcdn.com`.

## Features
- **Multi-Timezone Display**: Select multiple time zones to see their current time.
- **Time Conversion**: Convert a chosen time from one timezone to another.
- **Visual Flags**: Each timezone is displayed with its respective country flag.

## Requirements
- Python 3.8+
- Streamlit
- `zoneinfo` (included in Python standard library since 3.9)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/RaoAsadMehmood/Time-Zone-App-.git
   cd Time-Zone-App-
2. Install Dependencies: Create a virtual environment (optional) and install the required package:
```bash
   streamlit run main.py   


## Usage
Select Timezones:
Use the multiselect dropdown to choose timezones.
The current time for each selected timezone will appear with its flag.
Convert Time:
Input a time using the time picker.
Choose the "From" and "To" timezones from the dropdowns.
Click "Convert Time" to see the converted time with the target timezone's flag.

## **Timezones Supported**
. UTC
. Asia/Karachi (Pakistan)
. America/New_York (USA)
. Europe/London (UK)
. Asia/Tokyo (Japan)
. Australia/Sydney (Australia)
. America/Los_Angeles (USA)
. Europe/Berlin (Germany)
. Asia/Dubai (UAE)
. Asia/Kolkata (India)

## Contributing
Feel free to fork this repository, submit pull requests, or open issues for bugs and feature requests.

## License
This project is open-source and available under the [MIT License](LICENSE).

Author
Rao Asad Mehmood
GitHub: RaoAsadMehmood
LinkedIn: [Rao Asad Mehmood](https://www.linkedin.com/in/rao-asad-mehmood/) 