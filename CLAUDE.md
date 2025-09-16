# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the SMM635 Data Visualization course repository, containing:
- A Quarto website in the `/website` directory
- Course materials organized by week
- Conda environment specification for the course
- Resources for teaching data visualization using Python and R

## Common Development Tasks

### Building and Previewing the Website

```bash
cd website
quarto render         # Build the website
quarto preview        # Live preview with hot reload
```

### Adding New Content

1. **New Week Materials**: Create `website/weeks/week-XX.qmd` following the pattern in `week-01.qmd`
2. **New Pages**: Add `.qmd` files and update `_quarto.yml` navigation
3. **Lab Materials**: Store in `website/labs/` directory
4. **Slides**: Store in `website/slides/` directory

### Modifying Styles

- Light theme: Edit `website/theme.scss`
- Dark theme: Edit `website/theme-dark.scss`
- Use existing CSS classes for consistency

### Working with the Conda Environment

```bash
# Activate the course environment
conda activate smm635

# Update environment from yaml
conda env update -f resources/smm635.yaml

# Export current environment
conda env export > resources/smm635.yaml
```

## Code Architecture

### Website Structure
```
website/
├── _quarto.yml          # Main configuration - navigation, metadata
├── index.qmd            # Homepage
├── course-*.qmd         # Course information pages
├── computing-*.qmd      # Technical setup guides
├── project-*.qmd        # Project instructions
├── weeks/               # Weekly materials
├── supplemental/        # Extra resources
├── theme*.scss          # Custom styling
└── _site/              # Generated output (do not edit)
```

### Key Configuration Points

1. **Navigation**: Defined in `_quarto.yml` under `website.sidebar.contents`
2. **Theming**: Uses Cosmo base theme with custom SCSS overrides
3. **Code Highlighting**: Enabled with copy buttons
4. **Search**: Built-in search functionality enabled

### Content Patterns

- Use `.callout-*` classes for highlighted information boxes
- Use `.week-card` for weekly overview sections
- Use `.assignment-badge` for lab/homework indicators
- Tables use responsive Bootstrap styling

## Development Workflow

1. Make changes to `.qmd` files or configuration
2. Run `quarto preview` to see live changes
3. Test both light and dark themes
4. Ensure all links work (internal and external)
5. Commit changes with descriptive messages

## Testing

Before committing:
- Run `quarto render` to ensure no build errors
- Check for broken links in the warnings
- Verify responsive design on mobile viewport
- Test interactive elements if added

## Data Visualization Course Specifics

This course covers:
- Python visualization (matplotlib, seaborn, plotly, altair)
- R visualization (ggplot2, plotly, shiny)
- Design principles and theory
- Interactive and static visualizations
- Real-world projects

When adding examples:
- Ensure code is reproducible
- Include both Python and R versions when possible
- Follow visualization best practices taught in the course
- Consider accessibility in all visualizations

## Important Notes

- The main branch is `master` (not `main`)
- The repository went through a "Spring cleaning" - most historical content was removed
- Focus on creating new, high-quality content rather than recovering old materials
- Maintain consistency with the established visual design and navigation structure