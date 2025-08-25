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
ip_address = "192.168.12.1"
#ip_address = "127.0.0.1"
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

                """
                # 1) первые 10 регистров из ПЛК читаются
                holding_regs = client.read_holding_registers(0, count=10)
                registers: list = holding_regs.registers
                print("Holding Registers:", registers)
                # Holding Registers: [1408, 8, 0, 24, 0, 4, 434, 0, 0, 0]
                """

                """
                # 2) первые 10 регистров из ПЛК читаются
                #   !!! они почему-то равны Holding Registers
                input_regs = client.read_input_registers(0, count=10)
                print("Input Registers  :", input_regs.registers)
                # Input Registers: [1408, 8, 0, 24, 0, 4, 434, 0, 0, 0]
                """

                """
                # 3_1) значение одного регистра сохраняется
                client.write_register(5, 4)
                """

                """
                # 3_2) проверку пока не делаю
                # result = client.read_coils(0)
                # print(result.bits[0])
                """

                """
                # 4) катушки читаются
                print("100:", client.read_coils(100).bits[0])
                print("403:", client.read_coils(403))
                print("404:", client.read_coils(404))
                print("405:", client.read_coils(405))
                print("406:", client.read_coils(406))
                print("407:", client.read_coils(407))
                print("408:", client.read_coils(408))
                print("409:", client.read_coils(409))
                print("410:", client.read_coils(410))
                print()
                """

                """
                # 5) bool значение в катушку записывается
                client.write_coil(99, False)
                """

                """ OK
                # 6) температурные значения считываются
                holding_regs = client.read_holding_registers(34, count=3)
                registers: list = holding_regs.registers
                print("Holding Registers:", registers)
                # Holding Registers: [25, 65486, 5]

                # 7) температурные значения сохраняются
                client.write_register(34, 25)
                client.write_register(35, 65486)
                client.write_register(36, 5)
                """

                """
                # 8) хз пока как это понимать
                print("28:", client.read_coils(28))
                print("29:", client.read_coils(29))
                print("Holding Registers: ", client.read_holding_registers(28, count=2))
                print("Input Registers:     ", client.read_input_registers(28, count=2))
                    '''
                    OUT:
                    28: ReadCoilsResponse(dev_id=1, transaction_id=1, address=0, count=0, bits=[False, False, False, False, False, False, False, False], registers=[], status=1retries=0)
                    29: ReadCoilsResponse(dev_id=1, transaction_id=2, address=0, count=0, bits=[False, False, False, False, False, False, False, False], registers=[], status=1retries=0)
                    Holding Registers:  ReadHoldingRegistersResponse(dev_id=1, transaction_id=3, address=0, count=0, bits=[], registers=[18, 70], status=1retries=0)
                    Input Registers:      ReadInputRegistersResponse(dev_id=1, transaction_id=4, address=0, count=0, bits=[], registers=[18, 70], status=1retries=0)
                    '''
                """


                time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the client connection is closed
        client.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()
