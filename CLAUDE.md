# Claude Context - pySUPERMEATBOY Project

## Project Paths

### Local Development
- **Main Directory**: `/Users/andle/Desktop/pyDOOM/`
- **Game File**: `pySUPERMEATBOY.py`
- **Virtual Environment**: `~/pygame_env/` (for pygame installation)

### NAS Storage
- **NAS IP**: `192.168.4.82`
- **SSH Access**: `ssh andle@192.168.4.82`
- **Project Path on NAS**: `/testandleNAS/5_Projects/Active_Development/pySUPERMEATBOY/`
- **Full NAS Path from root**: `/volume1/testandleNAS/5_Projects/Active_Development/pySUPERMEATBOY/`
- **SMB Path**: `smb://ANDLENAS._smb._tcp.local/testandleNAS`

## Important Notes
- Git is NOT installed on the NAS
- Use SCP for file transfers to NAS
- The path from SSH home is `/testandleNAS/` not `/volume1/testandleNAS/`

## Sync Commands

### Copy to NAS
```bash
scp pySUPERMEATBOY.py andle@192.168.4.82:/testandleNAS/5_Projects/Active_Development/pySUPERMEATBOY/
```

### Pull from NAS
```bash
scp andle@192.168.4.82:/testandleNAS/5_Projects/Active_Development/pySUPERMEATBOY/pySUPERMEATBOY.py .
```

### SSH to NAS
```bash
ssh andle@192.168.4.82
cd /testandleNAS/5_Projects/Active_Development/pySUPERMEATBOY/
```

## Development Workflow
1. Edit locally in `/Users/andle/Desktop/pyDOOM/`
2. Test with pygame environment: `source ~/pygame_env/bin/activate`
3. Run: `python3 pySUPERMEATBOY.py`
4. Sync to NAS: `./sync-to-nas.sh` or use scp command above

## Game Features Implemented
- Gravity physics (falls naturally)
- Floor collision detection
- Jumping mechanics (spacebar, only when on ground)
- Left/right movement (arrow keys)
- Visual floor line
- Red block character (100x100 pixels)

## Physics Variables
- gravity = 0.8
- jump_strength = -15
- floor_y = 400
- movement_speed = 5