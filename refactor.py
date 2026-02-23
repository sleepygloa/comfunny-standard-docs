import os
import re

docs_dir = r"c:\work\comfunny-total-system\.docs"
standards_dir = os.path.join(docs_dir, "standards")
tech_guides_dir = os.path.join(docs_dir, "tech-guides")

def get_prefix(content):
    # Match the prefix like [A-10]
    match = re.search(r'^#\s+\[([A-Z]-\d{2})\]\s+', content, flags=re.MULTILINE)
    if match:
        return match.group(1)
    return None

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    prefix = get_prefix(content)
    if not prefix:
        print(f"No prefix found for {filepath}")
        return filepath, content
        
    filename = os.path.basename(filepath)
    if filename.startswith(f"{prefix}_"):
        new_filename = filename
    else:
        new_filename = f"{prefix}_{filename}"
        
    new_filepath = os.path.join(os.path.dirname(filepath), new_filename)
    
    def header_repl(match):
        header_level = match.group(1) 
        numbering = match.group(2)
        title = match.group(4) # group 4 is the title
        
        # If already prefixed
        if prefix in numbering:
            return match.group(0)
            
        clean_num = numbering.strip()
        new_num = f"{prefix}-{clean_num}"
        return f"{header_level} {new_num} {title}"
        
    pattern = r'^(\#{2,4})\s+((\d+\.)+\d*|\d+\.?)\s+(.*)$'
    new_content = re.sub(pattern, header_repl, content, flags=re.MULTILINE)
    
    return new_filepath, new_content

def main():
    rename_map = {}
    for d in [standards_dir, tech_guides_dir]:
        for fn in os.listdir(d):
            if fn.endswith('.md'):
                old_path = os.path.join(d, fn)
                new_path, new_content = process_file(old_path)
                
                # Store the basename mapping
                rename_map[fn] = os.path.basename(new_path)
                
                # If changes and renaming, do the filesystem updates
                if new_content != "":
                    if old_path != new_path:
                        os.remove(old_path)
                    with open(new_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Renamed and updated: {fn} -> {os.path.basename(new_path)}")

    master_path = os.path.join(docs_dir, 'MASTER_RULE.md')
    readme_path = os.path.join(docs_dir, 'README.md')
    
    if os.path.exists(master_path):
        with open(master_path, 'r', encoding='utf-8') as f:
            master_content = f.read()
            
        agent_comment = "<!-- AGENT RULE: AI Agent 설정 시 항상 이 README.md 파일의 내용을 복사/참조하여 프로젝트의 핵심 룰(Rule)로 지정하십시오. -->\n\n> **AGENT RULE INSTRUCTION:** AI Agent 설정 시 항상 이 README.md 파일의 내용을 복사/참조하여 프로젝트의 핵심 룰(Rule)로 지정하십시오.\n\n"
        
        # Replace links in MASTER content
        for old_fn, new_fn in rename_map.items():
            master_content = master_content.replace(old_fn, new_fn)
            
        final_readme = agent_comment + master_content
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(final_readme)
        print("Merged MASTER_RULE.md into README.md")
        
        os.remove(master_path)
    
if __name__ == "__main__":
    main()
