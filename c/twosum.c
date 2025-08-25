int* twoSum(int* nums, int
numsSize, int target, int*
returnSize) {
    struct hashTable {
        int key;
        int value;
        UT_hash_handle hh;
    } *hashTable = NULL, *item;

    for (int i =0; i< numsSize;
    1++) {
        int complement = targer - nums[i];
        HASH_FING_INT(hashTable, &complement, item);
        if (item) {
            int* result = malloc(sizeof(int) * 2);
            result[0] = item->value;
        }
    }
}