# 💻 Tech Stack: ![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=plastic&logo=pandas&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=plastic&logo=Streamlit&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-239120?style=plastic&logo=plotly&logoColor=white)

![Front page of the "Network Traffic Monitor"](/screenshot.jpg)

# Network Traffic Monitor

A real-time network traffic analysis dashboard that provides visual insights into network traffic patterns. Built with Python and Streamlit, this application enables network packet capture, analysis, and real-time visualisation.

## Background

Network traffic analysis is crucial in enterprise environments where networks form the backbone of applications and services. This tool enables:
- Real-time monitoring of network traffic (ingress and egress)
- Packet capture and interpretation
- Pattern identification and anomaly detection
- Network security and efficiency monitoring

The application serves as a practical tool for network troubleshooting, performance optimisation, and security analysis in enterprise systems.

## Tech Stack

- **Python 3.8+**: Core programming language
- **Streamlit**: Web application framework for data visualisation
- **Scapy**: Network packet capture and manipulation
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive data visualisation
- **Threading**: Concurrent packet capture and processing

## Features

- Real-time packet capture and analysis
- Interactive visualisation of protocol distribution
- Live timeline of packet frequency
- Protocol analysis (TCP, UDP, ICMP)
- Source/destination IP tracking
- Packet size monitoring
- Auto-refreshing dashboard
- Thread-safe packet processing
- Modular code structure

## Prerequisites

- Python 3.8+
- Administrator/root privileges (required for packet capture)
- Basic understanding of computer networking concepts
- Familiarity with TCP/IP protocols

## Project Structure

```
network-traffic-monitor/
├── dashboard.py        # Main Streamlit dashboard interface
├── packet_processor.py # Core packet capture and processing logic
├── visualizations.py   # Data visualisation components
├── config.py          # Logging and configuration settings
└── requirements.txt
```

### Component Description

- `dashboard.py`: Main application entry point and UI layout
- `packet_processor.py`: Handles packet capture and processing with protocol mapping (TCP, UDP, ICMP)
- `visualizations.py`: Creates and manages data visualisations (protocol distribution, packet timeline, top sources)
- `config.py`: Contains application-wide configuration settings and logging setup

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/network-traffic-monitor
cd network-traffic-monitor
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the dashboard:
```bash
# Linux/MacOS
sudo streamlit run dashboard.py

# Windows (Run as Administrator)
streamlit run dashboard.py
```

Note: Administrator/root privileges are required for packet capture functionality.

2. The dashboard provides:
   - Total packet count
   - Capture duration
   - Protocol distribution pie chart
   - Packets per second timeline
   - Top source IP addresses bar chart
   - Table of recent packets

3. The dashboard automatically refreshes every 2 seconds, with an option for manual refresh.

## Technical Details

### Key Components

- `PacketProcessor` (packet_processor.py):
  - Thread-safe packet capture and storage
  - Protocol mapping (TCP, UDP, ICMP)
  - Packet metadata extraction
  - Data management with size limiting (max 10,000 packets)

- Visualisation Module (visualizations.py):
  - Protocol distribution charts
  - Packet timeline graphs
  - Source IP analysis
  - Real-time data visualisation updates

- Dashboard Interface (dashboard.py):
  - Streamlit-based user interface
  - Real-time metrics display
  - Auto-refresh functionality
  - Recent packet display

### Architecture

- Modular design with separation of concerns
- Multi-threaded packet capture for non-blocking operation
- Thread-safe operations with proper locking mechanisms
- Memory-efficient storage with rolling window
- Centralised configuration and logging
- Session state management for persistent capture

## Security Considerations

- Requires root/administrator privileges for packet capture
- Only captures packet metadata (headers) - no payload inspection
- Local processing only - no external data transmission
- Thread-safe data handling

## Limitations

- Maximum storage of 10,000 packets in memory
- Requires elevated privileges
- Limited to IP-based protocols (TCP, UDP, ICMP)
- Single-threaded packet processing

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Licence

[MIT Licence](LICENCE)

## Acknowledgements

- Built with [Streamlit](https://streamlit.io/)
- Packet capture powered by [Scapy](https://scapy.net/)
- Visualisations using [Plotly](https://plotly.com/)
