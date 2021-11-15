#include "twosum.h"
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int main(int argc, char const *argv[]){

    int testcase = 1;
	
    // testcase 1:
    printf("Running testcase %d... ", testcase);
	int* nums = malloc(4 * sizeof(int));
    nums[0] = 2; nums[1] = 7; nums[2] = 11; nums[3] = 15;
	int* data = twoSum(nums, 4, 9);
    assert(data[0] == 0); assert(data[1] == 1);
	free(data); free(nums);
    printf("Passed\n"); testcase++;

    // testcase 2:
    printf("Running testcase %d... ", testcase);
    nums = malloc(3 * sizeof(int));
    nums[0] = 3; nums[1] = 2; nums[2] = 4;
	data = twoSum(nums, 3, 6);
    assert(data[0] == 1); assert(data[1] == 2);
	free(data); free(nums);
    printf("Passed\n"); testcase++;

    // testcase 3:
    printf("Running testcase %d... ", testcase);
    nums = malloc(2 * sizeof(int));
    nums[0] = 3; nums[1] = 3;
	data = twoSum(nums, 2, 6);
    assert(data[0] == 0); assert(data[1] == 1);
	free(data); free(nums);
    printf("Passed\n"); testcase++;

	return 0;
}
