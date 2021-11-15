#include "runningsum.h"
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int main(int argc, char const *argv[]){

    int testcase = 1;
	
    // testcase 1:
    printf("Running testcase %d... ", testcase);
	int* nums = malloc(4 * sizeof(int));
    nums[0] = 1; nums[1] = 2; nums[2] = 3; nums[3] = 4;
	int* data = runningSum(nums, 4);
    assert(data[0] == 1); assert(data[1] == 3); 
    assert(data[2] == 6); assert(data[3] == 10);
	free(data); free(nums);
    printf("Passed\n"); testcase++;

    // testcase 2:
    printf("Running testcase %d... ", testcase);
	nums = malloc(4 * sizeof(int));
    nums[0] = 1; nums[1] = 1; nums[2] = 1; nums[3] = 1; nums[4] = 1;
	data = runningSum(nums, 5);
    assert(data[0] == 1); assert(data[1] == 2); 
    assert(data[2] == 3); assert(data[3] == 4); assert(data[4] == 5);
	free(data); free(nums);
    printf("Passed\n"); testcase++;

    // testcase 3:
    printf("Running testcase %d... ", testcase);
	nums = malloc(4 * sizeof(int));
    nums[0] = 3; nums[1] = 1; nums[2] = 2; nums[3] = 10; nums[4] = 1;
	data = runningSum(nums, 5);
    assert(data[0] == 3); assert(data[1] == 4); 
    assert(data[2] == 6); assert(data[3] == 16); assert(data[4] == 17);
	free(data); free(nums);
    printf("Passed\n"); testcase++;

	return 0;
}
