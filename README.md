# OCPP Central Station to MQTT Bridge

[![Build Status](https://img.shields.io/github/actions/workflow/status/intrinseca/ocpp-mqtt-bridge/docker-image.yml?branch=main)](https://github.com/intrinseca/ocpp-mqtt-bridge/actions)
[![License](https://img.shields.io/github/license/intrinseca/ocpp-mqtt-bridge)](LICENSE)
[![Version](https://img.shields.io/github/v/release/intrinseca/ocpp-mqtt-bridge)](https://github.com/intrinseca/ocpp-mqtt-bridge/releases)
[![Issues](https://img.shields.io/github/issues/intrinseca/ocpp-mqtt-bridge)](https://github.com/intrinseca/ocpp-mqtt-bridge/issues)

## Overview

This project implements an OCPP (Open Charge Point Protocol) Central Station and bridges it to MQTT for seamless integration with Home Assistant. The goal is to provide a reliable and easy-to-use solution for managing and monitoring EV chargers through Home Assistant.

## Features

- **OCPP Central Station**: Implementation of OCPP 1.6.
- **MQTT Bridge**: Translates OCPP messages to MQTT topics.
- **Home Assistant Integration**: Easy setup with Home Assistant for real-time monitoring and control.
- **Docker Support**: Easily deployable with Docker.

## Compatibility

This project is tested with:

- BG SyncEV

## Getting Started

### Prerequisites

- Docker
- MQTT Broker (e.g., Mosquitto)
- Home Assistant

### Installation

1. Build and run the Docker container:
    ```bash
    docker run -d ghcr.io/intrinseca/ocpp-mqtt-bridge:main -h mqtt-broker-hostname.example
    ```

2. Connect your EV chargers to the OCPP Central Station using the provided URL.

Alternatively, use `docker-compose`:

```yaml
services:
  ocpp:
    image: ghcr.io/intrinseca/ocpp-mqtt-bridge:main
    container_name: ocpp
    ports:
      - "9000:9000" # map the websocket port you will program into the charge point
    volumes:
      - './logs:/app/logs'
    restart: always
    command: "-h mqtt-broker-hostname.example -p ocpp" # set to the address/hostname of your MQTT broker and the top-level MQTT topic to use
```

### Home Assistant Integration

(Not yet implemented)

Home Assistant integration is facilitated via MQTT discovery. Ensure your MQTT broker is correctly configured in Home Assistant.

MQTT discovery will automatically add your EV chargers as devices in Home Assistant.

## Development

This project uses Poetry for dependency management and packaging.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, open an issue on [GitHub](https://github.com/intrinseca/ocpp-mqtt-bridge/issues).

## Acknowledgements

- [mobilityhouse ocpp](https://github.com/mobilityhouse/ocpp) for the OCPP implementation.
- [aiomqtt](https://aiomqtt.felixboehm.dev/) for the MQTT client.
- The Home Assistant community for their support and documentation.
