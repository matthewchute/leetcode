#include "twosum.h"
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target){

    // init return size
    int* ret = malloc(2 * sizeof(int));

    // brute force checking each combination
    for (ret[0] = 0; ret[0] < numsSize; ++ret[0]){
        for (ret[1] = ret[0] + 1; ret[1] < numsSize; ++ret[1]){
            if (nums[ret[0]] + nums[ret[1]] == target) 
                return ret;
        }
    }

    return ret;
}
