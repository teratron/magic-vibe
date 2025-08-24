#!/bin/bash

# Version Management Script for template-ai-rules project
# This script manages versioning for both project and documentation

VERSION_FILE=".vscode/rules/.magic-vibe/version.json"
#DOCS_EN_README="docs/en/README.md"
#DOCS_RU_README="docs/ru/README.md"
MAIN_README="README.md"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}[VERSION]${NC} $1"
}

# Function to get current timestamp in ISO format
get_timestamp() {
    date -u +"%Y-%m-%dT%H:%M:%SZ"
}

# Function to get current date in YYYY-MM-DD format
get_date() {
    date -u +"%Y-%m-%d"
}

# Function to read version from JSON file
get_version() {
    local type=$1
    local field=$2
    if [ -f "$VERSION_FILE" ]; then
        python3 -c "
import json
try:
    with open('$VERSION_FILE', 'r') as f:
        data = json.load(f)
    print(data.get('$type', {}).get('$field', 'unknown'))
except:
    print('unknown')
"
    else
        echo "unknown"
    fi
}

# Function to update version in JSON file
update_version() {
    local type=$1
    local field=$2
    local value=$3
    
    if [ ! -f "$VERSION_FILE" ]; then
        print_error "Version file not found: $VERSION_FILE"
        return 1
    fi
    
    python3 -c "
import json
try:
    with open('$VERSION_FILE', 'r') as f:
        data = json.load(f)
    
    if '$type' not in data:
        data['$type'] = {}
    
    data['$type']['$field'] = '$value'
    
    with open('$VERSION_FILE', 'w') as f:
        json.dump(data, f, indent=2)
    print('Success')
except Exception as e:
    print(f'Error: {e}')
"
}

# Function to increment version number
increment_version() {
    local version=$1
    local type=${2:-patch}  # major, minor, patch
    
    IFS='.' read -ra VERSION_PARTS <<< "$version"
    local major=${VERSION_PARTS[0]:-0}
    local minor=${VERSION_PARTS[1]:-0}
    local patch=${VERSION_PARTS[2]:-0}
    
    case $type in
        major)
            major=$((major + 1))
            minor=0
            patch=0
            ;;
        minor)
            minor=$((minor + 1))
            patch=0
            ;;
        patch)
            patch=$((patch + 1))
            ;;
    esac
    
    echo "${major}.${minor}.${patch}"
}

# Function to update documentation version
update_docs_version() {
    local new_doc_version=$1

    print_status "Updating documentation version to $new_doc_version"

    # Update version in JSON
    update_version "documentation" "version" "$new_doc_version"
    update_version "documentation" "last_updated" "$(get_timestamp)"

    # Increment generation count
    local new_count=$(($(get_version "documentation" "generation_count") + 1))
    update_version "documentation" "generation_count" "$new_count"

    print_status "Documentation version updated successfully"
}

# Function to update project version
update_project_version() {
    local new_version=$1
    
    print_status "Updating project version to $new_version"
    
    # Update version in JSON
    update_version "project" "version" "$new_version"
    update_version "project" "release_date" "$(get_date)"
    
    # Update build number
    local new_build=$(($(get_version "project" "build") + 1))
    update_version "project" "build" "$new_build"

    print_status "Project version updated successfully"
}

# Function to show current versions
show_versions() {
    print_header "Current Versions"
    echo "======================================"
    echo "Project Version:      $(get_version 'project' 'version')"
    echo "Project Build:        $(get_version 'project' 'build')"
    echo "Project Release Date: $(get_version 'project' 'release_date')"
    echo ""
    echo "Documentation Version: $(get_version 'documentation' 'version')"
    echo "Documentation Format:  v$(get_version 'documentation' 'format_version')"
    echo "Last Updated:         $(get_version 'documentation' 'last_updated')"
    echo "Generation Count:     $(get_version 'documentation' 'generation_count')"
    echo ""
    echo "Magic Vibe System:    v$(get_version 'task_magic' 'system_version')"
    echo "Hooks Version:        v$(get_version 'task_magic' 'documentation_hooks_version')"
    echo "======================================"
}

# Function to update version badges in README files
update_version_badges() {
    local project_version=$1
    #local doc_version=$2
    
    if [ -f "$MAIN_README" ]; then
        # Update main README version badge
        sed -i "s/Version-[0-9.]*/Version-$project_version/g" "$MAIN_README"
        print_status "Updated version badge in main README.md"
    fi
}

# Main script logic
case "${1:-show}" in
    "show"|"status")
        show_versions
        ;;
    "bump-project")
        version_type=${2:-patch}
        current_version=$(get_version "project" "version")
        new_version=$(increment_version "$current_version" "$version_type")
        update_project_version "$new_version"
        update_version_badges "$new_version" "$(get_version 'documentation' 'version')"
        show_versions
        ;;
    "bump-docs")
        version_type=${2:-patch}
        current_version=$(get_version "documentation" "version")
        new_version=$(increment_version "$current_version" "$version_type")
        update_docs_version "$new_version"
        show_versions
        ;;
    "set-project")
        if [ -z "$2" ]; then
            print_error "Please provide version number (e.g., 2.1.0)"
            exit 1
        fi
        update_project_version "$2"
        update_version_badges "$2" "$(get_version 'documentation' 'version')"
        show_versions
        ;;
    "set-docs")
        if [ -z "$2" ]; then
            print_error "Please provide version number (e.g., 1.2.0)"
            exit 1
        fi
        update_docs_version "$2"
        show_versions
        ;;
    "auto-docs")
        # Automatic documentation version update (called by hooks)
        current_version=$(get_version "documentation" "version")
        new_version=$(increment_version "$current_version" "patch")
        update_docs_version "$new_version"
        ;;
    "help"|"-h"|"--help")
        echo "Usage: $0 [command] [arguments]"
        echo ""
        echo "Commands:"
        echo "  show                    Show current versions (default)"
        echo "  bump-project [type]     Bump project version (major|minor|patch)"
        echo "  bump-docs [type]        Bump documentation version (major|minor|patch)"
        echo "  set-project <version>   Set specific project version"
        echo "  set-docs <version>      Set specific documentation version"
        echo "  auto-docs               Auto-increment docs version (for hooks)"
        echo "  help                    Show this help message"
        echo ""
        echo "Examples:"
        echo "  $0 show"
        echo "  $0 bump-project minor"
        echo "  $0 set-project 2.0.0"
        echo "  $0 bump-docs patch"
        ;;
    *)
        print_error "Unknown command: $1"
        echo "Use '$0 help' for usage information"
        exit 1
        ;;
esac