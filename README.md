# VisionStream Core Feature

This repository contains the core feature of VisionStream, a real-time screen sharing tool that leverages websockets for efficient data transmission. This core functionality can be integrated into various applications where screen sharing capabilities are required.

## Overview

The VisionStream Core Feature is the backbone of a larger project that aims to provide seamless screen sharing capabilities. It is designed to be lightweight, efficient, and easy to integrate with other software components.

## Features

- **Real-Time Screen Capture**: Captures the screen in real-time with minimal latency.
- **Websocket Communication**: Utilizes websockets for fast and secure data transfer.
- **Cross-Platform**: Can be run on any platform that supports Python and the necessary dependencies.
- **Modular Design**: Designed to be a standalone component, making it easy to incorporate into larger systems.

## Getting Started

### Prerequisites

- Python 3.x
- Access to a command-line interface (CLI)

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/visionstream-core.git
```

### Navigate to the cloned directory and install the required dependencies:
```bash
cd visionstream-core
pip install -r requirements.txt
```
### Running the Core Feature

**To start the screen sharing server:**
```bash
# Run the server script
python server.py
```

**To connect a client to the server:**
```bash
# Run the client script
python client.py
```

## Usage
This core feature can be used as a starting point for building a full-fledged screen sharing application or for adding screen sharing capabilities to existing projects.

## Contributing
Contributions to improve the core feature or extend its capabilities are welcome. Please feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgements
- asyncio
- websockets
- Pillow
- pyautogui
- mss

## Contact
- Your Name - spmskperera@gmail.com
- Project Link: https://github.com/mskperera/realtime_screen_sharing_suite
