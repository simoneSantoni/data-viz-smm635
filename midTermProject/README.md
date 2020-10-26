# Mid-term project - README

This directory contains a textual description of the problem at the center of
the mid-course project along with essential data.

# Scope of the project

For the **MTP**, students are supposed to:

+   to analyze the performance of British, publicly-listed companies in the
aftermath of the 2016 Brexit Referendum. A group of publicly listed companies
based in France and Germany will offer the counterfactual data to estimate how
British companies could have performed in case of no-leave;
+   to visually display the insights emerging from the analysis.

Mainly, there are three routes to visually display the results:

1.  adopting descriptive statistical charts (that is, drawing on the tools
2.  adopting charts that convey the results produced with statistical models
such as linear regression (that is, drawing on the tools discussed in week 5
of the model);
3.  going for a combination of the previous two routes.

**!!!  Notes ¡¡¡**: the choice of the route does not affect the mark of the
submission. In other words, I do not have any preference for a certain route.
In terms of marking, what matters is the set of assessment criteria reported
in the README of the repo.

# Target audience

The chart will be included in the next issues of The Economist to complement a
commentary written by an economic journalist.

# Data

The data for the project contains:

+   population of companies
+   economic & financials (both short- and long-term)

## Variables

Below is the codebook for the variables included in the data table:

-   'company': name of the company;
-   'country': company location;
-   'price': share price;
-   'sector': sector in which a company operates
-   'assets': company assets (in thousands)
-   'operating': ratio of a company's operating income before interest and
    taxes (earnings before interest, taxes) to the book value of total assets;
-   'debt_to_assets': the variable reflects the ratio between the sum of a
     company’s total debt on the book value of total assets;
-   'age': company's tenure;
-   'date': timestemp

## Population of companies

The file `companies.csv` contains a list of companies along with the reference
country/stock market.

## Economic & financials

There are two files containing economic & financials (variables' names are
self-explanatory):

+   `financials__long_term`: monthly data-points spanning the years 2014 -
2018
+   `financials__short_term`: daily data-points in the vicinity of the Brexit
Referendum.

# Deliverables

By November 11 (8:00 PM),i students are supposed to upload the following onto Moodle:

+   a .pdf of the visualization;
+   the Python code of the project;
+   a companion document that explains:
  -   the design choices behind the visualization and their rationales
  -   the data transformation and analysis tasks (if any) carried out to achieve the visualization.

Regarding the companion document, students are free to pick-up the template the best serves their needs. I'll accept:

+ report (.docx, .md, or .pdf generated via LaTeX)
+ beamer (.pptx, .md, or .pdf generated via LaTeX)
+ report + beamer

Concise documents with high per word added value are welcome.

# Modeling Tip

**!!!  Notes ¡¡¡**: What follows is relevant **IF AND ONLY IF** you decide to go down route 2, as per the 'Scope' section of this README.

Tip to model the economic-financial performance of UK companies relative to
German and French companies: use the so-called Difference-in-Differences (DiD)
design (see [Sieweke & Santoni,
2020](https://www.sciencedirect.com/science/article/pii/S1048984318308476),
page: 3, 'Standard Natural Experiments' section). Here's the intuition of the
DiD: let's assume your data contain diachronic information on two types of
companies, namely, treated and control companies. Treated companies only
experience an environmental change, i.e., the increase in institutional
uncertainty associated with the 'leave' decision. This translates in a dataset
that looks like this:

| Company | Year | Country | Treated (d) | Post-Brexit Year (t) | y   | x   | z   |
|---------|------|---------|-------------|----------------------|-----|-----|-----|
| A       | 2015 | UK      | Yes         | No                   | ... | ... | ... |
| A       | 2016 | UK      | Yes         | No                   | ... | ... | ... |
| A       | 2017 | UK      | Yes         | Yes                  | ... | ... | ... |
| B       | 2015 | FR      | No          | No                   | ... | ... | ... |
| B       | 2016 | FR      | No          | No                   | ... | ... | ... |
| B       | 2017 | FR      | No          | Yes                  | ... | ... | ... |

The economic-financial performance (y) can then be modeled as:

y = α + β1 * x + β2 * z + γ * d + δ * t + ζ * d * t + ε

The estimated quantity ζ captures the change in performance of UK companies
(i.e., treated units) relative to non-UK companies (i.e., control units). In
fact, the interaction between the binary variables d and t is equal to 1 if
and only if the observations pertain to a UK company in a post-Brexit
referendum year.
