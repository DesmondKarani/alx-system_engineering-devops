# Web Server Configuration Project

## Overview

This project aims to automate the configuration of a web server using Bash scripting, focusing on automating repetitive tasks for software reliability engineering (SRE). By automating the setup and configuration of a web server, we can ensure consistency, reduce human error, and improve the efficiency of managing server infrastructure.

## Objectives

- **Understand the main role of a web server** and how it processes HTTP requests.
- **Learn about child processes** and their importance in web server operations.
- **Explore DNS and its role** in resolving domain names to IP addresses.
- **Automate web server configuration** to meet specific requirements without manual intervention.

## Tasks

1. **Web Server Setup:** Configure `web-01` server according to the specified requirements.
2. **Automation Script:** Create a Bash script to automatically perform commands to configure an Ubuntu machine, including server setup and modifications.

## Requirements

- **Operating System:** All scripts and configurations are to be tested on Ubuntu 16.04 LTS.
- **Editing Tools:** Use of vi, vim, or emacs is allowed for editing files.
- **Script Specifications:**
  - All Bash script files must be executable.
  - Scripts must pass Shellcheck (version 0.3.7) without any error.
  - The first line of all Bash scripts must be `#!/usr/bin/env bash`.
  - The second line must contain a comment explaining the script's purpose.
- **Service Management:** Direct use of `systemctl` for restarting processes is prohibited.

## Testing

To ensure the scripts work as expected:
- Start an Ubuntu 16.04 sandbox environment.
- Run the script to configure the server.
- Verify that the server operates according to the project requirements.

## Learning Resources

- How the web works
- Configuring Nginx
- Understanding child processes
- DNS and its role in the web

## Project Submission

Submit all scripts and documentation by the project deadline. Ensure that your scripts are well-commented and adhere to the project guidelines.

## Disclaimer

This project is for educational purposes only. Plagiarism is prohibited, and all work submitted must be your own.
