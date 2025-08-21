#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
source:
	https://docs.golenishchev-electronics.ru/ru/smarttgm/pymodbus_smarttgm_guide
"""

from pymodbus.client import ModbusTcpClient 	# pip install pymodbus
from datetime import datetime
import time
import struct

# Define the Modbus TCP server IP address
ip_address = "192.168.0.208"
ip_address = "127.0.0.1"
port = 502  # Default Modbus TCP port

# Function to get current time
def current_time():
    return datetime.now().isoformat()

# Function to convert two 16-bit registers to a float, trying both endianness
def registers_to_float(register1, register2):
    try:
        # Try little-endian byte order
        packed_le = struct.pack('<HH', register1, register2)
        value_le = struct.unpack('<f', packed_le)[0]

        # Try big-endian byte order
        packed_be = struct.pack('>HH', register1, register2)
        value_be = struct.unpack('>f', packed_be)[0]

        # Choose the most plausible value
        if abs(value_le) < 1e10 and not struct.unpack('<I', packed_le)[0] == 0x7FC00000:
            return value_le
        elif abs(value_be) < 1e10 and not struct.unpack('>I', packed_be)[0] == 0x7FC00000:
            return value_be
        else:
            print("Both float interpretations seem invalid")
            return None
    except Exception as e:
        print(f"Error interpreting float: {e}")
        return None

# Initialize Modbus TCP client
client = ModbusTcpClient(ip_address, port=port)

try:
    # Attempt to connect to the Modbus client
    if not client.connect():
        print(f"Failed to connect to {ip_address}")
    else:
        print(f"Connected to {ip_address}")
        while True:
            # Read input registers
            input_regs = client.read_input_registers(0, count=6)
            print("Input Registers:", input_regs.registers)

            # Interpret input registers as floats
            current1 = registers_to_float(input_regs.registers[0], input_regs.registers[1])
            current2 = registers_to_float(input_regs.registers[2], input_regs.registers[3])
            current3 = registers_to_float(input_regs.registers[4], input_regs.registers[5])

            # Print the currents with 6 decimal places if they are valid
            if current1 is not None:
                print(f"Current 1: {current1:.6f}")
            if current2 is not None:
                print(f"Current 2: {current2:.6f}")
            if current3 is not None:
                print(f"Current 3: {current3:.6f}")

            # Sleep for a second
            time.sleep(1)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Ensure the client connection is closed
    client.close()
    print("Connection closed.")
