# PhantomFog

Arp Spoofing tool written in python , redirects packets from a target host (or all hosts) on the LAN intended for another host on the LAN by forging ARP replies.

## Features
- Simple Interaction: Easy-to-use command-line interface for initiating ARP spoofing attacks.
- Target Selection: Specify target IP addresses to spoof and intercept communication.
- MITM Attacks: Conduct Man-in-the-Middle attacks by intercepting and manipulating network traffic.
- Packet Forwarding: Enable packet forwarding to ensure seamless communication between the target and other devices.

## Prerequisites

- Linux operating system
- Python 3
- git
- pip3 install -r requirements.txt

## Installation

git clone https://github.com/MedAmyyne/ArpSpoofer.git

## Help

Sudo python3 PhantomFog.py --help

## Options

-t1, --target1: Specify the first target IP.

-t2, --target2: Specify the second target IP.

## Usage

sudo python3 PhantomFog.py -t1 <first_target> -t2 <second_target>
