Write-Host "Lucas Fulmer, Powershell Portscanner"
$Computername = $args[0]
$startPort = $args[1]
$endPort = $args[2]

$TCPTimeout = 1 #timeout in milliseconds
#Increase waiting for response when physically farther away

For ($Item = $startPort; $Item -le $endPort; $Item++)
{
    $TCPClient = New-Object System.Net.Sockets.TCPClient
    $AsyncResult = $TCPClient.BeginConnect($Computername,$Item,$null,$null)
    $Wait = $AsyncResult.AsyncWaitHandle.WaitOne($TCPTimeout)

       If ($Wait)
        {
            $Null = $TCPClient.EndConnect($AsyncResult)
            If ($TCPClient.Connected)
            {
                Write-Host "$Item`tOpen"
            }
        }
}

Write-Host "Complete"