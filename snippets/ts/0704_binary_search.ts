function search(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;
    let mid: number;

    while (left <= right) {
        mid = left + Math.floor((right - left) / 2);

        if (nums[mid] > target) {
            right = mid - 1;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            return mid;
        }
    }
    return -1;
}

const nums = [-1, 0, 3, 5, 9, 12];
const target = 9;
console.log(search(nums, target)); // 4
