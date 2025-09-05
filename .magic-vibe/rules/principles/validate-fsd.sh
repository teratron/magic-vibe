#!/bin/bash

# Feature-Sliced Design (FSD) Architecture Validation Script
# This script validates FSD compliance for AI-assisted development

set -e

echo "🍰 Feature-Sliced Design Validation Starting..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Counters
ERRORS=0
WARNINGS=0
CHECKS=0

# Helper functions
log_error() {
    echo -e "${RED}❌ ERROR: $1${NC}"
    ((ERRORS++))
}

log_warning() {
    echo -e "${YELLOW}⚠️  WARNING: $1${NC}"
    ((WARNINGS++))
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

increment_check() {
    ((CHECKS++))
}

# Check if src directory exists
check_src_structure() {
    increment_check
    if [ ! -d "src" ]; then
        log_error "src/ directory not found. FSD requires src/ as root directory."
        return 1
    fi
    log_success "src/ directory found"
}

# Validate FSD layer structure
validate_layers() {
    increment_check
    log_info "Validating FSD layer structure..."
    
    local required_layers=("shared")
    local optional_layers=("app" "pages" "widgets" "features" "entities")
    local deprecated_layers=("processes")
    
    # Check required layers
    for layer in "${required_layers[@]}"; do
        if [ ! -d "src/$layer" ]; then
            log_error "Required layer missing: src/$layer/"
        else
            log_success "Required layer found: src/$layer/"
        fi
    done
    
    # Check optional layers
    for layer in "${optional_layers[@]}"; do
        if [ -d "src/$layer" ]; then
            log_success "Optional layer found: src/$layer/"
        fi
    done
    
    # Check for deprecated layers
    for layer in "${deprecated_layers[@]}"; do
        if [ -d "src/$layer" ]; then
            log_warning "Deprecated layer found: src/$layer/ (consider removing)"
        fi
    done
}

# Validate segment structure within slices
validate_segments() {
    increment_check
    log_info "Validating segment structure..."
    
    local standard_segments=("ui" "model" "api" "lib" "config")
    local invalid_segments=("components" "views" "store" "state" "services" "requests")
    
    # Check for invalid segment names
    for segment in "${invalid_segments[@]}"; do
        if find src -type d -name "$segment" 2>/dev/null | grep -q .; then
            log_warning "Non-standard segment name found: '$segment'. Consider renaming to FSD standard."
        fi
    done
    
    # Validate shared layer segments
    if [ -d "src/shared" ]; then
        for segment in "${standard_segments[@]}"; do
            if [ -d "src/shared/$segment" ]; then
                log_success "Standard segment in shared: $segment/"
            fi
        done
    fi
}

# Check import violations using a simple pattern check
check_import_violations() {
    increment_check
    log_info "Checking for potential import violations..."
    
    local violation_count=0
    
    # Define layer hierarchy (index = layer level, higher numbers can't import from lower numbers)
    declare -A layer_levels=(
        ["app"]=6
        ["pages"]=5
        ["widgets"]=4
        ["features"]=3
        ["entities"]=2
        ["shared"]=1
    )
    
    # Check TypeScript/JavaScript files for import violations
    while IFS= read -r -d '' file; do
        if [[ -f "$file" ]]; then
            # Determine current file's layer
            local current_layer=""
            for layer in "${!layer_levels[@]}"; do
                if [[ "$file" == *"src/$layer/"* ]]; then
                    current_layer="$layer"
                    break
                fi
            done
            
            if [[ -n "$current_layer" ]]; then
                local current_level=${layer_levels[$current_layer]}
                
                # Check imports in this file
                while IFS= read -r line; do
                    if [[ "$line" =~ ^[[:space:]]*import.*from[[:space:]]+[\"\'](.*)[\"\']; ]]; then
                        local import_path="${BASH_REMATCH[1]}"
                        
                        # Check if it's a relative or absolute src import
                        if [[ "$import_path" =~ ^(app|pages|widgets|features|entities|shared)/ ]]; then
                            local imported_layer="${import_path%%/*}"
                            local imported_level=${layer_levels[$imported_layer]}
                            
                            if [[ $current_level -le $imported_level ]]; then
                                log_error "Import violation in $file: $current_layer cannot import from $imported_layer"
                                ((violation_count++))
                            fi
                        fi
                    fi
                done < "$file"
            fi
        fi
    done < <(find src -name "*.ts" -o -name "*.tsx" -o -name "*.js" -o -name "*.jsx" -print0 2>/dev/null)
    
    if [[ $violation_count -eq 0 ]]; then
        log_success "No import violations detected"
    else
        log_error "Found $violation_count potential import violations"
    fi
}

# Check file size compliance
check_file_sizes() {
    increment_check
    log_info "Checking file size compliance (max 300 lines)..."
    
    local oversized_files=0
    
    while IFS= read -r -d '' file; do
        if [[ -f "$file" ]]; then
            local line_count=$(wc -l < "$file")
            if [[ $line_count -gt 300 ]]; then
                log_warning "File exceeds 300 lines ($line_count): $file"
                ((oversized_files++))
            fi
        fi
    done < <(find src -name "*.ts" -o -name "*.tsx" -o -name "*.js" -o -name "*.jsx" -print0 2>/dev/null)
    
    if [[ $oversized_files -eq 0 ]]; then
        log_success "All files comply with size limit"
    else
        log_warning "Found $oversized_files files exceeding 300 lines"
    fi
}

# Check for proper index.ts exports
check_public_api() {
    increment_check
    log_info "Checking for proper public API exports..."
    
    local layers_with_slices=("pages" "widgets" "features" "entities")
    local missing_exports=0
    
    for layer in "${layers_with_slices[@]}"; do
        if [ -d "src/$layer" ]; then
            # Check each slice in the layer
            for slice_dir in src/$layer/*/; do
                if [ -d "$slice_dir" ]; then
                    local slice_name=$(basename "$slice_dir")
                    if [ ! -f "$slice_dir/index.ts" ] && [ ! -f "$slice_dir/index.js" ]; then
                        log_warning "Missing index file in slice: $layer/$slice_name"
                        ((missing_exports++))
                    else
                        log_success "Index file found in $layer/$slice_name"
                    fi
                fi
            done
        fi
    done
    
    if [[ $missing_exports -eq 0 ]]; then
        log_success "All slices have proper export files"
    fi
}

# Check naming conventions
check_naming_conventions() {
    increment_check
    log_info "Checking FSD naming conventions..."
    
    local naming_issues=0
    
    # Check for kebab-case in slice names
    while IFS= read -r -d '' dir; do
        local dirname=$(basename "$dir")
        if [[ ! "$dirname" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] && [[ "$dirname" != "src" ]]; then
            local parent_dir=$(dirname "$dir")
            local parent_name=$(basename "$parent_dir")
            
            # Only check slice directories (inside layer directories)
            if [[ "$parent_name" =~ ^(pages|widgets|features|entities)$ ]]; then
                log_warning "Non-kebab-case slice name: $dirname (should use kebab-case)"
                ((naming_issues++))
            fi
        fi
    done < <(find src -maxdepth 3 -type d -print0 2>/dev/null)
    
    if [[ $naming_issues -eq 0 ]]; then
        log_success "All slice names follow kebab-case convention"
    fi
}

# Generate FSD compliance report
generate_report() {
    echo ""
    echo "📊 FSD Validation Report"
    echo "========================"
    echo -e "Total checks performed: ${BLUE}$CHECKS${NC}"
    echo -e "Errors found: ${RED}$ERRORS${NC}"
    echo -e "Warnings issued: ${YELLOW}$WARNINGS${NC}"
    
    if [[ $ERRORS -eq 0 ]]; then
        echo -e "\n${GREEN}🎉 FSD compliance validation passed!${NC}"
        if [[ $WARNINGS -gt 0 ]]; then
            echo -e "${YELLOW}Note: Please review warnings for potential improvements.${NC}"
        fi
        return 0
    else
        echo -e "\n${RED}❌ FSD compliance validation failed.${NC}"
        echo -e "${RED}Please fix the errors above and run validation again.${NC}"
        return 1
    fi
}

# Main validation flow
main() {
    echo "🔍 Starting Feature-Sliced Design validation..."
    echo "Project directory: $(pwd)"
    echo ""
    
    # Run all validation checks
    check_src_structure || true
    validate_layers
    validate_segments
    check_import_violations
    check_file_sizes
    check_public_api
    check_naming_conventions
    
    # Generate final report
    generate_report
}

# Run main function
main "$@"