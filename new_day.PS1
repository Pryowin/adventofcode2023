Param(
    $day
)

$path = ".\" + $day
$new_file = $path + "\" + $day + ".py"
$new_test_file = $path + "\" + "test.txt"
$new_input_file = $path + "\" + "input.txt"
$new_pytest_file = $path + "\test_" + $day + ".py"
$import_command = "import " + $day + "`n"

If (!(Test-Path -Path $path)) {
    New-Item -Path $path -Type Directory
    Write-Host "New folder created successfully" -f Green
}
Else {
    Write-Host "Folder already exists" -f Yellow
}

If (!(Test-Path -Path $new_file)) {
    Copy-Item ".\python_modules\advent_template.py" -Destination $new_file
    Write-Host "Python file created successfully!" -f Green
}
Else {
    Write-Host "Python file already exists" -f Yellow
}

If (!(Test-Path -Path $new_test_file)) {
    New-Item -Name $new_test_file -ItemType File
    Write-Host "Test input created successfully!" -f Green
}
Else {
    Write-Host "Test input file already exists" -f Yellow
}

If (!(Test-Path -Path $new_input_file)) {
    New-Item -Name $new_input_file -ItemType File
    Write-Host "Input file created successfully!" -f Green
}
Else {
    Write-Host "Input file already exists" -f Yellow
}   

If (!(Test-Path -Path $new_pytest_file)) {
    New-Item -Name $new_pytest_file -ItemType File
    Add-Content -Path $new_pytest_file -Value($import_command)
    Write-Host "Unit test module created successfully!" -f Green
}
Else {
    Write-Host "Unit test module already exists" -f Yellow
}

