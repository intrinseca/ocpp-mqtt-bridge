# OCPP Central Station to MQTT Bridge

[![Build Status](https://img.shields.io/github/actions/workflow/status/intrinseca/ocpp-mqtt-bridge/ci.yml?branch=main)](https://github.com/intrinseca/ocpp-mqtt-bridge/actions)
[![License](https://img.shields.io/github/license/intrinseca/ocpp-mqtt-bridge)](LICENSE)
[![Version](https://img.shields.io/github/v/release/intrinseca/ocpp-mqtt-bridge)](https://github.com/intrinseca/ocpp-mqtt-bridge/releases)
[![Issues](https://img.shields.io/github/issues/intrinseca/ocpp-mqtt-bridge)](https://github.com/intrinseca/ocpp-mqtt-bridge/issues)

## Overview

This project implements an OCPP (Open Charge Point Protocol) Central Station and bridges it to MQTT for seamless integration with Home Assistant. The goal is to provide a reliable and easy-to-use solution for managing and monitoring EV chargers through Home Assistant.

## Features

- **OCPP Central Station**: Full implementation of OCPP 1.6 and 2.0.
- **MQTT Bridge**: Translates OCPP messages to MQTT topics.
- **Home Assistant Integration**: Easy setup with Home Assistant for real-time monitoring and control.
- **Docker Support**: Easily deployable with Docker.
- **Extensible**: Designed to be extended with new features and protocols.

## Compatibility

This project is tested with:

- BG SyncEV

## Getting Started

### Prerequisites

- Docker
- MQTT Broker (e.g., Mosquitto)
- Home Assistant

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/intrinseca/ocpp-mqtt-bridge.git
    cd ocpp-mqtt-bridge
    ```

2. Build and run the Docker container:
    ```bash
    docker-compose up --build -d
    ```

3. Configure your MQTT broker details in the `config.yaml` file.

4. Connect your EV chargers to the OCPP Central Station using the provided URL.

### Configuration

Update the `config.yaml` file with your MQTT broker details and other configuration parameters.

```yaml
mqtt:
  broker: 'mqtt://your_broker_address'
  username: 'your_username'
  password: 'your_password'
  topic_prefix: 'ocpp'

ocpp:
  port: 8082
```

### Home Assistant Integration

Home Assistant integration is facilitated via MQTT discovery. Ensure your MQTT broker is correctly configured in Home Assistant.

Add the following configuration to your `configuration.yaml` in Home Assistant:

```yaml
mqtt:
  broker: 'your_broker_address'
  username: 'your_username'
  password: 'your_password'

# Example configuration for MQTT discovery
homeassistant:
  mqtt:
    discovery: true
    discovery_prefix: homeassistant
```

MQTT discovery will automatically add your EV chargers as devices in Home Assistant.

## Usage

- Start the central station:
    ```bash
    docker-compose up
    ```
- Connect your EV chargers using the OCPP protocol.
- Monitor and control your chargers through Home Assistant.

## Development

This project uses Poetry for dependency management and packaging.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, open an issue on [GitHub](https://github.com/intrinseca/ocpp-mqtt-bridge/issues).

## Acknowledgements

- [mobilityhouse ocpp](https://github.com/mobilityhouse/ocpp) for the OCPP implementation.
- [asyncio-mqtt](https://github.com/sbtinstruments/asyncio-mqtt) for the MQTT client.
- The Home Assistant community for their support and documentation.
