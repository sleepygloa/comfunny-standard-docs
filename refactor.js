const fs = require('fs');
const path = require('path');

const docsDir = 'c:\\work\\comfunny-total-system\\.docs';
const standardsDir = path.join(docsDir, 'standards');
const techGuidesDir = path.join(docsDir, 'tech-guides');

function getPrefix(content) {
    const match = content.match(/^#\s+\[([A-Z]-\d{2})\]\s+/m);
    if (match) return match[1];
    return null;
}

function processFile(filepath) {
    const content = fs.readFileSync(filepath, 'utf8');
    const prefix = getPrefix(content);

    if (!prefix) {
        console.log("No prefix found for", filepath);
        return { newFilepath: filepath, newContent: content, basename: path.basename(filepath) };
    }

    const filename = path.basename(filepath);
    const newFilename = filename.startsWith(prefix + "_") ? filename : `${prefix}_${filename}`;
    const newFilepath = path.join(path.dirname(filepath), newFilename);

    const pattern = /^(\#{2,4})\s+((\d+\.)+\d*|\d+\.?)\s+(.*)$/gm;
    let newContent = content.replace(pattern, (match, headerLvl, numbering, _inner, title) => {
        if (numbering.includes(prefix)) return match;

        let cleanNum = numbering.trim();
        let newNum = `${prefix}-${cleanNum}`;
        return `${headerLvl} ${newNum} ${title}`;
    });

    return { newFilepath, newContent, basename: newFilename };
}

function main() {
    const renameMap = {};
    [standardsDir, techGuidesDir].forEach(d => {
        fs.readdirSync(d).forEach(fn => {
            if (fn.endsWith('.md')) {
                const oldPath = path.join(d, fn);
                const result = processFile(oldPath);

                renameMap[fn] = result.basename;

                if (result.newContent) {
                    if (oldPath !== result.newFilepath) {
                        fs.unlinkSync(oldPath);
                    }
                    fs.writeFileSync(result.newFilepath, result.newContent, 'utf8');
                    console.log(`Updated: ${fn} -> ${result.basename}`);
                }
            }
        });
    });

    const masterPath = path.join(docsDir, 'MASTER_RULE.md');
    const readmePath = path.join(docsDir, 'README.md');

    if (fs.existsSync(masterPath)) {
        let masterContent = fs.readFileSync(masterPath, 'utf8');
        const agentComment = "<!-- AGENT RULE: AI Agent 설정 시 항상 이 README.md 파일의 내용을 복사/참조하여 프로젝트의 핵심 룰(Rule)로 지정하십시오. -->\n\n> **AGENT RULE INSTRUCTION:** AI Agent 설정 시 항상 이 README.md 파일의 내용을 복사/참조하여 프로젝트의 핵심 룰(Rule)로 지정하십시오.\n\n";

        Object.keys(renameMap).forEach(oldFn => {
            masterContent = masterContent.split(oldFn).join(renameMap[oldFn]);
        });

        const finalReadme = agentComment + masterContent;
        fs.writeFileSync(readmePath, finalReadme, 'utf8');
        console.log("Merged MASTER_RULE into README");
        fs.unlinkSync(masterPath);
    }
}

main();
