# Release Notes

## Release Date: 08/05/2020 | Build: 1.0.20200731.2336

### New Features and Fixes
- SoftAP SSID changed to a more unique name (scz-<last 4 hex digits of wmac>)
- OOBE updates
	- OOBE now waits for modules to start before showing the last screen
	- Added link to be able to view the camera stream at the end of OOBE
	- Added redirect to Azure Edge Devices portal to last screen
	- Updated EULA page
- Updated the hostname to include "scz-" at the front
- Moved to a UEFI-based carrier board image
- Enabled Secure Boot and Update Verification with secure Private Preview keys
- Added Preloaded Containers so that devices doesn’t have to download them at the end of OOBE
- Added pushing Update images to Azure Blob Storage
- Added Firmware and OS OTA update support
- Added Watchdog rollback support
- Deleted ffmpeg and apps that depended on ffmpeg from base image
- Added ability to trigger USB flash mode from OS and automatically from U-Boot recovery mode
- Various bug fixes
