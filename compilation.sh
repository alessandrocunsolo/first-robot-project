gcc -c testlib.c -o testlib.o
gcc -shared -o testlib.so testlib.o
