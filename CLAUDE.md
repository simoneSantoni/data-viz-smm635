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
# The .deployment-trigger file is a legacy artifact from previous deployment setup
```

## Architecture and Structure

### Quarto Website Architecture
The website uses Quarto's multi-format publishing system with custom output configuration:
- **_quarto.yml**: Main configuration defining site structure, sidebar navigation, and theming
  - **Critical**: `output-dir: _site` publishes to `website/_site`
  - GitHub Actions deploys from `website/_site` to GitHub Pages
  - Sidebar has 10 weeks of content plus course info and project sections
- **_site/**: Generated static website output (git-tracked, do not manually edit)
- **_freeze/**: Quarto's computational cache for executed code (enabled with `freeze: auto`)
- **.quarto/**: Internal Quarto metadata and indexing

### Content Organization
- **website/weeks/**: Weekly course materials following the 5P structure:
  - Each week has a `main.qmd` with: Prepare, Participate, Practice, Perform, Ponder sections
  - Additional topic-specific `.qmd` files (e.g., `design-principles-presentation.qmd`)
  - Supporting assets in `images/` subdirectories
  - **Note**: There's an unusual `cd ../` directory within weeks/ - appears to be a directory naming accident
- **website/course/**: Core course documents (syllabus, schedule, support, team)
- **website/project/**: Mid-term and final project specifications in subdirectories
- **website/notes/**: Supplemental learning materials
- **website/imgs/**: Icons and branding assets (e.g., `r-module-icon-light.svg`)
- **data/**: Course datasets (e.g., `crm.xlsx`) - located at repository root, not in website/

### Theming System
- **Dual theme support**: `theme.scss` (light) and `theme-dark.scss` (dark)
  - Base: Cosmo from Bootswatch
  - Custom fonts: Atkinson Hyperlegible (specified in `_quarto.yml: mainfont`)
- **RevealJS presentations**: Separate styling in `presentation-styles.css` (e.g., week-1)
- **Theme switcher**: JavaScript-based theme toggle via `theme-switcher.js`

### R Configuration
Quarto is configured to use a specific R installation from the conda environment:
- `r-path: /home/simon/miniconda3/envs/smm635/bin/R` in `_quarto.yml`
- Jupyter kernelspec points to "ir" (R kernel) with display name "R (ind215)"
- When working on different machines, this path may need adjustment

### Key Technologies
- **Quarto**: Static site generator with support for executable R/Python code blocks
- **RevealJS**: Interactive presentation framework for lectures (format: revealjs in YAML)
- **R/Python Integration**: Dual-language support via conda environment
- **Visualization Libraries**:
  - R: ggplot2, plotly, shiny, leaflet, gganimate, highcharter, treemap
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
- Special handling: Temporarily removes PDF format from syllabus during CI build
- Deploys from `website/_site` to GitHub Pages

## Common Issues

### R Path Configuration
The `_quarto.yml` contains a hardcoded R path specific to one machine:
```yaml
r:
  r-path: /home/simon/miniconda3/envs/smm635/bin/R
```
If working on a different machine, either:
- Update this path to match your conda environment, or
- Comment out the `r-path` setting to use system R

### Conda Environment Typo
The `smm635.yaml` file contains a typo: `sependencies` instead of `dependencies`. Despite this typo, conda correctly interprets it. If recreating the environment file, use the correct spelling.

### Working with Presentations
When creating new RevealJS presentations:
1. Set `format: revealjs` in YAML front matter
2. Render the presentation: `quarto render presentation-file.qmd`
3. The output will be `presentation-file.html`
4. Link to it from the week's `main.qmd` using relative path
5. Do not use `quarto preview` for presentations - it may not work correctly. Use `quarto render` and open the HTML file directly.