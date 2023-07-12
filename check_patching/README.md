## Patching


### Build main:
`gcc -o main main.c`

### Check `.text` section to find `main`:
`objdump -S --section=.text main`

#### We interested in `main` section:

```
...
0000000000001169 <main>:
    1169:	f3 0f 1e fa          	endbr64
    116d:	55                   	push   %rbp
    116e:	48 89 e5             	mov    %rsp,%rbp
    1171:	48 83 ec 10          	sub    $0x10,%rsp
    1175:	c7 45 fc 0a 00 00 00 	movl   $0xa,-0x4(%rbp)
    117c:	e8 ef fe ff ff       	call   1070 <rand@plt>
    1181:	39 45 fc             	cmp    %eax,-0x4(%rbp)
    1184:	75 0f                	jne    1195 <main+0x2c>        # we looking for `jne` opcode `75`, address 0x1184
    1186:	48 8d 05 77 0e 00 00 	lea    0xe77(%rip),%rax
    118d:	48 89 c7             	mov    %rax,%rdi
    1190:	e8 cb fe ff ff       	call   1060 <puts@plt>
    1195:	b8 00 00 00 00       	mov    $0x0,%eax
    119a:	c9                   	leave
    119b:	c3                   	ret
...

```

We have to change `jne` `75` to `74` `jz`:

```
...
0000000000001169 <main>:
    1169:	f3 0f 1e fa          	endbr64
    116d:	55                   	push   %rbp
    116e:	48 89 e5             	mov    %rsp,%rbp
    1171:	48 83 ec 10          	sub    $0x10,%rsp
    1175:	c7 45 fc 0a 00 00 00 	movl   $0xa,-0x4(%rbp)
    117c:	e8 ef fe ff ff       	call   1070 <rand@plt>
    1181:	39 45 fc             	cmp    %eax,-0x4(%rbp)
    1184:	74 0f                	jz     1195 <main+0x2c>        # replace  `jne` opcode `75` to `jz` opcode `74`, address 0x1184
    1186:	48 8d 05 77 0e 00 00 	lea    0xe77(%rip),%rax
    118d:	48 89 c7             	mov    %rax,%rdi
    1190:	e8 cb fe ff ff       	call   1060 <puts@plt>
    1195:	b8 00 00 00 00       	mov    $0x0,%eax
    119a:	c9                   	leave
    119b:	c3                   	ret
...
```

```
#include <stdio.h>


int main() {
    FILE *f = fopen("main", "r+b");        # pointer to `main` file
    unsigned char opcode = 0x74;           # replace to `0x74 jz`
    fseek(f, 0x1184, SEEK_SET);            # address 0x1184
    fwrite(&opcode, sizeof(opcode), 1, f); # write
    fclose(f);
    printf("Done!\n");
    return 0;
}

```

### Build patch:
`gcc -o patch patch.c`
