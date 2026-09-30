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
    docker run -d ghcr.io/intrinseca/ocpp-mqtt-bridge:dev -h mqtt-broker-hostname.example
    ```

2. Connect your EV chargers to the OCPP Central Station using the provided URL.

Alternatively, use `docker-compose`:

```yaml
services:
  ocpp:
    image: ghcr.io/intrinseca/ocpp-mqtt-bridge:dev
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

This project uses uv for dependency management and packaging. Pushes to `main` publish the mutable `dev` image tag.

## Releases

Merge the release commit to `main`, then create and push an annotated tag at that commit, such as `v1.2.3`:

```bash
git tag -a v1.2.3 -m "Release v1.2.3"
git push origin v1.2.3
```

After the release workflow succeeds, verify that the published image tag is `ghcr.io/intrinseca/ocpp-mqtt-bridge:v1.2.3` and its installed `ocpp-mqtt-bridge` package version is `1.2.3`. Tags without the `v` prefix also work; the image tag always matches the Git tag.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, open an issue on [GitHub](https://github.com/intrinseca/ocpp-mqtt-bridge/issues).

## Acknowledgements

- [mobilityhouse ocpp](https://github.com/mobilityhouse/ocpp) for the OCPP implementation.
- [aiomqtt](https://aiomqtt.felixboehm.dev/) for the MQTT client.
- The Home Assistant community for their support and documentation.
