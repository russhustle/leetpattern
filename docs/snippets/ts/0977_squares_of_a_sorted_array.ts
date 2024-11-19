function sortedSquares(nums: number[]): number[] {
    const res: number[] = [];
    let left = 0,
        right = nums.length - 1;

    while (left <= right) {
        if (Math.abs(nums[left]) > nums[right]) {
            res.unshift(nums[left] ** 2);
            left++;
        } else {
            res.unshift(nums[right] ** 2);
            right--;
        }
    }

    return res;
}

const nums = [-4, -1, 0, 3, 10];
console.log(sortedSquares(nums)); // [0, 1, 9, 16, 100]
