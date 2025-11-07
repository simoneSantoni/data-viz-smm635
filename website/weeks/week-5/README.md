# Week 5: Storytelling and Crop Residue Case

## Overview

This week focuses on data storytelling principles using the Crop Residue Management (CRM) case study from IIM Bangalore. Students learn how to use data visualization and narrative techniques to communicate insights effectively.

## Materials Included

### 📖 Prepare
- Review Week 3 EDA materials
- Read the CRM case study (available on Moodle)

### 👥 Participate

1. **[case_discussion.qmd](case_discussion.qmd)** → `case_discussion.html`
   - 5-slide presentation introducing the case
   - Problem: Air pollution from crop residue burning
   - Solution: CII's sustainable alternatives initiative
   - Discussion questions for class engagement

2. **[teaching_summary.qmd](teaching_summary.qmd)** → `teaching_summary.html`
   - 26-slide comprehensive teaching guide
   - Covers all concepts from teaching notes
   - Seven data story types
   - Visualization best practices
   - Interactive examples and exercises

### 💻 Practice
- Introduction to data storytelling principles
- Building effective narratives with data visualization

### 📝 Perform

1. **[perform_1.qmd](perform_1.qmd)** → `perform_1.html`
   - Comprehensive EDA using R and tidyverse
   - Data cleaning with janitor
   - Visualizations with ggplot2
   - Analysis of farmer adoption patterns
   - Feedback analysis on sustainable practices

2. **[perform_1_python.qmd](perform_1_python.qmd)** → `perform_1_python.html`
   - Same analysis using Python
   - pandas for data manipulation
   - matplotlib and seaborn for visualizations
   - Identical structure to R version for comparison

### 📚 Ponder
- Essential readings on data storytelling
- Academic papers on narrative visualization

## Key Learning Objectives

By the end of this week, students should be able to:

1. Apply the seven-stage visualization process (Acquire → Interact)
2. Distinguish between exploratory and explanatory visualization
3. Use the seven basic data story types effectively
4. Create compelling narratives using data
5. Apply visualization best practices
6. Build interactive visualizations for stakeholder engagement

## Dataset

**File:** `data/crm.xlsx` (located at repository root)

**Contents:**
- 1,599 farmer records
- Variables: farmer_id, state, district, land, crm_type
- Methods: soil_incorporation, mulching, collection, others
- Burning indicators: complete_burning, partial_burning
- Feedback: pest_infestation, weed_infestation, water_consumption, fertiliser_consumption

**Geographic Coverage:**
- States: Punjab, Haryana
- Districts: Ludhiana, Patiala, Sirsa, Fatehabad, and others

## Key Insights from the Data

1. **High Adoption Rate:** Over 80% of farmers adopted sustainable practices
2. **Regional Variation:** Different districts prefer different CRM methods
3. **Positive Impacts:**
   - 69-71% reduction in water consumption
   - 60-80% reduction in fertilizer consumption
   - 33-53% reduction in weed infestation
4. **Tool Access:** Rotavator most common due to availability, not efficiency
5. **Scale:** Program expanded from 19 villages (2019) to 226 villages (2021)

## Technical Requirements

### R Version
- tidyverse (dplyr, ggplot2, tidyr)
- readxl
- janitor
- scales
- knitr

### Python Version
- pandas
- numpy
- matplotlib
- seaborn

### Visualization Tools (Optional)
- Tableau Public
- Power BI Desktop

## File Structure

```
week-5/
├── main.qmd                    # Weekly overview with links
├── case_discussion.qmd         # 5-slide case introduction
├── teaching_summary.qmd        # 26-slide teaching guide
├── perform_1.qmd              # R/tidyverse EDA
├── perform_1_python.qmd       # Python/pandas EDA
├── main-1.pdf                 # Case study document
└── README.md                  # This file
```

## Rendering Instructions

From the repository root:

```bash
cd website
quarto render weeks/week-5/main.qmd
quarto render weeks/week-5/case_discussion.qmd
quarto render weeks/week-5/teaching_summary.qmd
quarto render weeks/week-5/perform_1.qmd
quarto render weeks/week-5/perform_1_python.qmd
```

Or render all at once:
```bash
cd website
quarto render
```

## Teaching Notes

This week is designed for a 90-minute session:
- **30% Theory** (27 minutes): Data visualization concepts, story types
- **70% Practice** (63 minutes): Hands-on with Tableau/Power BI/R/Python

**Recommended Flow:**
1. Present case_discussion.qmd (10 min)
2. Discuss teaching_summary.qmd key concepts (15 min)
3. Demonstrate EDA with perform_1.qmd (20 min)
4. Students practice creating visualizations (30 min)
5. Wrap-up and Q&A (15 min)

## Assessment Connections

This week prepares students for:
- **Mid-term Project (50%):** Team-based visualization project
- **Final Project (40%):** Individual visualization project

Students should apply storytelling principles learned here to their project presentations.

## References

### Books
- Knaflic, C.N. (2015). *Storytelling with Data*
- Sringeswara, S. et al. (2022). *Data Visualization and Storytelling*

### Papers
- Segel, E., & Heer, J. (2010). Narrative Visualization: Telling Stories with Data
- Schwabish, J.A. (2014). An Economist's Guide to Visualizing Data

### Case Source
- IIM Bangalore Case IMB 959 & IMB 960 (Teaching Note)
- Data Storytelling: What are the Alternatives to Crop Residue Burning in India?

---

**Note:** All materials follow the 5P structure (Prepare, Participate, Practice, Perform, Ponder) consistent with other weeks in the course.
