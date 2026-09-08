#!/usr/bin/env python3

import os
import re
from datetime import datetime
from pathlib import Path

version = os.environ["VERSION"].removeprefix("v")
release_date = (
    datetime.fromisoformat(os.environ["RELEASE_DATE"].replace("Z", "+00:00"))
    .date()
    .isoformat()
)
readme_path = Path("README.md")
readme = readme_path.read_text()

downloads = f"""| **macOS** | **Linux 64 bit** | **Windows 64 bit** |
|-----------|------------------|--------------------|
| [download](https://download.clis.cloud.ibm.com/ibm-cloud-cli/{version}/IBM_Cloud_CLI_{version}.pkg) | [download](https://download.clis.cloud.ibm.com/ibm-cloud-cli/{version}/IBM_Cloud_CLI_{version}_amd64.tar.gz) | [download](https://download.clis.cloud.ibm.com/ibm-cloud-cli/{version}/IBM_Cloud_CLI_{version}_amd64.exe) |"""

readme, count = re.subn(
    r"<!-- DOWNLOADS:START -->.*?<!-- DOWNLOADS:END -->",
    f"<!-- DOWNLOADS:START -->\n{downloads}\n<!-- DOWNLOADS:END -->",
    readme,
    flags=re.DOTALL,
)
if count != 1:
    raise SystemExit("README.md must contain exactly one downloads marker block")

readme, count = re.subn(
    r"Latest version \*\*[^*]+\*\* released \*\*[^*]+\*\*\.",
    f"Latest version **{version}** released **{release_date}**.",
    readme,
)
if count != 1:
    raise SystemExit("README.md must contain exactly one latest-version line")

readme_path.write_text(readme)
