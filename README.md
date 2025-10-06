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
<h3>The basics of linear regression</h3>

Here, in this topic, we will try to estimate a value `y` based on a value `x`, i.e. the price of a car based on its mileage.

This involves guessing/calculating `y` based on `x`. In mathematics, we refer to this as a linear function, which is defined by the formula: `y = (a * x) + b = ax + b`.
We know that once we know `a` and `b`, we can estimate the price of a car based on its mileage.

To do this, we have a sample of data that gives us access to estimated prices based on mileage. The goal is to find the values of `a` and `b` for which we find the same values as in the initial sample.

In general, a linear function can be represented by a straight line where `a` represents the slope of the line and `b` represents the first value of the line in `y`.

<h2>Building the 42 ft_linear_regression project</h2>
<h3>Predict the price of a car</h3>

The estimated price of a car in this roject is set at : `estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)` for every given mileage.
In parallel with the preamble, we find `θ0 = b` and `θ1 = a` in `y = ax + b`.

<h3>Train the model</h3>

To find `a` and `b`, we have at our disposal : 
```
                          m-1
θ0 = θ0 - (learningRate ∗  ∑  (estimateP rice(mileage[i]) − price[i]))
                          i=0

                          m-1
θ1 = θ1 - (learningRate ∗  ∑  (estimateP rice(mileage[i]) − price[i]) ∗ mileage[i])
                          i=0

```

1. Since the formula for θ1 involves multiplying by mileage AND the mileage indicated in the data is very high, we will obtain disproportionate theta values. We will therefore normalise each column to set the maximum value to 1.0 and the minimum value to 0.0.
2. Next, we will loop until the results of the thetas formula are similar.
3. At this stage, it is sufficient to denormalise the data and the thetas.
4. Tests can be carried out to verify the consistency between the estimate and the actual price for a certain mileage.
5. Finally, we will save thetas in our json.

<h3>Bonuses</h3>

1-2. The goal is to draw a plot of data into a graph, then draw the regression line to see the precision of this project.
3. The aim of this part is to calculate the precision of the algorithm that we've been coding. To do so, we know that `R²` or 'coefficient of determination' is the most appropriate and is set at : `R² = 1 - (Σ(y_i - ŷ_i)² / Σ(y_i - ȳ)²)` where `ŷ` is our prediction. `R²` answer to the question "What percentage of variation can we explain ?", so `R²` is between 0.00 and 1.00.
