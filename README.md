# Data Visualization (SMM635) ― README

This is the GitHub repository for the course Data Visualization, SMM635. The
repository is actively maintained and will be updated throughout the term.

## Course Website

The course website contains comprehensive materials including lectures,
assignments, and interactive visualizations. Visit the [course
website](https://simonesantoni.github.io/data-viz-smm635/) for the complete
learning experience.

### Latest Updates

- **🎯 Week 1 Complete**: Interactive presentation on design principles and processes
- **📊 Design Principles Guide**: Comprehensive coverage of:
  - Tufte's principles of graphical excellence
  - The grammar of graphics framework
  - Visual perception and chart junk identification
  - Before/after redesign examples
- **🎨 Interactive Materials**: RevealJS presentation with visual examples
- **📚 Updated Bibliography**: Essential readings from Tufte, Cairo, Wilkinson, and Healy

## Repository Structure

```
├── website/                    # Quarto website source
│   ├── weeks/                 # Weekly course materials
│   │   └── week-1/           # Week 1: Design principles
│   │       ├── main.qmd      # Week overview
│   │       ├── design-principles-presentation.qmd  # Interactive slides
│   │       ├── presentation-styles.css            # Custom styling
│   │       └── images/       # Presentation assets
│   ├── course/               # Course information
│   │   ├── syllabus.qmd     # Complete syllabus
│   │   ├── team.qmd         # Teaching team
│   │   └── schedule.qmd     # Course schedule
│   ├── project/             # Course projects
│   ├── imgs/                # Icons and branding
│   ├── theme.scss           # Light theme styling
│   ├── theme-dark.scss      # Dark theme styling
│   └── _site/               # Generated website files
├── _background_/            # Background materials and references
│   └── beamers/            # LaTeX presentation sources
│       └── design/         # Design principles materials
├── data/                   # Course datasets
├── smm635.yaml            # Conda environment file
└── README.md              # This file
```

## Course Overview

### Why Data Visualization?

Data is everywhere, but raw data alone doesn't tell stories. Effective data visualization
transforms complex information into clear, compelling narratives that drive decisions.
This module provides students with fundamental design principles, practical tools,
and hands-on experience in creating impactful visualizations. Students will learn
to apply the grammar of graphics, design effective charts, and build interactive
dashboards. Ultimately, the goal is to develop skills in transforming data into
actionable insights through thoughtful visual design.

### Course Topics (10 weeks)

1. **Week 1**: Designing charts: processes and principles
2. **Week 2**: Design variables and the grammar of graphics
3. **Week 3**: Exploratory data analysis and Nomis Solutions case
4. **Week 4**: Multidimensional data visualization and Saving Lives with Data case
5. **Week 5**: Storytelling and Crop Residue case
6. **Week 7**: Introduction to Tableau (Part 1)
7. **Week 8**: Introduction to Tableau (Part 2) and Accounting case
8. **Week 9**: Dashboards with Tableau (Part 1)
9. **Week 10**: Dashboards with Tableau (Part 2) and Market Street Wine case

### Learning Objectives

By the end of this module, students will be able to:

- **Design Foundation**: Understand fundamental principles of effective data visualization design
- **Technical Skills**: Apply the grammar of graphics to create meaningful visualizations
- **Tool Proficiency**: Design appropriate charts for different data types and analytical goals
- **Interactive Development**: Create interactive visualizations and dashboards using modern tools
- **Professional Implementation**: Leverage Python libraries and Tableau for professional visualizations
- **Communication**: Apply storytelling techniques to communicate data insights effectively
- **Business Application**: Produce elegant, effective visual solutions to practical problems in business analytics

## Technical Requirements

### Software Setup

- **R** (version 4.3+) with RStudio
- **Python** (version 3.9+) with Jupyter Lab
- **Tableau** (student license provided)
- Git for version control

### Environment Setup

Create the course environment using the provided configuration:

```bash
conda env create -f smm635.yaml
conda activate smm635
```

### Key Libraries

**R Packages:**

- `ggplot2`, `plotly`, `shiny` for visualizations
- `tidyverse` for data manipulation
- `viridis`, `RColorBrewer` for color schemes

**Python Libraries:**

- `matplotlib`, `seaborn`, `plotly` for plotting
- `pandas`, `numpy` for data handling
- `altair`, `bokeh`, `dash` for interactive visualizations

## Assessment

- **Class Participation** (10%): Active engagement and critique contributions
- **Mid-term Project** (50%): Team-based visualization project - Due November 11, 2025
- **Final Project** (40%): Individual visualization project - Due December 11, 2025

## Essential Readings

1. **Tufte, E. R. (1983).** _The visual display of quantitative information_
2. **Cairo, A. (2012).** _The Functional Art: An introduction to information graphics and visualization_
3. **Wilkinson, L. (2011).** _The grammar of graphics_
4. **Healy, K. (2024).** _Data visualization: a practical introduction_

## Getting Started

1. **Clone this repository**:

   ```bash
   git clone https://github.com/simoneSantoni/data-viz-smm635.git
   ```

2. **Set up environment**:

   ```bash
   conda env create -f smm635.yaml
   conda activate smm635
   ```

3. **Visit the course website**: [https://simonesantoni.github.io/data-viz-smm635](https://simonesantoni.github.io/data-viz-smm635)

4. **Start with Week 1**: Review the design principles presentation and complete the exercises

## Support

- **Office Hours**: Wednesdays 15:00-17:00 (by appointment)
- **Email**: [simone.santoni.1@city.ac.uk](mailto:simone.santoni.1@city.ac.uk)
- **Course Forum**: Available on Moodle

## Contributing

This repository is actively maintained. Students are encouraged to:

- Report issues with course materials
- Suggest improvements to visualizations
- Share interesting data visualization resources

---

**📊 Ready to transform data into compelling visual stories? Let's begin!**
