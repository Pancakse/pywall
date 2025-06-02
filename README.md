# pyWall – A Simple Custom Firewall in Python

`pyWall` is a lightweight, customizable firewall written in Python that inspects and filters network packets based on user-defined rules. Designed for educational and experimental use, it offers packet monitoring, IP/port filtering, and logging — all using pure Python with `scapy`.

## Features

- Define custom rules (block/allow by IP, port, protocol)
- Real-time packet inspection using `scapy`
- Logging of blocked packets with timestamps
- 🖥Simple CLI interface for managing rules
- JSON-based configuration

## Getting Started

## Prerequisites

- Python 3.7+
- Root privileges (required for packet sniffing)

## Installation

```bash
git clone https://github.com/yourusername/pywall.git
cd pywall
pip install -r requirements.txt
