# compiler
CC = gcc

all: test_runningsum test 

# compile all .c files into .o files
# $< is the source file (.c file)
%.o: %.c
	$(CC) -c $<

# build if any .o file changes
test_runningsum: runningsum.o test_runningsum.o
	$(CC) -o test_runningsum runningsum.o test_runningsum.o

test: test_runningsum
	./test_runningsum

clean:
	rm -f *.o test_runningsum
	clear