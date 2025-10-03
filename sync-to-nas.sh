#!/bin/bash

# pySUPERMEATBOY NAS Sync Script
# Syncs local development files to NAS storage

NAS_IP="192.168.4.82"
NAS_USER="andle"
NAS_PATH="/testandleNAS/5_Projects/Active_Development/pySUPERMEATBOY/"
LOCAL_PATH="/Users/andle/Desktop/pyDOOM/"

echo "====================================="
echo "pySUPERMEATBOY NAS Sync"
echo "====================================="
echo "Syncing to: $NAS_USER@$NAS_IP:$NAS_PATH"
echo ""

# Sync main game file
echo "• Uploading pySUPERMEATBOY.py..."
scp "${LOCAL_PATH}pySUPERMEATBOY.py" "$NAS_USER@$NAS_IP:$NAS_PATH"

# Sync documentation
echo "• Uploading README.md..."
scp "${LOCAL_PATH}README.md" "$NAS_USER@$NAS_IP:$NAS_PATH"

echo "• Uploading CLAUDE.md..."
scp "${LOCAL_PATH}CLAUDE.md" "$NAS_USER@$NAS_IP:$NAS_PATH"

echo ""
echo "✓ Sync complete!"
echo "====================================="