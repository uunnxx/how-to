; 64-bit Linux only.
; nasm -felf64 hello.asm
; ld hello.o
; ./a.out
;
; ld hello.o -o hello
; ./hello
;


global      _start                  ; DIRECTIVES
section     .text                   ; SECTIONS

_start:     
    mov     rax, 1                  ; system call for write
    mov     rdi, 1                  ; file handle 1 is stdout
    mov     rsi, message            ; address of string to output
    mov     rdx, 13                 ; number of bytes
    syscall                         ; invoke operating system to do the write
    mov     rax, 60                 ; system call for exit
    xor     rdi, rdi                ; exit code 0
    syscall                         ; invoke operating system to do the write

    section .data

message:
    db      'Hello, world', 10      ; note the newline at the end
