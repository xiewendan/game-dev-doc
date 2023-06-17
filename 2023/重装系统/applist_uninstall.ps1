# It must be run as administrator. Fetching the permission.
If (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))
{   
    $arguments = "& '" + $myinvocation.mycommand.definition + "'"
    Start-Process powershell -Verb runAs -ArgumentList $arguments
    Break
}
Write-Host 'Start to install...'

# System
choco uninstall python3 --version 3.7.2 -y

# Done
Write-Host "Softwares installation complete"

pause