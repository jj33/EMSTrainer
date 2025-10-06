#!/bin/bash
# EMSTrainer - Common Cleanup Script
# Removes common development artifacts

echo "Cleaning common artifacts..."

# macOS files
find . -name ".DS_Store" -delete

# Python cache
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -name "*.pyc" -delete
find . -name "*.pyo" -delete

# Temp files
find . -name "*.tmp" -delete
find . -name "*.temp" -delete
find . -name "*.bak" -delete
find . -name "*~" -delete

# Log files
find . -name "*.log" -delete

echo "Common cleanup complete!"
echo "Removed: .DS_Store, Python cache, temp files, logs"
