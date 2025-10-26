<div align="center" class="text-center">
  <h1>42-Ft_Linear_Regression</h1>
  
  <img alt="last-commit" src="https://img.shields.io/github/last-commit/socallmebertille/42-Ft_Linear_Regression?style=flat&amp;logo=git&amp;logoColor=white&amp;color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
  <img alt="repo-top-language" src="https://img.shields.io/github/languages/top/socallmebertille/42-Ft_Linear_Regression?style=flat&amp;color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
  <img alt="repo-language-count" src="https://img.shields.io/github/languages/count/socallmebertille/42-Ft_Linear_Regression?style=flat&amp;color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
  <p><em>Built with the tools and technologies:</em></p>
  <img alt="Markdown" src="https://img.shields.io/badge/Markdown-000000.svg?style=flat&amp;logo=Markdown&amp;logoColor=white" class="inline-block mx-1" style="margin: 0px 2px;">
  <img alt="GNU%20Bash" src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&amp;logo=GNU-Bash&amp;logoColor=white" class="inline-block mx-1" style="margin: 0px 2px;">
  <img alt="Python" src="https://img.shields.io/badge/python-2496ED.svg?style=flat&amp;logo=python&amp;logoColor=white" class="inline-block mx-1" style="margin: 0px 2px;">
</div>

<h2>Table of Contents</h2>
<ul class="list-disc pl-4 my-0">
  <li class="my-0"><a href="#overview">Overview</a></li>
  <ul class="list-disc pl-4 my-0">
    <li class="my-0"><a href="#few-python-notions">Few Python notions</a></li>
    <li class="my-0"><a href="#the-basics-of-linear-regression">The basics of linear regression</a></li>
  </ul>
  <li class="my-0"><a href="#building-the-42-ft_linear_regression-project">Building the 42 ft_linear_regression project</a>
  <ul class="list-disc pl-4 my-0">
    <li class="my-0"><a href="#predict-the-price-of-a-car">Predict the price of a car</a></li>
    <li class="my-0"><a href="#train-the-model">Train the model</a></li>
    <li class="my-0"><a href="#bonuses">Bonuses</a></li>
  </ul>
  </li>
</ul>

<h2>Overview</h2>
<h3>Few Python notions</h3>

- `flake8`

```
            installation:
pip install flake8
export PATH="$HOME/.local/bin:$PATH"
source ~/.zshrc                           // if zsh env

            usage:
flake8 my_file.py
flake8 my_project/
```

Return syntax errors or possible syntax improvements :
| Code | Meaning                                     |
| ---- | ------------------------------------------- |
| E501 | Line too long                               |
| E302 | Not enough blank lines before a function    |
| F401 | Unused import                               |
| F841 | Variable assigned but never used            |
| W291 | Spaces at the end of the line               |
| C901 | Function too complex                        |

- `yield`

| Aspect                   | `return`             | `yield`                                    |
| ------------------------ | -------------------- | ------------------------------------------ |
| Interrupts the function  | Yes (permanently)    | No (pauses, can resume)                    |
| Returns a value          | Once only            | Several times (once per call to `next()`)  |
| Memory usage             | Stores everything    | Produced on demand                         |
| Output type              | Direct value         | Generator (`<generator object ...>`)       |


<h3>The basics of linear regression</h3>

Here, in this topic, we will try to estimate a value `y` based on a value `x`, i.e. the price of a car based on its mileage.

This involves guessing/calculating `y` based on `x`. In mathematics, we refer to this as a linear function, which is defined by the formula: `y = (a * x) + b = ax + b`.
We know that once we know `a` and `b`, we can estimate the price of a car based on its mileage.

To do this, we have a sample of data that gives us access to estimated prices based on mileage. The goal is to find the values of `a` and `b` for which we find the same values as in the initial sample.

In general, a linear function can be represented by a straight line where `a` represents the slope of the line and `b` represents the first value of the line in `y`.

To find `a` & `b`, also called `θ0` & `θ1`, we will implement the GRADIENT DESCENT ALGORITHM :
1. Initialize theta0, theta1
2. Repeat until convergence:
   - Calculate gradients
   - Update thetas
   - Check convergence
3. Return optimal thetas

<h2>Building the 42 ft_linear_regression project</h2>
<h3>Predict the price of a car</h3>

The estimated price of a car in this roject is set at : `estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)` for every given mileage.
In parallel with the preamble, we find `θ0 = b` and `θ1 = a` in `y = ax + b`.

<h3>Train the model</h3>

To find `a` and `b`, we have at our disposal : 
```
                          1    m-1
θ0 = θ0 - (learningRate ∗ __ ∗  ∑  (estimateP rice(mileage[i]) − price[i]))
                          m    i=0

                          1    m-1
θ1 = θ1 - (learningRate ∗ __ ∗  ∑  (estimateP rice(mileage[i]) − price[i]) ∗ mileage[i])
                          m    i=0

```
where learning rate is the size of the steps your algorithm takes to adjust the thetas.

1. **Data Normalization**
   - Problem: Raw mileage values (up to 240,000) cause numerical instability
   - Solution: Normalize all values between 0.0 and 1.0
   - Formula: `normalized = (value - min) / (max - min)`

2. **Gradient Descent Loop**
   - Initialize θ0 = 0, θ1 = 0
   - Iterate until convergence (change < threshold) or max iterations
   - Update thetas using gradient formulas

3. **Denormalization**
   - Convert normalized thetas back to work with real mileage values
   - Formula: `θ1_real = θ1_norm × (price_range / mileage_range)`

4. **Validation**
   - Test predictions against actual prices
   - Display sample results

5. **Save Results**
   - Store final θ0 and θ1 in `theta.json`

<h3>Bonuses</h3>

1 - 2 . The goal is to draw a plot of data into a graph, then draw the regression line to see the precision of this project.

3 . The aim of this part is to calculate the precision of the algorithm that we've been coding. To do so, we know that `R²` or 'coefficient of determination' is the most appropriate and is set at : `R² = 1 - (Σ(y_i - ŷ_i)² / Σ(y_i - ȳ)²)` where `ŷ` is our prediction. `R²` answer to the question "What percentage of variation can we explain ?", so `R²` is between 0.00 and 1.00. To be more precise, we also used to the `RMSE` or "Root Mean Squared Error" which answers to the question "What is my standard error ?".
