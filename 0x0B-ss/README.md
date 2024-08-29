# 0x0B. SSH

## Introduction

This project is part of the ALX Software Engineering Program and focuses on understanding and implementing Secure Shell (SSH) for secure server connections. Throughout this project, we learned the following key concepts:

- **What is a server**: Understanding the role and function of servers in a network.
- **Where servers usually live**: Exploring typical server environments and data centers.
- **What is SSH**: Learning about Secure Shell (SSH) and its importance in secure communication.
- **How to create an SSH RSA key pair**: Generating RSA key pairs for secure authentication.
- **How to connect to a remote host using an SSH RSA key pair**: Establishing secure connections to remote servers.
- **The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`**: Understanding the benefits of using the env command for portability.

## Tasks

We completed the following tasks as part of this project:

1. **Use a private key**:
   - Write a Bash script that uses SSH to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.
   - **Requirements**:
     - Only use SSH single-character flags.
     - You cannot use `-l`.
     - You do not need to handle the case of a private key protected by a passphrase.

2. **Create an SSH key pair**:
   - Write a Bash script that creates an RSA key pair.
   - **Requirements**:
     - Name of the created private key must be `school`.
     - Number of bits in the created key: 4096.
     - The created key must be protected by the passphrase `betty`.

3. **Client configuration file**:
   - Configure your local SSH client to connect to a server without typing a password.
   - **Requirements**:
     - Configure the SSH client to use the private key `~/.ssh/school`.
     - Configure the SSH client to refuse to authenticate using a password.

4. **Let me in!**:
   - Add the provided SSH public key to your server so that others can connect using the `ubuntu` user.

5. **Client configuration file (w/ Puppet)**:
   - Use Puppet to set up your client SSH configuration file to connect to a server without typing a password.
   - **Requirements**:
     - Configure the SSH client to use the private key `~/.ssh/school`.
     - Configure the SSH client to refuse to authenticate using a password.

This project has enhanced our understanding of SSH and its practical applications in secure server management. Feel free to explore the scripts and configurations provided in this repository. If you have any questions or need further assistance, don't hesitate to reach out.
