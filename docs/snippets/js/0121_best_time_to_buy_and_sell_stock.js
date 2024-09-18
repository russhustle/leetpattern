// Greedy
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let maxProfit = 0;
  let seenMin = prices[0];
  const n = prices.length;

  if (n < 2) {
    return maxProfit;
  }

  for (let i = 1; i < n; i++) {
    maxProfit = Math.max(maxProfit, prices[i] - seenMin);
    seenMin = Math.min(seenMin, prices[i]);
  }
  return maxProfit;
};

const prices = [7, 1, 5, 3, 6, 4];
console.log(maxProfit(prices)); // 5
