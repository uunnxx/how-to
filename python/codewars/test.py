def int32_to_ip(int32):
    def get_bits(int32):
        four_byte = str(format(int32, '032b'))  # 10000000
        split_size = 8
        bits = [four_byte[i: i + split_size] for i in range(0, 32, split_size)]
        return bits

    def get_ints(bits):
        ints = [str(int(bit, 2)) for bit in bits]
        return ints

    return '.'.join(get_ints(get_bits(int32)))


def ip_to_int32(ip):
    def get_bits(ip):
        four_byte = str(format(ip, '032b'))  # 10000000
        split_size = 8
        bits = [four_byte[i: i + split_size] for i in range(0, 32, split_size)]
        return bits

    def get_ints(bits):
        ints = [str(int(bit, 2)) for bit in bits]
        return ints

    return '.'.join(get_ints(get_bits(ip)))


print(int32_to_ip(2149583361))  # ==> "128.32.10.1"
print(int32_to_ip(32))          # ==> "0.0.0.32"
print(int32_to_ip(0))           # ==> "0.0.0.0"
print('-' * 40)
print(ip_to_int32("128.32.10.1"))  # ==> "128.32.10.1"
print(ip_to_int32("0.0.0.32"))          # ==> "0.0.0.32"
print(ip_to_int32("0.0.0.0"))           # ==> "0.0.0.0"
