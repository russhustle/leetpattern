function numIslands(grid: string[][]): number {
    const m = grid.length;
    const n = grid[0].length;

    function dfs(grid: string[][], r: number, c: number) {
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] === "0") {
            return;
        }

        grid[r][c] = "0";
        dfs(grid, r - 1, c);
        dfs(grid, r + 1, c);
        dfs(grid, r, c - 1);
        dfs(grid, r, c + 1);
    }

    let res = 0;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c] === "1") {
                res++;
                dfs(grid, r, c);
            }
        }
    }
    return res;
}

const grid: string[][] = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
];
console.log(numIslands(grid)); // 3
