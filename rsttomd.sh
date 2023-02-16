find . -type f -name "*.rst" -exec sh -c 'pandoc -f rst -t markdown "$1" -o "${1%.rst}.md" && rm "$1"' _ {} \;
