# Feature-Sliced Design (FSD) Architecture Validation Script
# This PowerShell script validates FSD compliance for AI-assisted development

param(
    [string]$ProjectPath = ".",
    [switch]$Verbose
)

# Set error handling
$ErrorActionPreference = "Continue"

Write-Host "🍰 Feature-Sliced Design Validation Starting..." -ForegroundColor Cyan

# Counters
$script:Errors = 0
$script:Warnings = 0
$script:Checks = 0

# Helper functions
function Log-Error {
    param([string]$Message)
    Write-Host "❌ ERROR: $Message" -ForegroundColor Red
    $script:Errors++
}

function Log-Warning {
    param([string]$Message)
    Write-Host "⚠️  WARNING: $Message" -ForegroundColor Yellow
    $script:Warnings++
}

function Log-Success {
    param([string]$Message)
    Write-Host "✅ $Message" -ForegroundColor Green
}

function Log-Info {
    param([string]$Message)
    Write-Host "ℹ️  $Message" -ForegroundColor Blue
}

function Increment-Check {
    $script:Checks++
}

# Check if src directory exists
function Test-SrcStructure {
    Increment-Check
    $srcPath = Join-Path $ProjectPath "src"
    
    if (-not (Test-Path $srcPath -PathType Container)) {
        Log-Error "src/ directory not found. FSD requires src/ as root directory."
        return $false
    }
    Log-Success "src/ directory found"
    return $true
}

# Validate FSD layer structure
function Test-Layers {
    Increment-Check
    Log-Info "Validating FSD layer structure..."
    
    $requiredLayers = @("shared")
    $optionalLayers = @("app", "pages", "widgets", "features", "entities")
    $deprecatedLayers = @("processes")
    
    $srcPath = Join-Path $ProjectPath "src"
    
    # Check required layers
    foreach ($layer in $requiredLayers) {
        $layerPath = Join-Path $srcPath $layer
        if (-not (Test-Path $layerPath -PathType Container)) {
            Log-Error "Required layer missing: src/$layer/"
        } else {
            Log-Success "Required layer found: src/$layer/"
        }
    }
    
    # Check optional layers
    foreach ($layer in $optionalLayers) {
        $layerPath = Join-Path $srcPath $layer
        if (Test-Path $layerPath -PathType Container) {
            Log-Success "Optional layer found: src/$layer/"
        }
    }
    
    # Check for deprecated layers
    foreach ($layer in $deprecatedLayers) {
        $layerPath = Join-Path $srcPath $layer
        if (Test-Path $layerPath -PathType Container) {
            Log-Warning "Deprecated layer found: src/$layer/ (consider removing)"
        }
    }
}

# Validate segment structure within slices
function Test-Segments {
    Increment-Check
    Log-Info "Validating segment structure..."
    
    $standardSegments = @("ui", "model", "api", "lib", "config")
    $invalidSegments = @("components", "views", "store", "state", "services", "requests")
    
    $srcPath = Join-Path $ProjectPath "src"
    
    # Check for invalid segment names
    foreach ($segment in $invalidSegments) {
        $segmentDirs = Get-ChildItem -Path $srcPath -Recurse -Directory -Name $segment -ErrorAction SilentlyContinue
        if ($segmentDirs) {
            Log-Warning "Non-standard segment name found: '$segment'. Consider renaming to FSD standard."
        }
    }
    
    # Validate shared layer segments
    $sharedPath = Join-Path $srcPath "shared"
    if (Test-Path $sharedPath -PathType Container) {
        foreach ($segment in $standardSegments) {
            $segmentPath = Join-Path $sharedPath $segment
            if (Test-Path $segmentPath -PathType Container) {
                Log-Success "Standard segment in shared: $segment/"
            }
        }
    }
}

# Check import violations using pattern matching
function Test-ImportViolations {
    Increment-Check
    Log-Info "Checking for potential import violations..."
    
    $violationCount = 0
    $srcPath = Join-Path $ProjectPath "src"
    
    # Define layer hierarchy (higher numbers can't import from lower numbers)
    $layerLevels = @{
        "app" = 6
        "pages" = 5
        "widgets" = 4
        "features" = 3
        "entities" = 2
        "shared" = 1
    }
    
    # Get all TypeScript/JavaScript files
    $codeFiles = Get-ChildItem -Path $srcPath -Recurse -Include "*.ts", "*.tsx", "*.js", "*.jsx" -ErrorAction SilentlyContinue
    
    foreach ($file in $codeFiles) {
        # Determine current file's layer
        $currentLayer = $null
        foreach ($layer in $layerLevels.Keys) {
            if ($file.FullName -like "*src\$layer\*") {
                $currentLayer = $layer
                break
            }
        }
        
        if ($currentLayer) {
            $currentLevel = $layerLevels[$currentLayer]
            
            # Read file content and check imports
            try {
                $content = Get-Content $file.FullName -ErrorAction SilentlyContinue
                foreach ($line in $content) {
                    if ($line -match '^\s*import.*from\s+["\''](.*)["\'']\s*;') {
                        $importPath = $Matches[1]
                        
                        # Check if it's a layer import
                        foreach ($layer in $layerLevels.Keys) {
                            if ($importPath -like ($layer + "/*")) {
                                $importedLevel = $layerLevels[$layer]
                                
                                if ($currentLevel -le $importedLevel) {
                                    Log-Error "Import violation in $($file.FullName): $currentLayer cannot import from $layer"
                                    $violationCount++
                                }
                                break
                            }
                        }
                    }
                }
            }
            catch {
                if ($Verbose) {
                    Log-Warning "Could not read file: $($file.FullName)"
                }
            }
        }
    }
    
    if ($violationCount -eq 0) {
        Log-Success "No import violations detected"
    } else {
        Log-Error "Found $violationCount potential import violations"
    }
}

# Check file size compliance
function Test-FileSizes {
    Increment-Check
    Log-Info "Checking file size compliance (max 300 lines)..."
    
    $oversizedFiles = 0
    $srcPath = Join-Path $ProjectPath "src"
    
    $codeFiles = Get-ChildItem -Path $srcPath -Recurse -Include "*.ts", "*.tsx", "*.js", "*.jsx" -ErrorAction SilentlyContinue
    
    foreach ($file in $codeFiles) {
        try {
            $lineCount = (Get-Content $file.FullName -ErrorAction SilentlyContinue | Measure-Object -Line).Lines
            if ($lineCount -gt 300) {
                Log-Warning "File exceeds 300 lines ($lineCount): $($file.FullName)"
                $oversizedFiles++
            }
        }
        catch {
            if ($Verbose) {
                Log-Warning "Could not check file size: $($file.FullName)"
            }
        }
    }
    
    if ($oversizedFiles -eq 0) {
        Log-Success "All files comply with size limit"
    } else {
        Log-Warning "Found $oversizedFiles files exceeding 300 lines"
    }
}

# Check for proper index.ts exports
function Test-PublicApi {
    Increment-Check
    Log-Info "Checking for proper public API exports..."
    
    $layersWithSlices = @("pages", "widgets", "features", "entities")
    $missingExports = 0
    $srcPath = Join-Path $ProjectPath "src"
    
    foreach ($layer in $layersWithSlices) {
        $layerPath = Join-Path $srcPath $layer
        if (Test-Path $layerPath -PathType Container) {
            # Check each slice in the layer
            $slices = Get-ChildItem -Path $layerPath -Directory -ErrorAction SilentlyContinue
            foreach ($slice in $slices) {
                $indexTs = Join-Path $slice.FullName "index.ts"
                $indexJs = Join-Path $slice.FullName "index.js"
                
                if (-not (Test-Path $indexTs) -and -not (Test-Path $indexJs)) {
                    Log-Warning "Missing index file in slice: $layer/$($slice.Name)"
                    $missingExports++
                } else {
                    Log-Success "Index file found in $layer/$($slice.Name)"
                }
            }
        }
    }
    
    if ($missingExports -eq 0) {
        Log-Success "All slices have proper export files"
    }
}

# Check naming conventions
function Test-NamingConventions {
    Increment-Check
    Log-Info "Checking FSD naming conventions..."
    
    $namingIssues = 0
    $srcPath = Join-Path $ProjectPath "src"
    $layersWithSlices = @("pages", "widgets", "features", "entities")
    
    foreach ($layer in $layersWithSlices) {
        $layerPath = Join-Path $srcPath $layer
        if (Test-Path $layerPath -PathType Container) {
            $slices = Get-ChildItem -Path $layerPath -Directory -ErrorAction SilentlyContinue
            foreach ($slice in $slices) {
                # Check for kebab-case naming
                if ($slice.Name -notmatch '^[a-z0-9]+(-[a-z0-9]+)*$') {
                    Log-Warning "Non-kebab-case slice name: $($slice.Name) (should use kebab-case)"
                    $namingIssues++
                }
            }
        }
    }
    
    if ($namingIssues -eq 0) {
        Log-Success "All slice names follow kebab-case convention"
    }
}

# Generate FSD compliance report
function Write-Report {
    Write-Host ""
    Write-Host "📊 FSD Validation Report" -ForegroundColor Cyan
    Write-Host "========================" -ForegroundColor Cyan
    Write-Host "Total checks performed: $script:Checks" -ForegroundColor Blue
    Write-Host "Errors found: $script:Errors" -ForegroundColor Red
    Write-Host "Warnings issued: $script:Warnings" -ForegroundColor Yellow
    
    if ($script:Errors -eq 0) {
        Write-Host ""
        Write-Host "🎉 FSD compliance validation passed!" -ForegroundColor Green
        if ($script:Warnings -gt 0) {
            Write-Host "Note: Please review warnings for potential improvements." -ForegroundColor Yellow
        }
        return $true
    } else {
        Write-Host ""
        Write-Host "❌ FSD compliance validation failed." -ForegroundColor Red
        Write-Host "Please fix the errors above and run validation again." -ForegroundColor Red
        return $false
    }
}

# Main validation flow
function Start-Validation {
    Write-Host "🔍 Starting Feature-Sliced Design validation..." -ForegroundColor Cyan
    Write-Host "Project directory: $((Resolve-Path $ProjectPath).Path)" -ForegroundColor Cyan
    Write-Host ""
    
    # Run all validation checks
    $srcExists = Test-SrcStructure
    if (-not $srcExists) {
        Write-Report
        return
    }
    
    Test-Layers
    Test-Segments
    Test-ImportViolations
    Test-FileSizes
    Test-PublicApi
    Test-NamingConventions
    
    # Generate final report
    $success = Write-Report
    
    if (-not $success) {
        exit 1
    }
}

# Run main function
Start-Validation