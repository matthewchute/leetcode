#include "runningsum.h"
#include <stdlib.h>

int* runningSum(int* nums, int numsSize){

    // init return size
    int* ret = malloc(numsSize * sizeof(int));

    // linear scan through and accumulate values
    for(int i = 0; i < numsSize; i++){
        if (i == 0)
            ret[i] = nums[i];
        else
            ret[i] = ret[i-1] + nums[i];
    }

    return ret;
}
