# Project 0x13. Firewall

## Overview

In this project, we delve into the crucial aspect of cybersecurity - firewalls. This DevOps, SysAdmin, and Security project, designated with a weight of 1, was conducted from March 18, 2024, 6:00 AM to March 19, 2024, 6:00 AM. The project emphasizes the importance of securing servers using firewalls to prevent unauthorized access and attacks.

## Objectives

- Understand what a firewall is and its importance in securing networked systems.
- Learn to manage firewall rules to control traffic flow to and from servers.
- Use telnet to test and debug firewall configurations and socket connections.

## Background Context

Imagine your servers exposed to the internet without a firewall—a scenario akin to leaving your house with doors wide open. A firewall acts as a barrier or filter that controls the flow of traffic between your network and the rest of the internet, ensuring that only authorized traffic can enter or exit.

## Resources

To succeed in this project, you are encouraged to read or watch the following:

- [What is a firewall?](https://en.wikipedia.org/wiki/Firewall_(computing))

## More Info

### Debugging with Telnet

The web stack debugging guide introduces telnet, an effective tool for checking open sockets. For instance, to verify if port 22 is open on `web-02`, you could use:

```bash
sylvain@ubuntu$ telnet web-02.holberton.online 22
```

This method proves useful not only for this project but for any scenario requiring socket communication debugging.

### Note

The school's network employs a network-based firewall that may restrict outgoing connections to certain ports on external servers. To circumvent this, perform tests from servers outside the school network, such as your `web-02` server.

### Warning!

Avoid using containers on demand for this project due to Docker container limitations. Also, be cautious when configuring firewall rules. Improper settings, like denying port 22/TCP, could lock you out of your server permanently.

## Quiz Questions

Congratulations on completing the quiz successfully! Continue applying the knowledge as you progress through the project.

## Servers

For this project, you will be working with the following servers:

- `472670-web-01` | Username: ubuntu | State: running
- `472670-web-02` | Username: ubuntu | State: running
- `472670-lb-01` | Username: ubuntu | State: running

Ensure that you have SSH access to these servers and that your firewall configurations are correctly set to prevent unauthorized access while maintaining necessary operational communications.

## Conclusion

Securing your network with a firewall is a fundamental step in safeguarding your digital assets from potential threats. This project offers a hands-on approach to understanding, implementing, and managing firewalls effectively.
