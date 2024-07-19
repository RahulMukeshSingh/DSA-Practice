var maxProfit = function(prices) {
    let min_price = prices[0];
    let max_profit = 0;
    for (let i = 1; i < prices.length; i++) {
        min_price = Math.min(min_price, prices[i]);
        max_profit = Math.max(max_profit,prices[i] - min_price);
    }
    return max_profit;
};

let prices = [7,1,5,3,6,4];
console.log(maxProfit(prices));