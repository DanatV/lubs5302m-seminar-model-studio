"""Developer only: rebuild the portable HTML after editing the source files."""
from pathlib import Path
root = Path(__file__).resolve().parent
page = (root / 'page.html').read_text()
for marker, name in [('/*CSS*/', 'styles.css'), ('/*MODEL*/', 'model.js'), ('/*APP*/', 'app.js')]:
    page = page.replace(marker, (root / name).read_text())
(root / 'index.html').write_text(page)
print('Built standalone index.html')
