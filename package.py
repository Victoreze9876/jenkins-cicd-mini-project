from pathlib import Path
import zipfile

root = Path(__file__).parent
output_dir = root / "deployment"
output_dir.mkdir(exist_ok=True)

artifact = output_dir / "jenkins-cicd-app.zip"

with zipfile.ZipFile(artifact, "w", zipfile.ZIP_DEFLATED) as archive:
    archive.write(root / "src" / "app.py", "app.py")
    archive.write(root / "README.md", "README.md")

print(f"Created artifact: {artifact}")
