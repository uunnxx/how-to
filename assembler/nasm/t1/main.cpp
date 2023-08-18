#include <iostream>

// using namespace std;


// int get_asm_value() {
// 	asm("movl $254, %eax");
// }


extern "C" int get_asm_value();


int main() {
	std::cout << "FROM ASM: " << get_asm_value() << std::endl;
	return 0;
}
