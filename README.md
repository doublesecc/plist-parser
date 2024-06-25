# plist-parser

## Overview
`plist parser` is a python script to parse Info.plist files, convert them into JSON format and print to stdout.

Info.plist files can be found in two formats:
- XML
- Binary

After unzipping the IPA, the XML format is often easy enough to read, but the binary file is not.

## Checking File Type
A quick check is to try and open the file, it will be immediately clear if its XML or Binary data.

However, you can also utilise some LOLbins tell you.

### File
You can use `file` to check.
```zsh
$ file Info.plist
Info.plist: Apple binary property list
```
> **Note:**
> `Apple binary property list` confirms it is a binary file type

### Cat
You can view the magic bytes of the file.
``` zsh
$ cat Info.plist
bplist00


5#678:ABCDECFGHIJKNORUmnpr_BuildMachineOSBuild_CFBundleDevelopmentRegion_CFBundleExecutable]CFBundleIcons_CFBundleIcons~ipad_CFBundleIdentifier_CFBundleInfoDictionaryVersion\CFBundleName_CFBundlePackageType_CFBundleShortVersionString_CFBundleSupportedPlatforms_CFBundleURLTypes_CFBundleVersionZDTCompiler_DTPlatformBuild^DTPlatformName_DTPlatformVersionZDTSDKBuildYDTSDKNameWDTXcode\DTXcodeBuild_LSRequiresIPhoneOS_MinimumOSVersion_NSAppTransportSecurity_NSCameraUsageDescriptionZUIAppFonts^UIDeviceFamily^UILaunchImages_UIMainStoryboardFile_UIRequiredDeviceCapabilities_ UISupportedInterfaceOrientations_%UISupportedInterfaceOrientations~ipadU17D47RenWDVIA-v2%&_CFBundlePrimaryIcon'()._CFBundleIconFiles_CFBundleIconName*+,-\AppIcon20x20\AppIcon29x29\AppIcon40x40\AppIcon60x60WAppIcon%0'(1.*+,-23\AppIcon76x76_AppIcon83.5x83.5_!com.highaltitudehacks.DVIAswiftv2S6.0TAPPLS2.09XiPhoneOS;<=4>_CFBundleURLName_CFBundleURLSchemes?@TdviaYdviaswiftQ1_"com.apple.compilers.llvm.clang.1_0V15C107XiphoneosT11.2\iphoneos11.2T0920U9C40b  T10.0LI_NSAllowsArbitraryLoads _ETo demonstrate the misuse of Camera, please grant it permission once.PQZAvenir.ttc_HelveticaNeue.ttcSTV_cfjWXYZ[\]^_UILaunchImageMinimumOSVersion_UILaunchImageName_UILaunchImageOrientation_UILaunchImageSizeT11.0_LaunchImage-1100-Portrait-2436hXPortraitZ{375, 812}WXYZ`a]bS8.0_LaunchImage-800-Portrait-736hZ{414, 736}WXYZ`d]e_LaunchImage-800-667hZ{375, 667}WXYZgh]iS7.0_LaunchImage-700-568hZ{320, 568}WXYZgk]l_LaunchImage-700-Portrait[{768, 1024}TRootoUarm64q_UIInterfaceOrientationPortraitqstu_(UIInterfaceOrientati*GZlw2=L[rUpsideDown_#UIInterfaceOrientationLandscapeLeft_$UIInterfaceOrientationLandscapeRighKa}
          27DQ^ksv{
                    ELUZglrsx{
                              5Idx}
                                   #:ENiuz|v"%
```
> **Note:**
> See that `bplist00` is on the first line of the output

# Usage
``` zsh
python3 /opt/github/plist-parser/plist_parser.py -f <Info.plist>
```

### Example Output
This example output is from the IPA [DVIA-v2](https://github.com/prateek147/DVIA-v2).

``` zsh
$ python3 /opt/github/plist-parser/plist_parser.py -f Info.plist
{
    "BuildMachineOSBuild": "17D47",
    "CFBundleDevelopmentRegion": "en",
    "CFBundleExecutable": "DVIA-v2",
    "CFBundleIcons": {
        "CFBundlePrimaryIcon": {
            "CFBundleIconFiles": [
                "AppIcon20x20",
                "AppIcon29x29",
                "AppIcon40x40",
                "AppIcon60x60"
            ],
            "CFBundleIconName": "AppIcon"
        }
    },
    "CFBundleIcons~ipad": {
        "CFBundlePrimaryIcon": {
            "CFBundleIconFiles": [
                "AppIcon20x20",
                "AppIcon29x29",
                "AppIcon40x40",
                "AppIcon60x60",
                "AppIcon76x76",
                "AppIcon83.5x83.5"
            ],
            "CFBundleIconName": "AppIcon"
        }
    },
    "CFBundleIdentifier": "com.highaltitudehacks.DVIAswiftv2",
    "CFBundleInfoDictionaryVersion": "6.0",
    "CFBundleName": "DVIA-v2",
    "CFBundlePackageType": "APPL",
    "CFBundleShortVersionString": "2.0",
    "CFBundleSupportedPlatforms": [
        "iPhoneOS"
    ],
    "CFBundleURLTypes": [
        {
            "CFBundleURLName": "com.highaltitudehacks.DVIAswiftv2",
            "CFBundleURLSchemes": [
                "dvia",
                "dviaswift"
            ]
        }
    ],
    "CFBundleVersion": "1",
    "DTCompiler": "com.apple.compilers.llvm.clang.1_0",
    "DTPlatformBuild": "15C107",
    "DTPlatformName": "iphoneos",
    "DTPlatformVersion": "11.2",
    "DTSDKBuild": "15C107",
    "DTSDKName": "iphoneos11.2",
    "DTXcode": "0920",
    "DTXcodeBuild": "9C40b",
    "LSRequiresIPhoneOS": true,
    "MinimumOSVersion": "10.0",
    "NSAppTransportSecurity": {
        "NSAllowsArbitraryLoads": true
    },
    "NSCameraUsageDescription": "To demonstrate the misuse of Camera, please grant it permission once.",
    "UIAppFonts": [
        "Avenir.ttc",
        "HelveticaNeue.ttc"
    ],
    "UIDeviceFamily": [
        1,
        2
    ],
    "UILaunchImages": [
        {
            "UILaunchImageMinimumOSVersion": "11.0",
            "UILaunchImageName": "LaunchImage-1100-Portrait-2436h",
            "UILaunchImageOrientation": "Portrait",
            "UILaunchImageSize": "{375, 812}"
        },
        {
            "UILaunchImageMinimumOSVersion": "8.0",
            "UILaunchImageName": "LaunchImage-800-Portrait-736h",
            "UILaunchImageOrientation": "Portrait",
            "UILaunchImageSize": "{414, 736}"
        },
        {
            "UILaunchImageMinimumOSVersion": "8.0",
            "UILaunchImageName": "LaunchImage-800-667h",
            "UILaunchImageOrientation": "Portrait",
            "UILaunchImageSize": "{375, 667}"
        },
        {
            "UILaunchImageMinimumOSVersion": "7.0",
            "UILaunchImageName": "LaunchImage-700-568h",
            "UILaunchImageOrientation": "Portrait",
            "UILaunchImageSize": "{320, 568}"
        },
        {
            "UILaunchImageMinimumOSVersion": "7.0",
            "UILaunchImageName": "LaunchImage-700-Portrait",
            "UILaunchImageOrientation": "Portrait",
            "UILaunchImageSize": "{768, 1024}"
        }
    ],
    "UIMainStoryboardFile": "Root",
    "UIRequiredDeviceCapabilities": [
        "arm64"
    ],
    "UISupportedInterfaceOrientations": [
        "UIInterfaceOrientationPortrait"
    ],
    "UISupportedInterfaceOrientations~ipad": [
        "UIInterfaceOrientationPortrait",
        "UIInterfaceOrientationPortraitUpsideDown",
        "UIInterfaceOrientationLandscapeLeft",
        "UIInterfaceOrientationLandscapeRight"
    ]
}
```

You can now combine this JSON output with other tooling to extract information of interest.

Some examaples:

Combine with jq to check the Minimum Supported OS Version:
``` zsh
$ python3 /opt/github/plist-parser/plist_parser.py -f Info.plist | jq -r '.MinimumOSVersion'
10.0
```

Combine with grep and cut to check the Minimum Supported OS Version:
``` zsh
$ python3 /opt/github/plist-parser/plist_parser.py -f Info.plist | grep '"MinimumOSVersion"' | cut -f 4 -d '"'
10.0
```

Combine with jq to check if anything is declared in NSAppTransportSecurity:
``` zsh
$ python3 /opt/github/plist-parser/plist_parser.py -f Info.plist | jq -r '.NSAppTransportSecurity'
{
  "NSAllowsArbitraryLoads": true
}
```
