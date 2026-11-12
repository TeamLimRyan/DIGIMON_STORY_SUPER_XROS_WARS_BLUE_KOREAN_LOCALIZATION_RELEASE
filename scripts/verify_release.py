import hashlib, json, subprocess
from pathlib import Path
r = Path(__file__).resolve().parents[1]
m = json.loads((r / 'patch_manifest.json').read_text(encoding='utf-8'))
allowed = {'README.md','INSTALL.md','COMPATIBILITY.md','SUPPORT.md','NOTICE.md','SHA256SUMS.txt','patch_manifest.json','release-notes.md','.gitattributes','.gitignore','.github/workflows/integrity.yml','.github/ISSUE_TEMPLATE/bug_report.yml','scripts/verify_release.py',m['patch']['file']}
tracked = subprocess.check_output(['git','ls-files','-z'],cwd=r).decode().split('\0')
assert set(filter(None,tracked)) == allowed, 'Unexpected or missing tracked files'
for line in (r/'SHA256SUMS.txt').read_text().splitlines():
    h, name = line.split('  ',1)
    assert name in allowed and hashlib.sha256((r/name).read_bytes()).hexdigest() == h, name
p=(r/m['patch']['file']).read_bytes()
assert p[:4] == bytes([0xd6,0xc3,0xc4,0]) and not (p[4]&4), 'Invalid VCDIFF or application header present'
assert len(p)==m['patch']['size'] and hashlib.sha256(p).hexdigest()==m['patch']['sha256']
assert m['roundtrip']['sha256']==m['target']['sha256'] and m['roundtrip']['size']==m['target']['size']
for part in ('source','target','patch','roundtrip'):
    assert len(m[part]['sha256'])==64 and m[part]['size']>0
print('PASS: exact public file allowlist, checksums, headerless VCDIFF, source/target metadata')
