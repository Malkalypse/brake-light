# Brake Light for AUTOMATIC1111

Brake Light is a modular control interface for managing interrupt and skip behavior in AUTOMATIC1111 workflows. It acts as a semantic “braking system,” allowing extensions to coordinate execution flow with clarity, responsiveness, and minimal overhead.

## Why Brake Light?

In complex AUTOMATIC1111 workflows, managing interrupt and skip behavior can become fragmented and opaque. Brake Light centralizes these control signals into a lightweight, reusable interface — making your scripts more responsive, readable, and audit-friendly.

## Features
- Unified interrupt and skip handling via a single decision point (interrupt_or_skip())
- UI status updates via `shared.state.textinfo`
- Designed for audit-friendly scripting environments
- Workflow-agnostic and reusable across extensions

## Installation
To use Brake Light in your AUTOMATIC1111 workflow:
1. **Download or clone** the repository
2. **Create a folder named `brake_light`** inside your AUTOMATIC1111 `extensions` directory.
3. **Place the contents of this repository** into that `brake_light` folder.
4. **Restart AUTOMATIC1111** if it's already running.

## Usage

```python
from extensions.brake_light import BrakeLight

brake = BrakeLight()
brake.reset()

if brake.interrupt_or_skip( "image generation" ):
    return None

brake.status( "Starting image generation..." )
```

## Version
Brake Light v1.0.0

## License
MIT License
