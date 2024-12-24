function removeElement(nums: number[], val: number): number {
    let slow: number = 0,
        fast: number = 0;

    while (fast < nums.length) {
        if (nums[fast] !== val) {
            nums[slow++] = nums[fast];
        }
        fast++;
    }
    return slow;
}

const nums: number[] = [3, 2, 2, 3];
const val: number = 3;
console.log(removeElement(nums, val)); // 2
