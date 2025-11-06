# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the course repository for SMM635 Data Visualization, a Master's level module at Bayes Business School. The repository contains:
- A Quarto-based course website with weekly materials, syllabus, and project information
- Interactive presentations using RevealJS for lectures on design principles and data visualization techniques
- Course materials covering visualization theory (Tufte, grammar of graphics) and practical implementation with R, Python, and Tableau

## Build and Development Commands

### Website Development
All Quarto commands should be run from the `website/` directory:

```bash
# Build the website (from repository root)
cd website && quarto render

# Preview with live reload (opens browser on http://localhost:XXXX)
cd website && quarto preview

# Build a specific file
cd website && quarto render path/to/file.qmd

# Build without executing code (faster, uses cached results)
cd website && quarto render --no-execute

# Clean all build artifacts and cache
cd website && rm -rf _site _freeze .quarto
```

**Important**: Always execute Quarto commands from within `website/` directory to ensure proper path resolution for assets, includes, and R/Python code execution.

### Environment Setup
```bash
# Create and activate the course conda environment
# Note: The YAML has a typo (sependencies instead of dependencies)
conda env create -f smm635.yaml
conda activate smm635

# The environment includes:
# - R packages: tidyverse, ggplot2, plotly, shiny, viridis, RColorBrewer, etc.
# - Python packages: matplotlib, seaborn, altair, dash, plotly, bokeh, pyvis
```

### Git Operations
```bash
# IMPORTANT: Main branch is 'master' (not 'main')
git push origin master

# Website is deployed via GitHub Actions on every push to master
# No manual deployment needed - see .github/workflows/publish.yml
```

## Architecture and Structure

### Quarto Website Architecture
The website uses Quarto's multi-format publishing system with custom output configuration:
- **_quarto.yml**: Main configuration defining site structure, sidebar navigation, and theming
  - **Critical**: `output-dir: _site` publishes to `website/_site`
  - GitHub Actions deploys from `website/_site` to GitHub Pages
  - Sidebar has 10 weeks of content plus course info and project sections
- **website/_site/**: Generated static website output (git-tracked, do not manually edit)
- **website/_freeze/**: Quarto's computational cache for executed code (enabled with `freeze: auto`)
- **website/.quarto/**: Internal Quarto metadata and indexing
- **docs/**: Legacy generated output directory (no longer actively used; kept for reference)

### Content Organization
- **website/weeks/**: Weekly course materials following the 5P structure:
  - Each week has a `main.qmd` with: Prepare, Participate, Practice, Perform, Ponder sections
  - Additional topic-specific `.qmd` files (e.g., `design-principles-presentation.qmd`)
  - Supporting assets in `images/` subdirectories
  - **Note**: There's an unusual `cd ../` directory within weeks/ - appears to be a directory naming accident
- **website/course/**: Core course documents (syllabus, schedule, support, team)
- **website/project/**: Mid-term and final project specifications in subdirectories (midTermProject/, finalCourseProject/)
- **website/notes/**: Supplemental learning materials
- **website/imgs/**: Icons and branding assets (e.g., `r-module-icon-light.svg`)
- **data/**: Course datasets located at repository root, including:
  - `crm.xlsx`: CRM data for exercises
  - `data_a.xlsx`: Additional dataset A
  - `ecar.csv`: Electric car dataset (large, 10MB+)
  - `googleplaystore.csv` and `googleplaystore_user_reviews.csv`: Google Play Store datasets

### Theming System
- **Dual theme support**: `theme.scss` (light) and `theme-dark.scss` (dark)
  - Base: Cosmo from Bootswatch
  - Custom fonts: Atkinson Hyperlegible (specified in `_quarto.yml: mainfont`)
- **RevealJS presentations**: Separate styling in `presentation-styles.css` (e.g., week-1)
- **Theme switcher**: JavaScript-based theme toggle via `website/theme-switcher.js`

### R Configuration
Quarto is configured to use a specific R installation from the conda environment:
- `r-path: /home/simon/miniconda3/envs/smm635/bin/R` in `_quarto.yml`
- **Note**: The hardcoded path uses `/home/simon/` which may differ from the current working directory `/home/simone/`
- Jupyter kernelspec points to "ir" (R kernel) with display name "R (ind215)"
- When working on different machines or with different users, this path will need adjustment

### Key Technologies
- **Quarto**: Static site generator with support for executable R/Python code blocks
- **RevealJS**: Interactive presentation framework for lectures (format: revealjs in YAML)
- **R/Python Integration**: Dual-language support via conda environment
- **Visualization Libraries**:
  - R: ggplot2, plotly, shiny, leaflet, gganimate, highcharter, treemap, patchwork
  - Python: matplotlib, seaborn, altair, dash, plotly, bokeh, pyvis

## Development Patterns

### Adding New Weekly Content
Follow the established 5P structure when creating materials in `website/weeks/week-N/`:

1. Create `main.qmd` with standard sections:
   - **Prepare**: Pre-class materials/readings
   - **Participate**: Lecture materials (link to presentations)
   - **Practice**: Laboratory session activities
   - **Perform**: Exercises and assignments
   - **Ponder**: Essential readings and reflection materials

2. Add topic-specific files as needed (presentations, exercises, etc.)
3. Create `images/` subdirectory for visual assets
4. **Critical**: Update `website/_quarto.yml` sidebar navigation to include the new week
5. Use callout blocks for notes: `::: {.callout-note}`

### Working with Presentations
RevealJS presentations (e.g., `design-principles-presentation.qmd`):
- Set `format: revealjs` in YAML front matter
- Link custom CSS with `css: presentation-styles.css`
- Use `##` for slide breaks, `###` for sub-slides
- Slides are rendered to HTML and linked from weekly `main.qmd` files
- **Important**: Do not use `quarto preview` for presentations - it may not work correctly. Use `quarto render` and open the HTML file directly.

### Code Execution
Quarto documents support executable code chunks:
- R chunks: ````{r}` with optional chunk options
- Python chunks: ````{python}`
- Execution settings in `_quarto.yml`:
  - `freeze: auto` - caches results, re-executes only when code changes
  - `echo: true` - shows code in output
  - `warning: false`, `message: false` - suppresses R/Python warnings
- Use `--no-execute` flag to skip code execution and use cached results

### GitHub Actions Deployment
The site deploys automatically on push to master:
- Workflow: `.github/workflows/publish.yml`
- Installs minimal R dependencies (rmarkdown, knitr only)
- Uses `quarto render --no-execute` to avoid heavy computations
- Special handling: Temporarily removes PDF format from syllabus during CI build (using sed to strip PDF output section)
- Deploys from `website/_site` to GitHub Pages
- Timeout: 30 minutes
- Uses caching for R packages to speed up builds

## Common Issues

### R Path Configuration
The `_quarto.yml` contains a hardcoded R path specific to one machine:
```yaml
r:
  r-path: /home/simon/miniconda3/envs/smm635/bin/R
```
**Problem**: The current working directory shows `/home/simone/` but the configuration uses `/home/simon/`.

**Solutions**:
- Update the path to match your conda environment location
- Or comment out the `r-path` setting to use system R
- Or create a symlink if working across multiple machines

### Conda Environment Typo
The `smm635.yaml` file contains a typo: `sependencies` instead of `dependencies`. Despite this typo, conda correctly interprets it. If recreating the environment file, use the correct spelling.

### Directory Structure Quirk
There's a directory named `cd ../` in `website/weeks/` which appears to be a directory naming accident. Be careful not to confuse this with the bash command when navigating the file system.

### Large Datasets
The `data/ecar.csv` file is 10MB+ in size. When working with this dataset in code examples, consider performance implications and potentially use data sampling for demonstrations.
