
# From homeassistant
def serial_to_unique_id(serial: int) -> str:
    """Convert a lutron serial number to a unique id."""
    return hex(serial)[2:].zfill(8)


def service_signal(service: str, *args: str) -> str:
    """Encode signal."""
    return "_".join(["amcrest", service, *args])


# External File