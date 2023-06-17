###### 1 choco setting
# It must be run as administrator. Fetching the permission.
If (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))
{   
    $arguments = "& '" + $myinvocation.mycommand.definition + "'"
    Start-Process powershell -Verb runAs -ArgumentList $arguments
    Break
}

$InstallDir='D:\ChocoPortable'
If (!(Test-Path $InstallDir))
{
    $env:ChocolateyInstall="$InstallDir"

    Set-ExecutionPolicy Bypass -Scope Process -Force

    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072

    Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
}



###### 2 install app
Write-Host 'Start to install...'

### System
Write-Host 'System...'
choco install microsoft-windows-terminal -y

### Version Control
Write-Host 'Version Control...'
choco install git -y --params "/WindowsTerminal"
choco install tortoisegit -y
choco install git-lfs -y

### Program language
Write-Host 'Program language...'
choco install python3 --version 3.7.2 -y

### IDE
Write-Host 'IDE...'
choco install PyCharm-community -y
choco install vscode -y

choco install visualstudio2022community -y --package-parameters "--passive
                                                              --add Microsoft.VisualStudio.Workload.NativeDesktop
                                                              --add Microsoft.VisualStudio.Workload.NativeGame;includeRecommended
                                                              --add Component.Unreal
                                                              --add Microsoft.Net.Component.4.6.TargetingPack
                                                              --add Microsoft.Net.Component.4.6.2.TargetingPack
                                                              --addProductLang En-us
                                                              --locale Zh-cn"

### Tools
Write-Host 'Tools...'
choco install mongodb --version=4.0.12 -y -f
choco install xmind -y
choco install drawio -y
choco install screentogif -y

###### Done
Write-Host "The softwares are installed."

pause