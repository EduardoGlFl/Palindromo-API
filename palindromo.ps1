$Palindromo = Read-Host -Prompt "Ingrese una palabra: "

$folder = Read-Host -Prompt "Folder location: "

$FileName = Read-Host -Prompt "File name: "

$Path = $folder + "\\" + $FileName + ".txt"

Invoke-RestMethod "https://flask-app-6dcwzidtya-uc.a.run.app/palindromos/$Palindromo" | Out-File -Encoding utf8 -FilePath "$Path"
