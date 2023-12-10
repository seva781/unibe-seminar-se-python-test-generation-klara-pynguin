
def serial_to_unique_id(serial: int):
    return hex(serial)[2:].zfill(8)