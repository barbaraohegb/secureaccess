# SecureAccess

## Overview

SecureAccess is a Python program designed to manage user access controls and permissions to enhance security on Windows systems. It allows you to retrieve a list of local users, set permissions for specific users on designated folders, and display current permissions for review.

## Features

- Retrieve a list of local users on the system.
- Set permissions (read, write, full) for users on specific folders.
- Display current permissions for a folder.

## Requirements

- Python 3.x
- pywin32 library

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using pip:
   ```bash
   pip install pywin32
   ```

## Usage

1. Modify the folder path in the `__main__` section to the folder where you want to manage permissions.

2. Run the script:
   ```bash
   python secure_access.py
   ```

3. The script will display the available local users. You can set permissions for these users by calling `set_user_permission` with the appropriate username and permission level.

4. Use `display_permissions` to review current permissions on the folder.

## Permissions

- **Read**: Allows reading of files and folders.
- **Write**: Allows writing and modifying files and folders.
- **Full**: Grants all access rights.

## Notes

- This program is designed for educational purposes. Always ensure you have permission to modify system settings and user permissions.
- Tested on Windows 10.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request.