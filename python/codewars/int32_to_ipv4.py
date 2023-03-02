# Take the following IPv4 address: 128.32.10.1
#
# This address has 4 octets where each octet is a single byte (or 8 bits).
#
# 1st octet 128 has the binary representation: 10000000
# 2nd octet 32 has the binary representation: 00100000
# 3rd octet 10 has the binary representation: 00001010
# 4th octet 1 has the binary representation: 00000001
# So 128.32.10.1 == 10000000.00100000.00001010.00000001
#
# Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361
#
# Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.
#
# Examples
# 2149583361 ==> "128.32.10.1"
# 32         ==> "0.0.0.32"
# 0          ==> "0.0.0.0"

# int('10000000', 2)  # 128
# format(128, '08b')  # 10000000

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


print(int32_to_ip(2149583361))  # ==> "128.32.10.1"
print(int32_to_ip(32))          # ==> "0.0.0.32"
print(int32_to_ip(0))           # ==> "0.0.0.0"


# ['10000000', '00100000', '00001010', '00000001']
# ['00000000', '00000000', '00000000', '00100000']
# ['00000000', '00000000', '00000000', '00000000']






################################################
from ipaddress import IPv4Address

def int32_to_ip2(int32):
    return str(IPv4Address(int32))



def int32_to_ip3(int32):
    """
    The solution involves bitwise AND of int32 and a mask that we can shift around.
    Say we have the number 17194 (0b0100001100101010). This can be divided into 2
    bytes: 01000011 and 00101010.
    We can AND this with a byte that is filled with 1s - 255 (0b11111111), shifted
    left by a certain amount of bytes to get the digits in that byte:
    01000011 00101010 # 17194
    11111111 00000000 # 255 << 8
    01000011 00000000 # 17194 & 255 << 8
    However, we need to shift this value *back* to get a number within (0,255)
    inclusive, as required, so shift right by the same amount.
    """
    first = (int32 & (255 << 24)) >> 24
    second = (int32 & (255 << 16)) >> 16
    third = (int32 & (255 << 8)) >> 8
    fourth = int32 & 255
    return f"{first}.{second}.{third}.{fourth}"


def int32_to_ip4(int32):
    return '.'.join(str(int32 >> (o << 3) & 0xff) for o in range(3, -1, -1))
