import sys
import DataType
import DataSize
import serial
import socket
import math
import serial.tools.list_ports as serialports
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main.ui")[0]


class WindowClass(QMainWindow, form_class):
    COM = 0
    ETHERNET = 1

    font_size = 10
    font = "Gulim"

    main_data = [[], [], [], [], [], [], [], [], [], []]
    main_data_load_start = 0
    main_data_load_end = 1000

    appearanceDataSize = DataSize.BYTE
    appearanceDataType = DataType.INT
    ConnectionType = 0
    ETOS = ["ETOS", "ETOS", "ETOS"]

    LSPLC = ["XGI", "XGR", "XGK", "XGB(XBC)", "XGB(XEC)", "MASTER-K", "GLOFA-GM", "XGS"]
    LSPLC_XGI = ["XGI-CPUUN", "XGI-CPUU", "XGI-CPUH", "XGI-CPUS", "XGI-CPUE"]
    LSPLC_XGK = ["XGK-CPUUN", "XGK-CPUHN", "XGK-CPUSN", "XGK-CPUU", "XGK-CPUH", "XGK-CPUA", "XGK-CPUS", "XGK-CPUE"]
    LSPLC_XGR = ["XGR-CPUH/T", "XGR-CPUH/F", "XGR-CPUH/S"]
    LSPLC_XBC = ["XBC U TYPE", "XBC H TYPE", "XBC SU TYPE", "XBC E TYPE", "XBM TYPE", "XBM Slim"]
    LSPLC_XEC = ["XEC U TYPE", "XEC H TYPE", "XEC SU TYPE", "XEC E TYPE", "XEM TYPE"]
    LSPLC_MASTERK = ["K120S", " K200S", "K300S", "K10S1", "K80S", "K1000S", "K10S", "K30S", "K60S"]
    LSPLC_GLOFA = ["GM1", "GM2", "GM3", "GM4-CPUA", "GM4-CPUB", "GM4-CPUC", "GM6", "GM7U", "GMR"]
    serial = serial.Serial
    socket = socket.socket

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.port_refresh()
        self.Comm_Product_C.addItems(self.ETOS)
        self.button_menu_refresh_function()
        self.button_menu_refresh_function_2()

        self.Comm_Product.currentIndexChanged.connect(self.commsel_comm_product)
        self.Comm_Product_C.currentIndexChanged.connect(self.commsel_comm_product_c)
        self.CommSel_COM.clicked.connect(self.commsel_comm_type_function)
        self.CommSel_ETH.clicked.connect(self.commsel_comm_type_function)
        self.Comm_Refresh.clicked.connect(self.comm_refresh_function)
        """menu line2"""
        self.BitSel_Bit.clicked.connect(self.bitsel_bit_function)
        self.BitSel_Byte.clicked.connect(self.bitsel_byte_function)
        self.BitSel_Word.clicked.connect(self.bitsel_word_function)
        self.BitSel_DWord.clicked.connect(self.bitsel_dword_function)
        self.BitSel_LWord.clicked.connect(self.bitsel_lword_function)
        self.DataSel_Binary.clicked.connect(self.datasel_binary_function)
        self.DataSel_BCD.clicked.connect(self.datasel_bcd_function)
        self.DataSel_Int.clicked.connect(self.datasel_int_function)
        self.DataSel_UInt.clicked.connect(self.datasel_uint_function)
        self.DataSel_HEX.clicked.connect(self.datasel_hex_function)
        self.DataSel_Float.clicked.connect(self.datasel_float_function)
        self.DataSel_String.clicked.connect(self.datasel_string_function)
        self.FontSel_FontUp.clicked.connect(self.fontsel_font_up_function)
        self.FontSel_FontDown.clicked.connect(self.fontsel_font_down_function)
        self.Comm_Connect.clicked.connect(self.comm_connect_function)
        self.memory_search.clicked.connect(self.search_memory_function)

    def commsel_comm_product(self):
        if self.Comm_Product.currentIndex() == 0:
            self.Comm_Product_C.clear()
            self.Comm_Product_C.addItems(self.ETOS)
        elif self.Comm_Product.currentIndex() == 1:
            self.Comm_Product_C.clear()
            self.Comm_Product_C.addItems(self.LSPLC)

    def commsel_comm_product_c(self):
        if self.Comm_Product_C.currentIndex() == 0:
            self.Comm_Product_S_Name.clear()
            self.Comm_Product_S_Name.addItems(self.LSPLC_XGI)
        elif self.Comm_Product_C.currentIndex() == 1:
            self.Comm_Product_S_Name.clear()
            self.Comm_Product_S_Name.addItems(self.LSPLC_XGR)
        elif self.Comm_Product_C.currentIndex() == 2:
            self.Comm_Product_S_Name.clear()
            self.Comm_Product_S_Name.addItems(self.LSPLC_XGK)
        elif self.Comm_Product_C.currentIndex() == 3:
            self.Comm_Product_S_Name.clear()
            self.Comm_Product_S_Name.addItems(self.LSPLC_XBC)
        elif self.Comm_Product_C.currentIndex() == 4:
            self.Comm_Product_S_Name.clear()
            self.Comm_Product_S_Name.addItems(self.LSPLC_XEC)
        elif self.Comm_Product_C.currentIndex() == 5:
            self.Comm_Product_S_Name.clear()
            self.Comm_Product_S_Name.addItems(self.LSPLC_MASTERK)
        elif self.Comm_Product_C.currentIndex() == 6:
            self.Comm_Product_S_Name.clear()
            self.Comm_Product_S_Name.addItems(self.LSPLC_GLOFA)
        elif self.Comm_Product_C.currentIndex() == 7:
            self.Comm_Product_S_Name.clear()
            self.Comm_Product_S_Name.addItems(self.LSPLC_XGR)

    def commsel_comm_type_function(self):
        if self.CommSel_COM.isChecked():
            self.ConnectionType = self.COM
            self.IP_1.setEnabled(False)
            self.IP_2.setEnabled(False)
            self.IP_3.setEnabled(False)
            self.IP_4.setEnabled(False)
            self.CommSel_Comport.setEnabled(True)
        elif self.CommSel_ETH.isChecked():
            self.ConnectionType = self.ETHERNET
            self.IP_1.setEnabled(True)
            self.IP_2.setEnabled(True)
            self.IP_3.setEnabled(True)
            self.IP_4.setEnabled(True)
            self.CommSel_Comport.setEnabled(False)

    def comm_refresh_function(self):
        self.port_refresh()

    def bitsel_bit_function(self):
        self.appearanceDataSize = DataSize.BIT
        self.button_menu_refresh_function()

    def bitsel_byte_function(self):
        self.appearanceDataSize = DataSize.BYTE
        self.button_menu_refresh_function()

    def bitsel_word_function(self):
        self.appearanceDataSize = DataSize.WORD
        self.button_menu_refresh_function()

    def bitsel_dword_function(self):
        self.appearanceDataSize = DataSize.DWORD
        self.button_menu_refresh_function()

    def bitsel_lword_function(self):
        self.appearanceDataSize = DataSize.LWORD
        self.button_menu_refresh_function()

    def datasel_binary_function(self):
        self.appearanceDataType = DataType.BINARY
        self.button_menu_refresh_function_2()

    def datasel_bcd_function(self):
        self.appearanceDataType = DataType.BCD
        self.button_menu_refresh_function_2()

    def datasel_int_function(self):
        self.appearanceDataType = DataType.INT
        self.button_menu_refresh_function_2()

    def datasel_uint_function(self):
        self.appearanceDataType = DataType.UINT
        self.button_menu_refresh_function_2()

    def datasel_hex_function(self):
        self.appearanceDataType = DataType.HEX
        self.button_menu_refresh_function_2()

    def datasel_float_function(self):
        self.appearanceDataType = DataType.FLOAT
        self.button_menu_refresh_function_2()

    def datasel_string_function(self):
        self.appearanceDataType = DataType.STRING
        self.button_menu_refresh_function_2()

    def fontsel_font_up_function(self):
        self.font_size = self.font_size + 1

    def fontsel_font_down_function(self):
        self.font_size = self.font_size - 1

    def comm_connect_function(self):
        if self.ConnectionType == self.COM:
            self.serial = serial.Serial("COM3", 9600, timeout=0)

        elif self.ConnectionType == self.ETHERNET:
            try:
                self.serial = serial.serial_for_url("socket://" +
                                                    self.IP_1.text() + "." +
                                                    self.IP_2.text() + "." +
                                                    self.IP_3.text() + "." +
                                                    self.IP_4.text() + ":2004")
                mainWindow.statusBar().showMessage("온라인, 접속 완료")
                self.serial.close()
            except ValueError:
                """경고창 띄우기"""
                mainWindow.statusBar().showMessage("오프라인, 접속 대기중")

    def get_data(self, memory, address):
        send_packet = self.ethernet_packet_maker(memory, address)
        self.serial.write(send_packet)
        receive_packet = bytearray()
        for x in range(0, 1032):
            a = self.serial.read()
            if x > 31:
                receive_packet.append(int.from_bytes(a, "big"))
        return receive_packet

    def search_memory_function(self):
        start_memory = str(self.search_start_memory.text())
        end_memory = str(self.search_end_memory.text())
        if self.Comm_Product.currentIndex == 0:
            return

        elif self.Comm_Product.currentIndex == 1:
            if self.Comm_Product_C.currentIndex == 0:
                self.xec_search(start_memory, end_memory)
            elif self.Comm_Product_C.currentIndex == 1:
                self.xec_search(start_memory, end_memory)
            elif self.Comm_Product_C.currentIndex == 4:
                self.xec_search(start_memory, end_memory)

    def xec_search(self, data1, data2):
        start_memory = bytearray(data1)
        end_memory = bytearray(data2)
        if not(start_memory[0] == '%'):
            return



    def button_menu_refresh_function(self):
        self.BitSel_Bit.setChecked(False)
        self.BitSel_Byte.setChecked(False)
        self.BitSel_Word.setChecked(False)
        self.BitSel_DWord.setChecked(False)
        self.BitSel_LWord.setChecked(False)
        if self.appearanceDataSize == DataSize.BIT:
            self.BitSel_Bit.setChecked(True)
        elif self.appearanceDataSize == DataSize.BYTE:
            self.BitSel_Byte.setChecked(True)
        elif self.appearanceDataSize == DataSize.WORD:
            self.BitSel_Word.setChecked(True)
        elif self.appearanceDataSize == DataSize.DWORD:
            self.BitSel_DWord.setChecked(True)
        elif self.appearanceDataSize == DataSize.LWORD:
            self.BitSel_LWord.setChecked(True)

    def button_menu_refresh_function_2(self):
        self.DataSel_Binary.setChecked(False)
        self.DataSel_BCD.setChecked(False)
        self.DataSel_Int.setChecked(False)
        self.DataSel_UInt.setChecked(False)
        self.DataSel_HEX.setChecked(False)
        self.DataSel_Float.setChecked(False)
        self.DataSel_String.setChecked(False)
        if self.appearanceDataType == DataType.BINARY:
            self.DataSel_Binary.setChecked(True)
        elif self.appearanceDataType == DataType.BCD:
            self.DataSel_BCD.setChecked(True)
        elif self.appearanceDataType == DataType.INT:
            self.DataSel_Int.setChecked(True)
        elif self.appearanceDataType == DataType.UINT:
            self.DataSel_UInt.setChecked(True)
        elif self.appearanceDataType == DataType.HEX:
            self.DataSel_HEX.setChecked(True)
        elif self.appearanceDataType == DataType.FLOAT:
            self.DataSel_Float.setChecked(True)
        elif self.appearanceDataType == DataType.STRING:
            self.DataSel_String.setChecked(True)

    def port_refresh(self):
        serial_ports_list = serialports.comports()
        self.CommSel_Comport.clear()
        if len(serial_ports_list) == 0:
            self.CommSel_Comport.addItem("NO PORT")
        else:
            ports = []
            for i in serial_ports_list:
                ports.append(i.device)
            self.CommSel_Comport.addItems(ports)

    def ethernet_packet_maker(self, memory, address):
        application_header = bytearray("LSIS-XGT", encoding='ASCII')
        application_header.append(0x00);application_header.append(0x00)
        application_header.append(0x00);application_header.append(0x00)
        application_header.append(0xA0)
        application_header.append(0x33)
        application_header.append(0x01);application_header.append(0x00)
        application_header.append(15 + len(str(address)));application_header.append(0x00)
        application_header.append(0x01)
        application_header.append(0x00)
        application_instruction = bytearray()
        application_instruction.append(0x54)
        application_instruction.append(0x00)
        application_instruction.append(0x14)
        application_instruction.append(0x00)
        application_instruction.append(0x00)
        application_instruction.append(0x00)
        application_instruction.append(0x01)
        application_instruction.append(0x00)
        application_instruction.append(0x04)
        application_instruction.append(0x00)
        application_instruction.append(0x25)
        application_instruction.append(bytearray(str(memory), encoding="ASCII")[0])
        application_instruction.append(0x42)
        application_instruction = application_instruction + bytearray(str(address), encoding="ASCII")
        application_instruction.append(0xE8)
        application_instruction.append(0x03)
        send_data_packet = application_header + application_instruction
        return send_data_packet


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = WindowClass()
    mainWindow.show()
    mainWindow.CommSel_COM.setChecked(True)
    mainWindow.IP_1.setEnabled(False)
    mainWindow.IP_2.setEnabled(False)
    mainWindow.IP_3.setEnabled(False)
    mainWindow.IP_4.setEnabled(False)
    mainWindow.statusBar().showMessage("오프라인, 접속 대기중")
    mainWindow.setWindowTitle("메모리 뷰어")
    app.exec_()
