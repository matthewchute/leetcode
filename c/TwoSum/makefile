# compiler
CC = gcc

all: test_twosum test 

# compile all .c files into .o files
# $< is the source file (.c file)
%.o: %.c
	$(CC) -c $<

# build if any .o file changes
test_twosum: twosum.o test_twosum.o
	$(CC) -o test_twosum twosum.o test_twosum.o

test: test_twosum
	./test_twosum

clean:
	rm -f *.o test_twosum
	clear