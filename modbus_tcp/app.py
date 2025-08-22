#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
source:
    https://docs.golenishchev-electronics.ru/ru/smarttgm/pymodbus_smarttgm_guide
docs:
    https://pymodbus.readthedocs.io/en/latest/source/client.html#modbus-calls
"""

import struct
import time
from datetime import datetime

from pymodbus.client import ModbusTcpClient

ip_address = "192.168.0.208"
ip_address = "127.0.0.1"
port = 502


def current_time():
    return datetime.now().isoformat()


def registers_to_float(register1, register2):  # хз, нужно ли это, пусть пока будет тут
    """Function to convert two 16-bit registers to a float, trying both endianness"""
    try:
        # Try little-endian byte order
        packed_le = struct.pack("<HH", register1, register2)
        value_le = struct.unpack("<f", packed_le)[0]

        # Try big-endian byte order
        packed_be = struct.pack(">HH", register1, register2)
        value_be = struct.unpack(">f", packed_be)[0]

        # Choose the most plausible value
        if abs(value_le) < 1e10 and not struct.unpack("<I", packed_le)[0] == 0x7FC00000:
            return value_le
        elif (
            abs(value_be) < 1e10 and not struct.unpack(">I", packed_be)[0] == 0x7FC00000
        ):
            return value_be
        else:
            print("Both float interpretations seem invalid")
            return None
    except Exception as e:
        print(f"Error interpreting float: {e}")
        return None


def main():

    client = ModbusTcpClient(ip_address, port=port)

    try:
        # Attempt to connect to the Modbus client
        if not client.connect():
            print(f"Failed to connect to {ip_address}")
        else:
            print(f"Connected to {ip_address}")

            while True:

                """это пока не работает, но может еще пригодится
                # Read input registers
                input_regs = client.read_input_registers(0, count=6)
                print("Input Registers:", input_regs.registers)
                """

                # Read holding registers
                holding_regs = client.read_holding_registers(0, count=10)
                registers: list = holding_regs.registers

                print("Holding Registers:", registers)

                client.write_register(5, 4)
                # result = client.read_coils(0)
                # print(result.bits[0])

                # Sleep for a second
                time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the client connection is closed
        client.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()
