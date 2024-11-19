namespace TwoSumNamespace {
    export function twoSum(nums: number[], target: number): number[] {
        let map: Map<number, number> = new Map();
        let index: number | undefined;
        let res: number[] = [];

        for (let i = 0; i < nums.length; i++) {
            index = map.get(target - nums[i]);

            if (index !== undefined) {
                res = [i, index];
                break;
            }
            map.set(nums[i], i);
        }
        return res;
    }

    const nums = [2, 7, 11, 15];
    const target = 9;
    console.log(twoSum(nums, target)); // [1, 0]
}
