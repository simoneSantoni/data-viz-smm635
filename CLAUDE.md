# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the course repository for SMM635 Data Visualization, a Master's level module at Bayes Business School. The repository contains:
- A Quarto-based course website with weekly materials, syllabus, and project information
- Interactive presentations using RevealJS for lectures on design principles and data visualization techniques
- Course materials covering visualization theory (Tufte, grammar of graphics) and practical implementation with R, Python, and Tableau

## Build and Development Commands

### Website Development
```bash
# Build the website
cd website && quarto render

# Preview the website with live reload
cd website && quarto preview

# Build a specific file/section
cd website && quarto render path/to/file.qmd

# Clean build artifacts
cd website && rm -rf _site _freeze .quarto
```

### Environment Setup
```bash
# Create and activate the course conda environment
conda env create -f smm635.yaml
conda activate smm635

# The environment includes both R and Python packages for data visualization
```

### Git Operations
```bash
# The main branch is 'master' (not 'main')
git push origin master

# Website deployment trigger file exists at website/.deployment-trigger
```

## Architecture and Structure

### Quarto Website Architecture
The website uses Quarto's multi-format publishing system:
- **_quarto.yml**: Main configuration defining site structure, sidebar navigation, and theming
- **_site/**: Generated static website output (do not edit directly)
- **_freeze/**: Quarto's computational cache for executed code chunks
- **.quarto/**: Internal Quarto metadata and indexing

### Content Organization
- **website/weeks/**: Weekly course materials with main.qmd files for each week's overview
- **website/course/**: Core course documents (syllabus, schedule, support, team)
- **website/project/**: Mid-term and final project specifications
- **website/notes/**: Supplemental learning materials
- **website/imgs/**: Icons and branding assets

### Theming System
- Dual theme support: `theme.scss` (light) and `theme-dark.scss` (dark)
- Base theme: Cosmo from Bootswatch
- Custom fonts: Atkinson Hyperlegible for accessibility
- RevealJS presentations have separate styling in `presentation-styles.css`

### Key Technologies
- **Quarto**: Static site generator with support for executable code blocks
- **RevealJS**: Interactive presentation framework for lectures
- **R/Python Integration**: Both languages supported via conda environment
- **Visualization Libraries**: ggplot2, plotly, matplotlib, seaborn, altair, Tableau

## Development Patterns

### Adding New Weekly Content
Create a new week's materials in `website/weeks/week-N/`:
- `main.qmd` for the week overview
- Additional `.qmd` files for specific topics
- `images/` subdirectory for visual assets
- Update `website/_quarto.yml` sidebar navigation

### Working with Presentations
RevealJS presentations like `design-principles-presentation.qmd`:
- Use `format: revealjs` in YAML header
- Custom CSS via `presentation-styles.css`
- Slide transitions and interactive elements supported

### Code Execution
Quarto documents support executable code chunks:
- R chunks: ````{r}````
- Python chunks: ````{python}````
- Execution controlled via `execute:` settings in _quarto.yml