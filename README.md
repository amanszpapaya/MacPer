# MacPer
A python based tool that executes various CVEs to gain root privileges on various MAC OS platforms. Not all of the exploits directly spawns a root shell some of them executes commands as root and stores results in various locations. 

NOTE: This study was inspired by the study of rootos by Aiden Holland (thehappydinoa). 


## CVE LIST

|Name                | CVE           | Target OSX Version  | Reference                                                                                            |
| -------------      |:-------------:| -------------------:|:----------------------------------------------------------------------------------------------------:|
| WiFi Velocity LPE  | CVE-2021-30655| 10.16               | https://wojciechregula.blog/post/press-5-keys-and-become-root-aka-cve-2021-30655/                    |
| Keysteal LPE       | CVE-2019-8526 | 10.14.3             |https://github.com/LinusHenze/Keysteal                                                                |
| HideMyAss VPN LPE  | -             | 10.11               |https://www.securify.nl/advisory/multiple-local-privilege-escalation-vulnerabilities-in-hidemyass-pro-vpn-client-v2x-for-os-x|
| mount_apfs TCC LPE |CVE-2020-9771  | 10.15.3.            |https://theevilbit.github.io/posts/cve_2020_9771/                                                     |       
| TeamViewer LPE     |-              | 10.16               |https://theevilbit.github.io/posts/teamviewer_lpe/                                                    |
| Baron Samedit      |CVE-2021-3156  | 10.14.6             |https://twitter.com/hackerfantastic/status/1356645638151303169                                        |

## Installation
```
pip3 install -r requirements.txt
```
## Usage
