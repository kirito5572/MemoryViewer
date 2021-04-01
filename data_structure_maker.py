import DataSize


def memory_data_builder(memory, size, start, end):
    return_data = []
    if size == DataSize.BIT:
        size = "X"
        return_data = [i for i in range((((end - start) // 10) + 1) * 8)]
        for i in range((((end - start) // 10) + 1) * 8):
            return_data[i] = "%" + str(memory) + size + str(i * 10 + start)
    elif size == DataSize.BYTE:
        size = "B"
        return_data = [i for i in range(((end - start) // 10) + 1)]
        for i in range(((end - start) // 10) + 1):
            return_data[i] = "%" + str(memory) + size + str(i * 10 + start)
    elif size == DataSize.WORD:
        size = "W"
        return_data = [i for i in range(((end - start) // 20) + 1)]
        for i in range(((end - start) // 20) + 1):
            return_data[i] = "%" + str(memory) + size + str(i * 10 + start)
    elif size == DataSize.DWORD:
        size = "D"
        return_data = [i for i in range(((end - start) // 40) + 1)]
        for i in range(((end - start) // 40) + 1):
            return_data[i] = "%" + str(memory) + size + str(i * 10 + start)
    elif size == DataSize.LWORD:
        size = "L"
        return_data = [i for i in range(((end - start) // 80) + 1)]
        for i in range(((end - start) // 80) + 1):
            return_data[i] = "%" + str(memory) + size + str(i * 10 + start)
    return return_data
