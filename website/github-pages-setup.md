# GitHub Pages Setup Instructions

The website is built successfully but GitHub Pages needs to be enabled. Here's how to fix it:

## Steps to Enable GitHub Pages:

1. Go to https://github.com/simoneSantoni/data-viz-smm635/settings/pages

2. Under "Source", select:
   - **Source**: Deploy from a branch
   - **Branch**: Select "GitHub Actions" (not a branch)

3. If "GitHub Actions" is not available as an option:
   - First select "Deploy from a branch"
   - Then change it back to "GitHub Actions"

4. Save the settings

5. The workflow should automatically deploy on the next push

## Alternative: If GitHub Actions deployment is not working:

1. Check workflow runs at: https://github.com/simoneSantoni/data-viz-smm635/actions

2. Look for any failed "Publish SMM635 Website" runs

3. Click on a failed run to see error details

## Verify Permissions:

Make sure your repository has the correct permissions:
- Go to Settings > Actions > General
- Scroll to "Workflow permissions"
- Select "Read and write permissions"
- Check "Allow GitHub Actions to create and approve pull requests"
- Save

After following these steps, the site should be available at:
https://simonesantoni.github.io/data-viz-smm635/
EOF < /dev/null