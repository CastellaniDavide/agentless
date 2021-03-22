﻿# Variabiles
$toolsDir   = "$(Split-Path -parent $MyInvocation.MyCommand.Definition)"
$ppath = "C:\Progra~1\agentless"
$exepath = "$ppath\agentless.exe"
echo "My personal path is: $ppath"
echo "My exe path id $exepath"

# Set folder
New-Item -ItemType Directory -Force -Path $ppath
Copy-Item "$toolsDir\agentless.exe" "$ppath\agentless.exe"

# Add Path
$new_path = (Get-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment' -Name PATH).path
if ($new_path -notlike "*$ppath*")
{
	$new_path += ";$ppath"
	$new_path = $new_path.Replace(";;", ";")
	Set-ItemProperty -Path 'Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment' -Name PATH -Value $new_path
}

# Installing pypi
pip.exe install agentless
