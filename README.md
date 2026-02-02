# Freelance-Income-Data-Analysis
## Helping freelance performers manage income volatility by identifying a practical savings buffer and visualizing income trends for informed financial planning.
## Executive Summary
This project analyzes synthetic income data to determine a recommended savings buffer for a freelance performer. Using pandas, NumPy, SQL, and matplotlib, it calculates monthly totals, rolling averages, and a minimum buffer to ensure financial stability during low-income months.

Freelance performers experience variable and often unpredictable income. This project analyzes three years of synthetic income data to answer:

- What is the three-month rolling average income for any given month?
- What is the minimum recommended savings buffer to survive low- or no-income months?

## Project workflow
1. Generate synthetic income data (pandas & NumPy)
2. Aggregate payments by month (SQL)
3. Compute three-month rolling average and recommended savings buffer (pandas)
4. Visualize results (matplotlib)

## Key insights
- Average monthly income: €6,003  
- Number of low-income months (<€2,000): 3  
- Recommended savings buffer: €2,027.10

## Next steps
- Implement a dynamic savings plan: contribute higher amounts initially to reach the buffer, then maintain it with minimal contributions relative to monthly income.

## Limitations
- Synthetic data with simplified assumptions  
- Does not account for irregular large expenses
  
