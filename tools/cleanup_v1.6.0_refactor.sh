#!/bin/bash
# EMSTrainer Repository Cleanup Script
# Removes obsolete files and directories from v1.6.0 refactor

echo "EMSTrainer Repository Cleanup"
echo "=============================="
echo ""
echo "This will DELETE obsolete files and directories."
echo "Git history will preserve everything if you need it back."
echo ""
read -p "Continue? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "Cancelled."
    exit 0
fi

echo ""
echo "Removing obsolete files..."

# Old release packages
rm -rf emstrainer_v1.5.6.2_full_install_package_with_index/
rm -rf emstrainer_partner_names_restore_v1/
rm -f emstrainer_partner_names_restore_v1.zip
rm -rf emstrainer_release_v1.5.6.2_notes_and_guardrail/

# Duplicate scenario in root
rm -f code_blackout_scenario.json

# Old documentation archives
rm -rf docs/archive/
rm -rf docs/imports/v1.5.2/

# Empty/unused folders
rm -rf exports/ 2>/dev/null
rm -rf scenario/ 2>/dev/null
rm -rf study/ 2>/dev/null
rm -rf test/ 2>/dev/null

# Old validation artifacts
rm -f tools/expected_layout_v1.5.6.1.json

# Makefile if not using
read -p "Remove Makefile? (yes/no): " remove_make
if [ "$remove_make" = "yes" ]; then
    rm -f Makefile
fi

# Clean up .DS_Store files
find . -name ".DS_Store" -delete

echo ""
echo "Cleanup complete!"
echo ""
echo "Removed:"
echo "  - Old release packages"
echo "  - Documentation archives"
echo "  - Duplicate scenario file"
echo "  - Empty/unused folders"
echo "  - .DS_Store files"
echo ""
echo "Run 'git status' to see what was removed."
echo "To commit: git add -A && git commit -m 'Clean up obsolete files from v1.6.0 refactor'"
