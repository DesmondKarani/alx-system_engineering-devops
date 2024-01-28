![Secured and Monitored Web Infrastructure](2-secured_and_monitored_web_infrastructure.png)

## Description
This design illustrates a secured and monitored web infrastructure for hosting the website www.foobar.com. The setup includes advanced security measures and monitoring mechanisms to ensure the website's integrity, confidentiality, and availability.

## Additional Elements and Their Purposes
- **3 Firewalls**: Provide a barrier between your internal network and incoming traffic from external sources (internet) to block malicious traffic like viruses and hackers.
- **1 SSL Certificate**: Encrypts data transferred over the internet between the website and its users, ensuring secure transactions.
- **3 Monitoring Clients**: Tools like Sumologic or similar are used to collect and analyze data to provide insights into the performance and security of the web infrastructure.

## Explanation of Specifics
### What Are Firewalls For
Firewalls are security devices—either hardware or software—that monitor and control incoming and outgoing network traffic based on predetermined security rules.

### Why Is the Traffic Served Over HTTPS
HTTPS (Hypertext Transfer Protocol Secure) is used to secure communication over a computer network. It provides encrypted and secure identification of a network web server, protecting transmitted data from eavesdropping and tampering.

### What Monitoring Is Used For
Monitoring is used to continuously observe the health and performance of the web infrastructure. It helps in identifying and addressing issues proactively, ensuring the system's reliability and efficiency.

### How the Monitoring Tool Is Collecting Data
Monitoring tools collect data through agents installed on the server. These agents gather various metrics and logs, which are then transmitted to a central monitoring service for analysis.

### Explain What to Do If You Want to Monitor Your Web Server QPS
To monitor the Query Per Second (QPS) of your web server, you need to configure your monitoring tool to track and report on the number of requests the server receives and processes each second.

## Infrastructure Issues
### Why Terminating SSL at the Load Balancer Level Is an Issue
Terminating SSL at the load balancer can pose a security risk as the traffic between the load balancer and web servers would be unencrypted, potentially exposing sensitive data.

### Why Having Only One MySQL Server Capable of Accepting Writes Is an Issue
A single MySQL server for write operations is a bottleneck and a point of failure. If this server goes down, it would halt all write operations, affecting the website's availability and performance.

### Why Having Servers with All the Same Components Might Be a Problem
Using servers with identical setups (database, web server, application server) can lead to resource contention and does not allow for specialized configurations that optimize the performance of each component.
