Import-Module ActiveDirectory
# Importing the AD

# Adding a user with all their information
New-ADUser -Name "Franz Ferdinand" -GivenName "Franz" -Surname "Ferdinand" -SamAccountName "F.Ferdinand" -UserPrincipalName "ferdi@GlobeXpower.com" -Title "TPS Reporting Lead" -Company "GlobeX USA" -Location "Springfield, OR"
