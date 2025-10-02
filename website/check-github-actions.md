# GitHub Actions Not Running - Troubleshooting Guide

The workflow file exists and is properly committed, but it's not running. Here are the most likely causes:

## 1. Check if GitHub Actions is enabled

Go to: https://github.com/simoneSantoni/data-viz-smm635/settings/actions

Make sure:
- Actions are enabled for this repository
- "Allow all actions and reusable workflows" is selected

## 2. Check workflow runs page

Visit: https://github.com/simoneSantoni/data-viz-smm635/actions

- Do you see ANY workflows listed?
- Is there a "Publish SMM635 Website" workflow in the list?
- Are there any disabled workflows?

## 3. Check default branch

The workflow triggers on pushes to `master` branch. Verify:
- Is `master` the default branch? (not `main`)
- Go to: https://github.com/simoneSantoni/data-viz-smm635/settings
- Check "Default branch" setting

## 4. Manual trigger test

If Actions are enabled, try manually triggering:
1. Go to: https://github.com/simoneSantoni/data-viz-smm635/actions/workflows/publish.yml
2. Click "Run workflow" button
3. Select `master` branch
4. Click "Run workflow"

## 5. Check repository permissions

Ensure you have admin access to:
- Enable/disable Actions
- Modify workflow permissions
- Access repository settings

## Quick Fix Attempts:

1. **Force workflow detection** - Make a small change to the workflow file:
   ```bash
   # Edit the workflow file to add a comment
   # Then commit and push
   ```

2. **Check for .github in .gitignore**:
   ```bash
   cat ../.gitignore | grep github
   ```

Let me know what you find in the Actions settings page!