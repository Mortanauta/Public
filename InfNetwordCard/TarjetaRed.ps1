Write-Output -InputObject ("                                                                                                          Ver:1.0")
Write-Output -InputObject ("    |\                                                    ")
Write-Output -InputObject ("    |_\                # Informe de tarjetas de red            ")
Get-NetAdapter | Select-Object @{name='Name'; Expression={$_.name}}, interfaceDescription, status, linkSpeed, macaddress | Sort-Object Name | Format-Table 
Write-Output -InputObject ("")
Write-Output -InputObject ("                       # Drivers de red        ")
Get-NetAdapter -Name * | Sort-Object name | Format-Table -View Driver
Pause
