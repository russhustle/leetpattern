#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🔨 Building all C++ files...${NC}"

# Create build directory
mkdir -p build
cd build

# Run CMake
cmake .. || { echo -e "${RED}❌ CMake configuration failed${NC}"; exit 1; }

# Build all executables
make build_all -j$(nproc) || { echo -e "${RED}❌ Build failed${NC}"; exit 1; }

echo -e "${GREEN}✅ Build completed successfully!${NC}"
echo -e "${BLUE}🧪 Running all tests...${NC}"

# Run all executables and capture results
passed=0
failed=0
failed_programs=()

for exe in ./*; do
    if [[ -x "$exe" && -f "$exe" ]]; then
        filename=$(basename "$exe")
        echo -e "\n${BLUE}Running $filename...${NC}"
        
        if ./"$filename"; then
            echo -e "${GREEN}✅ $filename passed${NC}"
            ((passed++))
        else
            echo -e "${RED}❌ $filename failed${NC}"
            ((failed++))
            failed_programs+=("$filename")
        fi
    fi
done

echo -e "\n${BLUE}📊 Test Summary:${NC}"
echo -e "${GREEN}✅ Passed: $passed${NC}"
echo -e "${RED}❌ Failed: $failed${NC}"

if [ $failed -gt 0 ]; then
    echo -e "\n${RED}Failed programs:${NC}"
    for prog in "${failed_programs[@]}"; do
        echo -e "${RED}  - $prog${NC}"
    done
    exit 1
else
    echo -e "\n${GREEN}🎉 All tests passed!${NC}"
fi