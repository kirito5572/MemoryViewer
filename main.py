import sys
import DataType
import DataSize
import data_structure_maker
import PLC_Data
import pyautogui
import serial
import serial.serialutil as serialutil
import socket
import struct
import serial.tools.list_ports as serialports
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from bitarray import bitarray

form_class = uic.loadUiType("main.ui")[0]


def memory_end_detector(end, memory):
    if mainWindow.Comm_Product.currentIndex() == 0:
        pass
    elif mainWindow.Comm_Product.currentIndex() == 1:
        memory_sel = 0
        if mainWindow.Comm_Product_C.currentIndex() == 0:
            for i in range(len(PLC_Data.XGI)):
                if PLC_Data.XGI[i] == memory:
                    memory_sel = i
                    break
            if mainWindow.Comm_Product_S_Name.currentIndex() == 0:
                data = PLC_Data.XGI_CPUUN[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 1:
                data = PLC_Data.XGI_CPUU[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 2:
                data = PLC_Data.XGI_CPUH[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 3:
                data = PLC_Data.XGI_CPUS[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 4:
                data = PLC_Data.XGI_CPUE[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
        elif mainWindow.Comm_Product_C.currentIndex() == 1:
            for i in range(len(PLC_Data.XGI)):
                if PLC_Data.XGI[i] == memory:
                    memory_sel = i
                    break
            data = PLC_Data.XGR_CPUH[memory_sel]
            if end > data:
                return [data // 1000, data % 1000]
        elif mainWindow.Comm_Product_C.currentIndex() == 2:
            for i in range(len(PLC_Data.XGK)):
                if PLC_Data.XGK[i] == memory:
                    memory_sel = i
                    break
            if mainWindow.Comm_Product_S_Name.currentIndex() == 0:
                data = PLC_Data.XGK_CPUUN[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 1:
                data = PLC_Data.XGK_CPUHN[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 2:
                data = PLC_Data.XGK_CPUSN[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 3:
                data = PLC_Data.XGK_CPUU[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 4:
                data = PLC_Data.XGK_CPUH[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 5:
                data = PLC_Data.XGK_CPUA[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 6:
                data = PLC_Data.XGK_CPUS[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 7:
                data = PLC_Data.XGK_CPUE[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
        elif mainWindow.Comm_Product_C.currentIndex() == 3:
            if mainWindow.Comm_Product_S_Name.currentIndex() == 0:
                for i in range(len(PLC_Data.XGK)):
                    if PLC_Data.XGK[i] == memory:
                        memory_sel = i
                        break
                data = PLC_Data.XBC_TYPE_U[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 1:
                for i in range(len(PLC_Data.XGK)):
                    if PLC_Data.XGK[i] == memory:
                        memory_sel = i
                        break
                data = PLC_Data.XBC_TYPE_H[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 2:
                for i in range(len(PLC_Data.XBC_SU)):
                    if PLC_Data.XBC_SU[i] == memory:
                        memory_sel = i
                        break
                data = PLC_Data.XBC_TYPE_SU[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 3:
                for i in range(len(PLC_Data.XBC_E)):
                    if PLC_Data.XBC_E[i] == memory:
                        memory_sel = i
                        break
                data = PLC_Data.XBC_TYPE_E[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 4:
                for i in range(len(PLC_Data.XBC_S)):
                    if PLC_Data.XBC_S[i] == memory:
                        memory_sel = i
                        break
                data = PLC_Data.XBM_SILM[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
        elif mainWindow.Comm_Product_C.currentIndex() == 4:
            if mainWindow.Comm_Product_S_Name.currentIndex() == 0:
                for i in range(len(PLC_Data.XGI)):
                    if PLC_Data.XGI[i] == memory:
                        memory_sel = i
                        break
                data = PLC_Data.XEC_TYPE_U[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 1:
                for i in range(len(PLC_Data.XGI)):
                    if PLC_Data.XGI[i] == memory:
                        memory_sel = i
                        break
                data = PLC_Data.XEC_TYPE_H[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 2:
                for i in range(len(PLC_Data.XEC)):
                    if PLC_Data.XEC[i] == memory:
                        memory_sel = i
                        break
                data = PLC_Data.XEC_TYPE_SU[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 3:
                for i in range(len(PLC_Data.XEC)):
                    if PLC_Data.XEC[i] == memory:
                        memory_sel = i
                        break
                data = PLC_Data.XEC_TYPE_E[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
        elif mainWindow.Comm_Product_C.currentIndex() == 5:
            for i in range(len(PLC_Data.MASTER_K)):
                if PLC_Data.MASTER_K[i] == memory:
                    memory_sel = i
                    break
            if mainWindow.Comm_Product_S_Name.currentIndex() == 0:
                data = PLC_Data.MASTER_K120S[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 1:
                data = PLC_Data.MASTER_K200S[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 2:
                data = PLC_Data.MASTER_K300S[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 3:
                data = PLC_Data.MASTER_K10S1[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 4:
                data = PLC_Data.MASTER_K80S[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 5:
                data = PLC_Data.MASTER_K1000S[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 6:
                data = PLC_Data.MASTER_K10S[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 7:
                data = PLC_Data.MASTER_K30S[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 8:
                data = PLC_Data.MASTER_K60S[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
        elif mainWindow.Comm_Product_C.currentIndex() == 6:
            for i in range(len(PLC_Data.GLOFA)):
                if PLC_Data.GLOFA[i] == memory:
                    memory_sel = i
                    break
            if mainWindow.Comm_Product_S_Name.currentIndex() == 0:
                data = PLC_Data.GLOFA_GM1[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 1:
                data = PLC_Data.GLOFA_GM2[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 2:
                data = PLC_Data.GLOFA_GM3[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 3:
                data = PLC_Data.GLOFA_GM4[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 4:
                data = PLC_Data.GLOFA_GM4B[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 5:
                data = PLC_Data.GLOFA_GM4C[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 6:
                data = PLC_Data.GLOFA_GM6[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 7:
                data = PLC_Data.GLOFA_GM7U[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
            elif mainWindow.Comm_Product_S_Name.currentIndex() == 8:
                data = PLC_Data.GLOFA_GMR[memory_sel]
                if end > data:
                    return [data // 1000, data % 1000]
        elif mainWindow.Comm_Product_C.currentIndex() == 7:
            for i in range(len(PLC_Data.XGS)):
                if PLC_Data.XGS[i] == memory:
                    memory_sel = i
                    break
            data = PLC_Data.XGS_01[memory_sel]
            if end > data:
                return [data // 1000, data % 1000]
    return [0, 0]


def glofa_ethernet_data_read(start, end, memory):
    range_data = ((end // 1000) + 1) - (start // 1000)
    for a in range(range_data):
        """return_data, bytearray[1000] data"""
        mainWindow.main_data = mainWindow.main_data.astype('uint8')
        return_data = mainWindow.glofa_get_ethernet_data(memory, (a + (start // 1000)) * 1000, a + 1)
        if return_data != 0:
            for b in range(len(return_data)):
                aa = ((a + (start // 1000)) * 100) + ((b // 10) % 100)
                ab = b % 10
                print(str(aa) + ", " + str(ab) + ", " + str(return_data[b]))
                mainWindow.main_data[aa][ab] = return_data[b]
        else:
            for b in range(len(return_data)):
                mainWindow.main_data[((start // 1000) * 1000) + ((b // 100) % 100)][b % 10] = "???"


def xgi_ethernet_data_read(start, end, memory):
    range_data = ((end // 1000) + 1) - (start // 1000)
    for a in range(range_data):
        """return_data, bytearray[1000] data"""
        mainWindow.main_data = mainWindow.main_data.astype('uint8')
        return_data = mainWindow.xgi_get_ethernet_data(memory, (a + (start // 1000)) * 1000, a + 1)
        if return_data != 0:
            for b in range(len(return_data)):
                aa = ((a + (start // 1000)) * 100) + ((b // 10) % 100)
                ab = b % 10
                print(str(aa) + ", " + str(ab) + ", " + str(return_data[b]))
                mainWindow.main_data[aa][ab] = return_data[b]
        else:
            for b in range(len(return_data)):
                mainWindow.main_data[((start // 1000) * 1000) + ((b // 100) % 100)][b % 10] = "???"


def xgi_serial_data_read(start, end, memory):
    range_data = ((end // 100) + 1) - (start // 100)
    for a in range(range_data):
        """return_data, bytearray[100] data"""
        mainWindow.main_data = mainWindow.main_data.astype('uint8')
        return_data = mainWindow.xgi_get_serial_data(memory, a * 100)
        if return_data != 0:
            for b in range(len(return_data)):
                aa = (a * 10) + ((b // 10) % 10)
                ab = b % 10
                mainWindow.main_data[aa][ab] = return_data[b]
        else:
            for b in range(len(return_data)):
                mainWindow.main_data[((start // 100) * 100) + ((b // 10) % 10)][b % 10] = "???"


class WindowClass(QMainWindow, form_class):
    COM = 0
    ETHERNET = 1

    font = None

    main_data = np.zeros((50000, 10), dtype=np.int8)
    IP_Sel = 0
    main_data_load_start = 0
    main_data_load_end = 1000
    main_data_load_memory = "M"

    appearanceDataSize = DataSize.BYTE
    appearanceDataType = DataType.INT
    ConnectionType = 0
    ETOS = ["ETOS PD", "ETOS RD", "ETOS XPD"]
    ETOS_PD = ["GLOFA MODE"]
    ETOS_RD = ["GLOFA MODE"]
    ETOS_XPD = ["GLOFA MODE"]

    LSPLC = ["XGI", "XGR", "XGK", "XGB(XBC)", "XGB(XEC)", "MASTER-K", "GLOFA-GM", "XGS"]
    LSPLC_XGI = ["XGI-CPUUN", "XGI-CPUU", "XGI-CPUH", "XGI-CPUS", "XGI-CPUE"]
    LSPLC_XGK = ["XGK-CPUUN", "XGK-CPUHN", "XGK-CPUSN", "XGK-CPUU", "XGK-CPUH", "XGK-CPUA", "XGK-CPUS", "XGK-CPUE"]
    LSPLC_XGR = ["XGR-CPUH/T", "XGR-CPUH/F", "XGR-CPUH/S"]
    LSPLC_XBC = ["XBC U TYPE", "XBC H TYPE", "XBC SU TYPE", "XBC E TYPE", "XBM Slim"]
    LSPLC_XEC = ["XEC U TYPE", "XEC H TYPE", "XEC SU TYPE", "XEC E TYPE"]
    LSPLC_MASTERK = ["K120S", "K200S", "K300S", "K10S1", "K80S", "K1000S", "K10S", "K30S", "K60S"]
    LSPLC_GLOFA = ["GM1", "GM2", "GM3", "GM4-CPUA", "GM4-CPUB", "GM4-CPUC", "GM6", "GM7U", "GMR"]
    LSPLC_XGS = ["CPU01A"]
    serial = serial.Serial
    socket = socket.socket

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.font = self.dataTable.font()
        self.font.setFamily('NotoSansKR')
        self.font.setPointSize(9)
        self.dataTable.setFont(self.font)
        self.port_refresh()
        self.Comm_Product_C.addItems(self.ETOS)
        self.Comm_Product_S_Name.addItems(self.ETOS_PD)
        self.DataSel_Float.setEnabled(False)
        self.button_menu_refresh_function()
        self.button_menu_refresh_function_2()

        self.IP_1.textChanged.connect(self.ip_1)
        self.IP_2.textChanged.connect(self.ip_2)
        self.IP_3.textChanged.connect(self.ip_3)
        self.IP_4.textChanged.connect(self.ip_4)

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

        self.memoryTree.itemDoubleClicked.connect(self.memory_tree_function)

    # noinspection PyTypeChecker
    def memory_tree_viewer(self):
        self.dataTable.clear()
        self.dataTable.setColumnCount(10)
        vertical_header_labels = data_structure_maker.memory_data_builder(self.main_data_load_memory,
                                                                          self.appearanceDataSize,
                                                                          self.main_data_load_start,
                                                                          self.main_data_load_end)
        self.dataTable.setHorizontalHeaderLabels(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

        if self.appearanceDataSize == DataSize.BIT:
            a = ((self.main_data_load_end - self.main_data_load_start) // 10) + 1
            b = ((((self.main_data_load_end - self.main_data_load_start) // 10) + 1) * 8)

            temp_data = [[[i for i in range(8)] for _ in range(10)] for _ in range(a)]
            self.dataTable.setRowCount(b)
            self.dataTable.setVerticalHeaderLabels(vertical_header_labels)
            for i in range(a):
                for j in range(10):
                    try:
                        data = self.main_data[i][j]
                        arr = bitarray(endian='big')
                        arr.frombytes(bytes(chr(data), "latin-1"))
                        for k in range(8):
                            if arr[k]:
                                # noinspection PyTypeChecker
                                temp_data[i][j][k] = "1"
                            else:
                                temp_data[i][j][k] = "0"
                    except Exception as e:
                        print(e)
                        for k in range(8):
                            temp_data[i][j][k] = "?"
            np_data = np.array(temp_data)
            np_return = np_data.ravel()
            print(np_return)
            data_size = 0
            for i in range(b):
                for j in range(10):
                    try:
                        item = QTableWidgetItem(str(np_return[data_size]))
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.dataTable.setItem(i, j, item)
                        data_size = data_size + 1
                    except Exception as e:
                        print(e)
                        item = QTableWidgetItem("?")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.dataTable.setItem(i, j, item)
                        data_size = data_size + 1
        elif self.appearanceDataSize == DataSize.BYTE:
            a = ((self.main_data_load_end - self.main_data_load_start) // 10) + 1

            self.dataTable.setRowCount(a)
            self.dataTable.setVerticalHeaderLabels(vertical_header_labels)
            if self.appearanceDataType == DataType.BINARY:
                self.main_data = self.main_data.astype('uint8')
                for i in range(a):
                    for j in range(10):
                        try:
                            data = self.main_data[i][j]
                            arr = bitarray(endian='big')
                            arr.frombytes(bytes(chr(data), "latin-1"))
                            item = QTableWidgetItem(str(arr)[10:18])
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.BCD:
                self.main_data = self.main_data.astype('uint8')
                for i in range(a):
                    for j in range(10):
                        try:
                            data = self.main_data[i][j]
                            item = QTableWidgetItem(str(hex(data)))[2:]
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.UINT:
                self.main_data = self.main_data.astype('uint8')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(str(self.main_data[i][j]))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.INT:
                self.main_data = self.main_data.astype('int8')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(str(self.main_data[i][j]))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.HEX:
                self.main_data = self.main_data.astype('uint8')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(str(hex(self.main_data[i][j]))[2:])
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.STRING:
                self.main_data = self.main_data.astype('uint8')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(chr(self.main_data[i][j]))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
        elif self.appearanceDataSize == DataSize.WORD:
            a = ((self.main_data_load_end - self.main_data_load_start) // 20) + 1
            self.dataTable.setRowCount(a)
            self.dataTable.setVerticalHeaderLabels(vertical_header_labels)
            data = np.zeros((a, 10), np.uint16)
            for i in range(a):
                for j in range(10):
                    if j < 5:
                        try:
                            data[i][j] = self.main_data[i * 2][j * 2] + (self.main_data[i * 2][j * 2 + 1] * 256)
                        except Exception as e:
                            print(e)
                            data[i][j] = 0
                    else:
                        try:
                            data[i][j] = self.main_data[(i * 2) + 1][(j % 5) * 2] \
                                         + (self.main_data[(i * 2) + 1][(j % 5) * 2 + 1] * 256)
                        except Exception as e:
                            print(e)
                            data[i][j] = 0

            if self.appearanceDataType == DataType.BINARY:
                data = data.astype('uint16')
                for i in range(a):
                    for j in range(10):
                        try:
                            data_a = data[i][j]
                            arr = bitarray(endian='big')
                            arr.frombytes(int(data_a).to_bytes(2, byteorder="big"))
                            item = QTableWidgetItem(str(arr)[10:26])
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.BCD:
                data = data.astype('uint16')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(str(hex(data)))[2:]
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.UINT:
                data = data.astype('uint16')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(str(data[i][j]))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.INT:
                data = data.astype('int16')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(str(data[i][j]))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.HEX:
                data = data.astype('uint16')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(str(hex(data[i][j]))[2:])
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.STRING:
                data = data.astype('uint16')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(int(data[i][j]).to_bytes(2, byteorder="little").decode("latin-1"))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
        elif self.appearanceDataSize == DataSize.DWORD:
            temp_a = ((self.main_data_load_end - self.main_data_load_start) // 20) + 1
            a = ((self.main_data_load_end - self.main_data_load_start) // 40) + 1
            self.dataTable.setRowCount(a)
            self.dataTable.setVerticalHeaderLabels(vertical_header_labels)
            temp_data = np.zeros((temp_a, 10), np.uint16)
            data = np.zeros((a, 10), np.uint32)
            for i in range(temp_a):
                for j in range(10):
                    if j < 5:
                        try:
                            temp_data[i][j] = self.main_data[i * 2][j * 2] + (self.main_data[i * 2][j * 2 + 1] * 256)
                        except Exception as e:
                            print(e)
                            temp_data[i][j] = 0
                    else:
                        try:
                            temp_data[i][j] = self.main_data[(i * 2) + 1][(j % 5) * 2] \
                                         + (self.main_data[(i * 2) + 1][(j % 5) * 2 + 1] * 256)
                        except Exception as e:
                            print(e)
                            temp_data[i][j] = 0
            for i in range(a):
                for j in range(10):
                    if j < 5:
                        try:
                            data[i][j] = temp_data[i * 2][j * 2] + (temp_data[i * 2][j * 2 + 1] * 65536)
                        except Exception as e:
                            print(e)
                            data[i][j] = 0
                    else:
                        try:
                            data[i][j] = temp_data[(i * 2) + 1][(j % 5) * 2] \
                                         + (temp_data[(i * 2) + 1][(j % 5) * 2 + 1] * 65536)
                        except Exception as e:
                            print(e)
                            data[i][j] = 0
            if self.appearanceDataType == DataType.BINARY:
                data = data.astype('uint32')
                for i in range(a):
                    for j in range(10):
                        try:
                            data_a = data[i][j]
                            arr = bitarray(endian='big')
                            arr.frombytes(int(data_a).to_bytes(4, byteorder="big"))
                            item = QTableWidgetItem(str(arr)[10:42])
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.BCD:
                data = data.astype('uint32')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(str(hex(data[i][j]))[2:])
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.INT:
                data = data.astype('int32')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(str(data[i][j]))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.UINT:
                data = data.astype('uint32')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(str(data[i][j]))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.HEX:
                data = data.astype('uint32')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(str(hex(data[i][j]))[2:])
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.FLOAT:
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(
                                str(struct.unpack('f', int(data[i][j]).to_bytes(4, byteorder="little"))[0]))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.STRING:
                data = data.astype('uint32')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(
                                int(data[i][j]).to_bytes(4, byteorder="little").decode("latin-1"))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
        elif self.appearanceDataSize == DataSize.LWORD:
            temp_a = ((self.main_data_load_end - self.main_data_load_start) // 20) + 1
            temp_b = ((self.main_data_load_end - self.main_data_load_start) // 40) + 1
            a = ((self.main_data_load_end - self.main_data_load_start) // 80) + 1
            self.dataTable.setRowCount(a)
            self.dataTable.setVerticalHeaderLabels(vertical_header_labels)
            temp_data = np.zeros((temp_a, 10), np.uint16)
            temp_data2 = np.zeros((temp_b, 10), np.uint32)
            data = np.zeros((a, 10), np.uint64)
            for i in range(temp_a):
                for j in range(10):
                    if j < 5:
                        try:
                            temp_data[i][j] = self.main_data[i * 2][j * 2] + (self.main_data[i * 2][j * 2 + 1] * 256)
                        except Exception as e:
                            print(e)
                            temp_data[i][j] = 0
                    else:
                        try:
                            temp_data[i][j] = self.main_data[(i * 2) + 1][(j % 5) * 2] \
                                              + (self.main_data[(i * 2) + 1][(j % 5) * 2 + 1] * 256)
                        except Exception as e:
                            print(e)
                            temp_data[i][j] = 0
            for i in range(temp_b):
                for j in range(10):
                    if j < 5:
                        try:
                            temp_data2[i][j] = temp_data[i * 2][j * 2] + (temp_data[i * 2][j * 2 + 1] * 65536)
                        except Exception as e:
                            print(e)
                            temp_data2[i][j] = 0
                    else:
                        try:
                            temp_data2[i][j] = temp_data[(i * 2) + 1][(j % 5) * 2] \
                                         + (temp_data[(i * 2) + 1][(j % 5) * 2 + 1] * 65536)
                        except Exception as e:
                            print(e)
                            temp_data2[i][j] = 0
            for i in range(a):
                for j in range(10):
                    if j < 5:
                        try:
                            data[i][j] = temp_data2[i * 2][j * 2] + (temp_data2[i * 2][j * 2 + 1] * 16777216)
                        except Exception as e:
                            print(e)
                            data[i][j] = 0
                    else:
                        try:
                            data[i][j] = temp_data2[(i * 2) + 1][(j % 5) * 2] \
                                         + (temp_data2[(i * 2) + 1][(j % 5) * 2 + 1] * 16777216)
                        except Exception as e:
                            print(e)
                            data[i][j] = 0
            if self.appearanceDataType == DataType.BINARY:
                data = data.astype('uint64')
                for i in range(a):
                    for j in range(10):
                        try:
                            data_a = data[i][j]
                            arr = bitarray(endian='big')
                            arr.frombytes(int(data_a).to_bytes(8, byteorder="big"))
                            item = QTableWidgetItem(str(arr)[10:74])
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.BCD:
                data = data.astype('uint64')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(str(hex(data[i][j]))[2:])
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.INT:
                data = data.astype('int64')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(str(data[i][j]))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.UINT:
                data = data.astype('uint64')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(str(data[i][j]))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.HEX:
                data = data.astype('uint64')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(str(hex(data[i][j]))[2:])
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.FLOAT:
                data = data.astype('uint64')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(
                                str(struct.unpack('d', int(data[i][j]).to_bytes(8, byteorder="little"))[0]))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
            elif self.appearanceDataType == DataType.STRING:
                data = data.astype('uint64')
                for i in range(a):
                    for j in range(10):
                        try:
                            item = QTableWidgetItem(int(data[i][j]).to_bytes(8, byteorder="little").decode("latin-1"))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
                        except Exception as e:
                            print(e)
                            item = QTableWidgetItem("?")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.dataTable.setItem(i, j, item)
        self.dataTable.repaint()
        self.repaint()

    def memory_tree_function(self):
        pass

    def commsel_comm_product(self):
        if self.Comm_Product.currentIndex() == 0:
            self.Comm_Product_C.clear()
            self.Comm_Product_C.addItems(self.ETOS)
        elif self.Comm_Product.currentIndex() == 1:
            self.Comm_Product_C.clear()
            self.Comm_Product_C.addItems(self.LSPLC)

    def commsel_comm_product_c(self):
        if self.Comm_Product.currentIndex() == 0:
            self.Comm_Product_S_Name.clear()
            if self.Comm_Product_C.currentIndex() == 0:
                self.Comm_Product_S_Name.addItems(self.ETOS_PD)
            elif self.Comm_Product_C.currentIndex() == 1:
                self.Comm_Product_S_Name.addItems(self.ETOS_RD)
            elif self.Comm_Product_C.currentIndex() == 2:
                self.Comm_Product_S_Name.addItems(self.ETOS_XPD)
        elif self.Comm_Product.currentIndex() == 1:
            self.Comm_Product_S_Name.clear()
            if self.Comm_Product_C.currentIndex() == 0:
                self.Comm_Product_S_Name.addItems(self.LSPLC_XGI)
            elif self.Comm_Product_C.currentIndex() == 1:
                self.Comm_Product_S_Name.addItems(self.LSPLC_XGR)
            elif self.Comm_Product_C.currentIndex() == 2:
                self.Comm_Product_S_Name.addItems(self.LSPLC_XGK)
            elif self.Comm_Product_C.currentIndex() == 3:
                self.Comm_Product_S_Name.addItems(self.LSPLC_XBC)
            elif self.Comm_Product_C.currentIndex() == 4:
                self.Comm_Product_S_Name.addItems(self.LSPLC_XEC)
            elif self.Comm_Product_C.currentIndex() == 5:
                self.Comm_Product_S_Name.addItems(self.LSPLC_MASTERK)
            elif self.Comm_Product_C.currentIndex() == 6:
                self.Comm_Product_S_Name.addItems(self.LSPLC_GLOFA)
            elif self.Comm_Product_C.currentIndex() == 7:
                self.Comm_Product_S_Name.addItems(self.LSPLC_XGS)

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

    def ip_1(self):
        if len(self.IP_1.text()) > 0:
            if self.IP_1.text()[-1] == ".":
                pyautogui.press('tab')
            if len(self.IP_1.text()) > 3:
                self.IP_1.backspace()
            if not(self.IP_1.text().isdecimal()):
                self.IP_1.backspace()
            if (self.IP_1.cursorPosition() == 3) & (len(self.IP_1.text()) == 3):
                pyautogui.press('tab')

    def ip_2(self):
        if len(self.IP_2.text()) > 0:
            if self.IP_2.text()[-1] == ".":
                pyautogui.press('tab')
            if len(self.IP_2.text()) > 3:
                self.IP_2.backspace()
            if not(self.IP_2.text().isdecimal()):
                self.IP_2.backspace()
            if (self.IP_2.cursorPosition() == 3) & (len(self.IP_2.text()) == 3):
                pyautogui.press('tab')

    def ip_3(self):
        if len(self.IP_3.text()) > 0:
            if self.IP_3.text()[-1] == ".":
                pyautogui.press('tab')
            if len(self.IP_3.text()) > 3:
                self.IP_3.backspace()
            if not(self.IP_3.text().isdecimal()):
                self.IP_3.backspace()
            if (self.IP_3.cursorPosition() == 3) & (len(self.IP_3.text()) == 3):
                pyautogui.press('tab')

    def ip_4(self):
        if len(self.IP_4.text()) > 0:
            if self.IP_4.text()[-1] == ".":
                pyautogui.press('tab')
            if not(self.IP_4.text().isdecimal()):
                self.IP_4.backspace()

    def bitsel_bit_function(self):
        self.appearanceDataSize = DataSize.BIT
        if not self.DataSel_Binary.isChecked():
            self.appearanceDataType = DataType.BINARY
            self.button_menu_refresh_function_2()
        self.DataSel_BCD.setEnabled(False)
        self.DataSel_Int.setEnabled(False)
        self.DataSel_UInt.setEnabled(False)
        self.DataSel_HEX.setEnabled(False)
        self.DataSel_Float.setEnabled(False)
        self.DataSel_String.setEnabled(False)
        self.button_menu_refresh_function()
        self.memory_tree_viewer()

    def bitsel_byte_function(self):
        self.appearanceDataSize = DataSize.BYTE
        if self.DataSel_Float.setChecked:
            self.appearanceDataType = DataType.INT
            self.button_menu_refresh_function_2()
        self.DataSel_BCD.setEnabled(True)
        self.DataSel_Int.setEnabled(True)
        self.DataSel_UInt.setEnabled(True)
        self.DataSel_HEX.setEnabled(True)
        self.DataSel_Float.setEnabled(False)
        self.DataSel_String.setEnabled(True)
        self.button_menu_refresh_function()
        self.memory_tree_viewer()

    def bitsel_word_function(self):
        self.appearanceDataSize = DataSize.WORD
        if self.DataSel_Float.setChecked:
            self.appearanceDataType = DataType.INT
            self.button_menu_refresh_function_2()
        self.DataSel_BCD.setEnabled(True)
        self.DataSel_Int.setEnabled(True)
        self.DataSel_UInt.setEnabled(True)
        self.DataSel_HEX.setEnabled(True)
        self.DataSel_Float.setEnabled(False)
        self.DataSel_String.setEnabled(True)
        self.button_menu_refresh_function()
        self.memory_tree_viewer()

    def bitsel_dword_function(self):
        self.appearanceDataSize = DataSize.DWORD
        self.DataSel_BCD.setEnabled(True)
        self.DataSel_Int.setEnabled(True)
        self.DataSel_UInt.setEnabled(True)
        self.DataSel_HEX.setEnabled(True)
        self.DataSel_Float.setEnabled(True)
        self.DataSel_String.setEnabled(True)
        self.button_menu_refresh_function()
        self.memory_tree_viewer()

    def bitsel_lword_function(self):
        self.appearanceDataSize = DataSize.LWORD
        self.DataSel_BCD.setEnabled(True)
        self.DataSel_Int.setEnabled(True)
        self.DataSel_UInt.setEnabled(True)
        self.DataSel_HEX.setEnabled(True)
        self.DataSel_Float.setEnabled(True)
        self.DataSel_String.setEnabled(True)
        self.button_menu_refresh_function()
        self.memory_tree_viewer()

    def datasel_binary_function(self):
        self.appearanceDataType = DataType.BINARY
        self.button_menu_refresh_function_2()
        self.memory_tree_viewer()

    def datasel_bcd_function(self):
        self.appearanceDataType = DataType.BCD
        self.button_menu_refresh_function_2()
        self.memory_tree_viewer()

    def datasel_int_function(self):
        self.appearanceDataType = DataType.INT
        self.button_menu_refresh_function_2()
        self.memory_tree_viewer()

    def datasel_uint_function(self):
        self.appearanceDataType = DataType.UINT
        self.button_menu_refresh_function_2()
        self.memory_tree_viewer()

    def datasel_hex_function(self):
        self.appearanceDataType = DataType.HEX
        self.button_menu_refresh_function_2()
        self.memory_tree_viewer()

    def datasel_float_function(self):
        self.appearanceDataType = DataType.FLOAT
        self.button_menu_refresh_function_2()
        self.memory_tree_viewer()

    def datasel_string_function(self):
        self.appearanceDataType = DataType.STRING
        self.button_menu_refresh_function_2()
        self.memory_tree_viewer()

    def fontsel_font_up_function(self):
        self.font.setPointSize(self.font.pointSize() + 1)
        self.dataTable.setFont(self.font)
        self.repaint()

    def fontsel_font_down_function(self):
        self.font.setPointSize(self.font.pointSize() - 1)
        self.dataTable.setFont(self.font)
        self.repaint()

    def comm_connect_memory_function(self):
        if self.Comm_Product.currentIndex() == 0:
            if self.Comm_Product_C.currentIndex() == 0:
                self.memoryTree.clear()
                top = QTreeWidgetItem(self.memoryTree)
                top.setText(0, self.Comm_Product_S_Name.currentText())
                a = [QTreeWidgetItem(top) for _ in range(len(PLC_Data.ETOSPD))]
                for i in range(len(PLC_Data.ETOSPD)):
                    a[i].setText(0, PLC_Data.ETOSPD[i])
            elif self.Comm_Product_C.currentIndex() == 1:
                self.memoryTree.clear()
                top = QTreeWidgetItem(self.memoryTree)
                top.setText(0, self.Comm_Product_S_Name.currentText())
                a = [QTreeWidgetItem(top) for _ in range(len(PLC_Data.ETOSRD))]
                for i in range(len(PLC_Data.ETOSRD)):
                    a[i].setText(0, PLC_Data.ETOSRD[i])
            elif self.Comm_Product_C.currentIndex() == 2:
                self.memoryTree.clear()
                top = QTreeWidgetItem(self.memoryTree)
                top.setText(0, self.Comm_Product_S_Name.currentText())
                a = [QTreeWidgetItem(top) for _ in range(len(PLC_Data.ETOSXPD))]
                for i in range(len(PLC_Data.ETOSXPD)):
                    a[i].setText(0, PLC_Data.ETOSXPD[i])
        elif self.Comm_Product.currentIndex() == 1:
            if self.Comm_Product_C.currentIndex() == 0:
                """XGI"""
                self.memoryTree.clear()
                top = QTreeWidgetItem(self.memoryTree)
                top.setText(0, self.Comm_Product_S_Name.currentText())
                a = [QTreeWidgetItem(top) for _ in range(len(PLC_Data.XGI))]
                for i in range(len(PLC_Data.XGI)):
                    a[i].setText(0, PLC_Data.XGI[i])
            elif self.Comm_Product_C.currentIndex() == 1:
                """XGR"""
                self.memoryTree.clear()
                top = QTreeWidgetItem(self.memoryTree)
                top.setText(0, self.Comm_Product_S_Name.currentText())
                a = [QTreeWidgetItem(top) for _ in range(len(PLC_Data.XGI))]
                for i in range(len(PLC_Data.XGI)):
                    a[i].setText(0, PLC_Data.XGI[i])
            elif self.Comm_Product_C.currentIndex() == 2:
                """XGK"""
                self.memoryTree.clear()
                top = QTreeWidgetItem(self.memoryTree)
                top.setText(0, self.Comm_Product_S_Name.currentText())
                a = [QTreeWidgetItem(top) for _ in range(len(PLC_Data.XGK))]
                for i in range(len(PLC_Data.XGK)):
                    a[i].setText(0, PLC_Data.XGK[i])
            elif self.Comm_Product_C.currentIndex() == 3:
                """XGB(XBC)"""
                self.memoryTree.clear()
                if (self.Comm_Product_S_Name.currentIndex() == 0) | (self.Comm_Product_S_Name.currentIndex() == 1):
                    """U TYPE, H TYPE"""
                    top = QTreeWidgetItem(self.memoryTree)
                    top.setText(0, self.Comm_Product_S_Name.currentText())
                    a = [QTreeWidgetItem(top) for _ in range(len(PLC_Data.XGK))]
                    for i in range(len(PLC_Data.XGK)):
                        a[i].setText(0, PLC_Data.XGK[i])
                elif self.Comm_Product_S_Name.currentIndex() == 2:
                    """SU TYPE"""
                    top = QTreeWidgetItem(self.memoryTree)
                    top.setText(0, self.Comm_Product_S_Name.currentText())
                    a = [QTreeWidgetItem(top) for _ in range(len(PLC_Data.XBC_SU))]
                    for i in range(len(PLC_Data.XBC_SU)):
                        a[i].setText(0, PLC_Data.XBC_SU[i])
                elif self.Comm_Product_S_Name.currentIndex() == 3:
                    """E TYPE"""
                    top = QTreeWidgetItem(self.memoryTree)
                    top.setText(0, self.Comm_Product_S_Name.currentText())
                    a = [QTreeWidgetItem(top) for _ in range(len(PLC_Data.XBC_E))]
                    for i in range(len(PLC_Data.XBC_E)):
                        a[i].setText(0, PLC_Data.XBC_E[i])
                elif self.Comm_Product_S_Name.currentIndex() == 4:
                    """Slim"""
                    top = QTreeWidgetItem(self.memoryTree)
                    top.setText(0, self.Comm_Product_S_Name.currentText())
                    a = [QTreeWidgetItem(top) for _ in range(len(PLC_Data.XBM_SILM))]
                    for i in range(len(PLC_Data.XBM_SILM)):
                        a[i].setText(0, PLC_Data.XBM_SILM[i])
            elif self.Comm_Product_C.currentIndex() == 4:
                """XGB(XEC)"""
                self.memoryTree.clear()
                if (self.Comm_Product_S_Name.currentIndex() == 0) | (self.Comm_Product_S_Name.currentIndex() == 1):
                    """U TYPE, "H TYPE"""
                    top = QTreeWidgetItem(self.memoryTree)
                    top.setText(0, self.Comm_Product_S_Name.currentText())
                    a = [QTreeWidgetItem(top) for _ in range(len(PLC_Data.XEC))]
                    for i in range(len(PLC_Data.XEC)):
                        a[i].setText(0, PLC_Data.XEC[i])
                elif (self.Comm_Product_S_Name.currentIndex() == 2) | (self.Comm_Product_S_Name.currentIndex() == 3):
                    """SU TYPE, E TYPE"""
                    top = QTreeWidgetItem(self.memoryTree)
                    top.setText(0, self.Comm_Product_S_Name.currentText())
                    a = [QTreeWidgetItem(top) for _ in range(len(PLC_Data.XGK))]
                    for i in range(len(PLC_Data.XGK)):
                        a[i].setText(0, PLC_Data.XGK[i])
            elif self.Comm_Product_C.currentIndex() == 5:
                """MASTERK"""
                self.memoryTree.clear()
                top = QTreeWidgetItem(self.memoryTree)
                top.setText(0, self.Comm_Product_S_Name.currentText())
                a = [QTreeWidgetItem(top) for _ in range(len(PLC_Data.GLOFA))]
                for i in range(len(PLC_Data.GLOFA)):
                    a[i].setText(0, PLC_Data.GLOFA[i])
            elif self.Comm_Product_C.currentIndex() == 6:
                """GLOFA"""
                self.memoryTree.clear()
                top = QTreeWidgetItem(self.memoryTree)
                top.setText(0, self.Comm_Product_S_Name.currentText())
                a = [QTreeWidgetItem(top) for _ in range(len(PLC_Data.GLOFA))]
                for i in range(len(PLC_Data.GLOFA)):
                    a[i].setText(0, PLC_Data.GLOFA[i])
            elif self.Comm_Product_C.currentIndex() == 7:
                """XGS"""
                pass

    def comm_connect(self):
        if self.ConnectionType == self.COM:
            try:
                self.serial = serial.Serial(self.CommSel_Comport.currentText(), 9600, timeout=0)
            except serial.serialutil.SerialException:
                pass
            except ValueError:
                return 1
        elif self.ConnectionType == self.ETHERNET:
            try:
                self.serial = serial.serial_for_url("socket://" +
                                                    self.IP_1.text() + "." +
                                                    self.IP_2.text() + "." +
                                                    self.IP_3.text() + "." +
                                                    self.IP_4.text() + ":2004")
            except ValueError:
                return 101
            except serialutil.SerialException:
                return 102
        return 0

    def comm_connect_function(self):
        b = self.comm_connect()
        if b == 0:
            mainWindow.statusBar.showMessage("온라인, 접속 완료")
            self.search_start_memory.setText("%MB0")
            self.search_end_memory.setText("%MB999")
            self.serial.close()
        else:
            mainWindow.statusBar.showMessage("오프라인, 접속 대기중")

    def glofa_get_ethernet_data(self, memory, address, block):
        b = self.comm_connect()
        send_packet = self.glofa_ethernet_packet_maker(memory, address, block)
        receive_packet = bytearray()
        self.serial.write(send_packet)
        read_header = False
        read_start = False
        header = bytearray()
        header_count = 0
        count = 0
        while True:
            if read_start:
                raw_data = self.serial.read()
                if count > 12:
                    receive_packet.append(int.from_bytes(raw_data, "big"))
                count = count + 1
                if count > 1012:
                    break
            else:
                try:
                    temp = self.serial.read()
                    if read_header:
                        header.append(int.from_bytes(temp, "big"))
                        header_count = header_count + 1
                        if header_count == 20:
                            read_start = True
                    if temp == bytes([76]):
                        read_header = True
                        header.append(int.from_bytes(temp, "big"))
                        header_count = header_count + 1
                except serial.serialutil.SerialException as e:
                    print(e)
                    self.serial.close()
                    return 1
        self.serial.close()
        return receive_packet

    def xgi_get_ethernet_data(self, memory, address, block):
        b = self.comm_connect()
        send_packet = self.xgi_ethernet_packet_maker(memory, address, block)
        receive_packet = bytearray()
        self.serial.write(send_packet)
        read_header = False
        read_start = False
        header = bytearray()
        header_count = 0
        count = 0
        while True:
            if read_start:
                raw_data = self.serial.read()
                if count > 11:
                    receive_packet.append(int.from_bytes(raw_data, "big"))
                count = count + 1
                if count > 1011:
                    break
            else:
                try:
                    temp = self.serial.read()
                    if read_header:
                        header.append(int.from_bytes(temp, "big"))
                        header_count = header_count + 1
                        if header_count == 20:
                            read_start = True
                    if temp == bytes([76]):
                        read_header = True
                        header.append(int.from_bytes(temp, "big"))
                        header_count = header_count + 1
                except serial.serialutil.SerialException as e:
                    print(e)
                    self.serial.close()
                    return 1
        self.serial.close()
        return receive_packet

    def xgi_get_serial_data(self, memory, address):
        b = self.comm_connect()
        receive_packet = bytearray()
        if b == 0:
            send_packet = self.xgi_serial_packet_maker(memory, address)
            self.serial.write(send_packet)
            read_header = False
            read_start = False
            is_msb = True
            msb = ""
            while True:
                if read_start:
                    raw_data = self.serial.read()
                    if raw_data == bytes():
                        continue
                    if raw_data == bytes([3]):
                        break
                    if is_msb:
                        msb = str(raw_data)[-2:-1]
                        is_msb = False
                    else:
                        lsb = str(raw_data)[-2:-1]
                        is_msb = True
                        receive_packet.append(int(str(msb + lsb), 16))
                else:
                    try:
                        temp = self.serial.read()
                        if read_header:
                            if temp == bytes([52]):
                                read_start = True
                        if temp == bytes([6]):
                            read_header = True
                    except serial.serialutil.SerialException as e:
                        print(e)
                        self.serial.close()
                        return 1
        self.serial.close()
        return receive_packet

    def search_memory_function(self):
        start_memory = str(self.search_start_memory.text())
        end_memory = str(self.search_end_memory.text())
        if self.Comm_Product.currentIndex() == 0:
            if self.ConnectionType == self.COM:
                if (self.Comm_Product_C.currentIndex() == 0) | \
                        (self.Comm_Product_C.currentIndex() == 1) | \
                        (self.Comm_Product_C.currentIndex() == 2):
                    if self.Comm_Product_S_Name.currentIndex() == 0:
                        c = self.xec_search(start_memory, end_memory)
                        if c != 1:
                            try:
                                xgi_serial_data_read(self.main_data_load_start,
                                                     self.main_data_load_end,
                                                     self.main_data_load_memory)
                            except ValueError:
                                return 1
                    elif self.Comm_Product_S_Name.currentIndex() == 1:
                        pass
            elif self.ConnectionType == self.ETHERNET:
                if (self.Comm_Product_C.currentIndex() == 0) | \
                        (self.Comm_Product_C.currentIndex() == 1) | \
                        (self.Comm_Product_C.currentIndex() == 2):
                    if self.Comm_Product_S_Name.currentIndex() == 0:
                        c = self.xec_search(start_memory, end_memory)
                        if c != 1:
                            try:
                                glofa_ethernet_data_read(self.main_data_load_start,
                                                         self.main_data_load_end,
                                                         self.main_data_load_memory)
                            except ValueError:
                                return 1
                    elif self.Comm_Product_S_Name.currentIndex() == 1:
                        pass
        elif self.Comm_Product.currentIndex() == 1:
            if self.ConnectionType == self.COM:
                if (self.Comm_Product_C.currentIndex() == 0) | \
                        (self.Comm_Product_C.currentIndex() == 1) | \
                        (self.Comm_Product_C.currentIndex() == 4) | \
                        (self.Comm_Product_C.currentIndex() == 5) | \
                        (self.Comm_Product_C.currentIndex() == 6):
                    c = self.xec_search(start_memory, end_memory)
                    if c != 1:
                        try:
                            xgi_serial_data_read(self.main_data_load_start,
                                                 self.main_data_load_end,
                                                 self.main_data_load_memory)
                        except ValueError:
                            return 1
            elif self.ConnectionType == self.ETHERNET:
                if (self.Comm_Product_C.currentIndex() == 0) | \
                        (self.Comm_Product_C.currentIndex() == 1) | \
                        (self.Comm_Product_C.currentIndex() == 4):
                    c = self.xec_search(start_memory, end_memory)
                    if c != 1:
                        xgi_ethernet_data_read(self.main_data_load_start,
                                               self.main_data_load_end,
                                               self.main_data_load_memory)
                elif (self.Comm_Product_C.currentIndex() == 5) | \
                    (self.Comm_Product_C.currentIndex() == 6):
                    c = self.xec_search(start_memory, end_memory)
                    if c != 1:
                        glofa_ethernet_data_read(self.main_data_load_start,
                                                 self.main_data_load_end,
                                                 self.main_data_load_memory)

        self.memory_tree_viewer()
        self.comm_connect_memory_function()

    def xec_search(self, data1, data2):
        start_memory = bytearray(data1, encoding="latin-1")
        end_memory = bytearray(data2, encoding="latin-1")
        if start_memory[0] != 0x25:
            return 1
        if not(self.memory_checker(start_memory[1])):
            return 1
        if start_memory[2] == ord("X"):
            data = int(start_memory[3:])
            self.main_data_load_start = data // 8
        elif start_memory[2] == ord("B"):
            self.main_data_load_start = int(start_memory[3:])
        elif start_memory[2] == ord("W"):
            data = int(start_memory[3:])
            self.main_data_load_start = data * 2
        elif start_memory[2] == ord("D"):
            data = int(start_memory[3:])
            self.main_data_load_start = data * 4
        elif start_memory[2] == ord("L"):
            data = int(start_memory[3:])
            self.main_data_load_start = data * 8
        if end_memory[0] != 0x25:
            return 1
        if start_memory[1] != end_memory[1]:
            return 1
        else:
            self.main_data_load_memory = chr(start_memory[1])
        if end_memory[2] == ord("X"):
            data = int(end_memory[3:])
            self.main_data_load_end = data // 8
        elif end_memory[2] == ord("B"):
            self.main_data_load_end = int(end_memory[3:])
        elif end_memory[2] == ord("W"):
            data = int(end_memory[3:])
            self.main_data_load_end = data * 2
        elif end_memory[2] == ord("D"):
            data = int(end_memory[3:])
            self.main_data_load_end = data * 4
        elif end_memory[2] == ord("L"):
            data = int(end_memory[3:])
            self.main_data_load_end = data * 8
        if self.main_data_load_start > self.main_data_load_end:
            self.main_data_load_end = self.main_data_load_start + 999

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

    @staticmethod
    def glofa_ethernet_packet_maker(memory, address, block):
        application_header = bytearray("LGIS-GLOFA", encoding='latin-1')
        application_header.append(0x00)
        application_header.append(0x00)
        application_header.append(0x00)
        application_header.append(0x33)
        application_header.append(int(block))
        application_header.append(0x00)
        application_header.append(15 + len(str(address)))
        application_header.append(0x00)
        application_header.append(0x00)
        application_header.append(7 + len(str(address)))
        application_instruction = bytearray()
        application_instruction.append(0x54)
        application_instruction.append(0x00)
        application_instruction.append(0x14)
        application_instruction.append(0x00)
        application_instruction.append(0x00)
        application_instruction.append(0x00)
        application_instruction.append(0x01)
        application_instruction.append(0x00)
        application_instruction.append(3 + len(str(address)))
        application_instruction.append(0x00)
        application_instruction.append(0x25)
        application_instruction.append(bytearray(str(memory), encoding="latin-1")[0])
        application_instruction.append(0x42)
        application_instruction = application_instruction + bytearray(str(address), encoding="latin-1")
        application_instruction.append(0xE8)
        application_instruction.append(0x03)
        send_data_packet = application_header + application_instruction
        return send_data_packet

    @staticmethod
    def xgi_ethernet_packet_maker(memory, address, block):
        application_header = bytearray("LSIS-XGT", encoding='latin-1')
        application_header.append(0x00)
        application_header.append(0x00)
        application_header.append(0x00)
        application_header.append(0x00)
        application_header.append(0xA0)
        application_header.append(0x33)
        application_header.append(int(block))
        application_header.append(0x00)
        application_header.append(15 + len(str(address)))
        application_header.append(0x00)
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
        application_instruction.append(3 + len(str(address)))
        application_instruction.append(0x00)
        application_instruction.append(0x25)
        application_instruction.append(bytearray(str(memory), encoding="latin-1")[0])
        application_instruction.append(0x42)
        application_instruction = application_instruction + bytearray(str(address), encoding="latin-1")
        application_instruction.append(0xE8)
        application_instruction.append(0x03)
        send_data_packet = application_header + application_instruction
        return send_data_packet

    @staticmethod
    def xgi_serial_packet_maker(memory, address):
        packet = bytearray()
        packet.append(0x05)
        packet.append(0x30)
        packet.append(0x30)
        packet.append(0x52)
        packet.append(0x53)
        packet.append(0x42)
        packet.append(0x30)
        packet.append(51 + len(str(address)))
        packet.append(0x25)
        packet.append(bytearray(str(memory), encoding="latin-1")[0])
        packet.append(0x42)
        packet = packet + bytearray(str(address), encoding="latin-1")
        packet.append(0x36)
        packet.append(0x34)
        packet.append(0x04)
        bcc = 0
        for i in range(len(packet)):
            bcc = bcc + int(packet[i])
        packet.append(int(str(bcc)[-2:], 16))
        return packet

    def memory_checker(self, input_memory):
        memory = chr(input_memory)
        if self.Comm_Product_C.currentIndex() == 0:
            for a in PLC_Data.XGI:
                if a == memory:
                    return True
        elif self.Comm_Product_C.currentIndex() == 1:
            for a in PLC_Data.XGI:
                if a == memory:
                    return True
        elif self.Comm_Product_C.currentIndex() == 2:
            for a in PLC_Data.XGK:
                if a == memory:
                    return True
        elif self.Comm_Product_C.currentIndex() == 3:
            if self.Comm_Product_S_Name.currentIndex() == 0:
                for a in PLC_Data.XGK:
                    if a == memory:
                        return True
            elif self.Comm_Product_S_Name.currentIndex() == 1:
                for a in PLC_Data.XGK:
                    if a == memory:
                        return True
            elif self.Comm_Product_S_Name.currentIndex() == 2:
                for a in PLC_Data.XBC_SU:
                    if a == memory:
                        return True
            elif self.Comm_Product_S_Name.currentIndex() == 3:
                for a in PLC_Data.XBC_E:
                    if a == memory:
                        return True
            elif self.Comm_Product_S_Name.currentIndex() == 4:
                for a in PLC_Data.XBM_SILM:
                    if a == memory:
                        return True
        elif self.Comm_Product_C.currentIndex() == 4:
            if self.Comm_Product_S_Name.currentIndex() == 0:
                for a in PLC_Data.XGI:
                    if a == memory:
                        return True
            elif self.Comm_Product_S_Name.currentIndex() == 1:
                for a in PLC_Data.XGI:
                    if a == memory:
                        return True
            elif self.Comm_Product_S_Name.currentIndex() == 2:
                for a in PLC_Data.XEC:
                    if a == memory:
                        return True
            elif self.Comm_Product_S_Name.currentIndex() == 3:
                for a in PLC_Data.XEC:
                    if a == memory:
                        return True
        elif self.Comm_Product_C.currentIndex() == 5:
            return
        elif self.Comm_Product_C.currentIndex() == 6:
            for a in PLC_Data.GLOFA:
                if a == memory:
                    return True
        elif self.Comm_Product_C.currentIndex() == 7:
            return
        return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = WindowClass()
    mainWindow.show()
    mainWindow.CommSel_COM.setChecked(True)
    mainWindow.IP_1.setEnabled(False)
    mainWindow.IP_2.setEnabled(False)
    mainWindow.IP_3.setEnabled(False)
    mainWindow.IP_4.setEnabled(False)
    mainWindow.statusBar.showMessage("오프라인, 접속 대기중")
    mainWindow.setWindowTitle("메모리 뷰어")
    app.exec_()
