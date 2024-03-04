# Load Balancer Configuration for Web Redundancy

This project aims to improve our web stack's reliability and capacity to handle increased traffic by introducing redundancy through the addition of a second web server and configuring a load balancer using HAProxy. This setup ensures that if one web server fails, the other can continue to handle requests, thereby increasing our infrastructure's fault tolerance.

## Overview

The project involves the following components:

- Two web servers (`gc-[STUDENT_ID]-web-01`, `gc-[STUDENT_ID]-web-02`) running Ubuntu 16.04 LTS, serving the web application.
- A load balancer (`gc-[STUDENT_ID]-lb-01`) also running Ubuntu 16.04 LTS, distributing incoming traffic between the two web servers.

## Prerequisites

- Ubuntu 16.04 LTS on all servers.
- Root or sudo access on all servers.
- Basic understanding of shell scripting, HAProxy, and web server configuration (Apache/Nginx).

## Configuration Steps

### 1. Install and Configure HAProxy on the Load Balancer

- **Script:** `install_haproxy.sh`
- **Purpose:** Installs HAProxy and configures it to balance requests between the two web servers.

### 2. Setup Web Servers

- **Script:** `setup_web_server.sh` (Run this script on both web servers)
- **Purpose:** Installs the web server software (Apache in this example) and sets up a simple test page to verify that the load balancing is working correctly.

## Usage

To deploy this setup, follow these steps:

1. Run `setup_web_server.sh` on both web servers to install and configure the web server software.
2. Run `install_haproxy.sh` on the load balancer to install HAProxy and apply the necessary configuration for load balancing.
3. Verify the setup by accessing the load balancer's IP address in a web browser. You should be served the test page from one of the web servers.

## Monitoring and Maintenance

- Access the HAProxy statistics page by navigating to `http://[LOAD_BALANCER_IP]/haproxy?stats` in your web browser.
- Regularly check the health of the web servers and the load balancer to ensure high availability.

## Troubleshooting

- If the web page does not load, check the HAProxy and web server logs for any errors.
- Ensure that HAProxy is correctly configured to point to the IPs of your web servers.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your enhancements.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

- Thanks to Holberton School for the project requirements.
- Special thanks to Sylvain Kalache for inspiring this project setup.
