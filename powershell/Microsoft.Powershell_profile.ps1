##############################
# PATH                       #
##############################

$env:PATH += ":$HOME/dotfiles/powershell/Scripts/"
$env:PATH += ":$HOME/dotfiles/powershell/Scripts/gforces/"
$env:PATH += ":$HOME/dotfiles/powershell/Scripts/New-GforcesTour/"
$env:PATH += ":$HOME/dotfiles/powershell/Scripts/tours/"

##############################
# Functions                  #
##############################

function Global:prompt {"PS $($pwd.ProviderPath) `n> "}
function .. {Set-Location  ..}
function ... {Set-Location ../..}
function List-DirectoryAll {Get-ChildItem -Force | Format-Table -AutoSize}
function List-DirectoriesOnly {Get-ChildItem -Directory | Format-Table -AutoSize}
function List-FilesOnly {Get-ChildItem -File | Format-Table -AutoSize}
function List-DotFilesOnly {Get-ChildItem -File -Filter .* | Format-Table -AutoSize}
function Go-CarsDirectory {cd $HOME/virtual-tours/gforces/cars/}

##############################
# Alias                      #
##############################

Set-Alias ll Get-ChildItem
Set-Alias la List-DirectoryAll
Set-Alias ld List-DirectoriesOnly
Set-Alias lf List-FilesOnly
Set-Alias ldf List-DotFilesOnly
Set-Alias cc Clear-Host
Set-Alias sls Select-String
Set-Alias pro Reload-Profile
Set-Alias nf New-File
Set-Alias nd New-Directory
Set-Alias cars Go-CarsDirectory