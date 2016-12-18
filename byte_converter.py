def bytes_to_int(input_bytes):
	int_array = []
	for index in range(len(input_bytes)):
		int_array.append(input_bytes[index])
	int_array.reverse()

	final_value = 0
	for index in range(len(int_array)):
		final_value += int_array[index] * (256 ** index)

	return final_value

def int_to_bytes(input_int, width):
	int_array = []
	value = input_int
	for n in range(width-1, -1 , -1):
		byte_value = input_int // (256 ** n)
		if byte_value >= 256:
			int_array.append(255)
		elif byte_value < 0:
			int_array.append(0)
		else:
			int_array.append(input_int // (256 ** n))
		value = value % (256 ** n)

	return bytes(int_array)
