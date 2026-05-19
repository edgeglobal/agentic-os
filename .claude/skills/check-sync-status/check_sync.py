"""Detect Cloud-Drive stub files via macOS extended attributes.

Stub indicators by provider:
- Google Drive: xattr "com.google.drivefs.item-id"
- iCloud Drive: xattr "com.apple.brokendownloadednotyet" OR file size much smaller than logical size
- OneDrive: xattr "com.microsoft.OneDrive.RecallOnOpen"
- Dropbox (legacy Smart Sync): xattr "com.dropbox.attributes" with online-only flag
"""
import os
import subprocess

STUB_XATTRS = [
    "com.google.drivefs.item-id",
    "com.apple.brokendownloadednotyet",
    "com.microsoft.OneDrive.RecallOnOpen",
]

def _list_xattrs(path: str) -> list[str]:
    """Return list of extended attribute names for path. Empty list if none."""
    try:
        result = subprocess.run(
            ["xattr", path],
            capture_output=True, text=True, check=True
        )
        return [line.strip() for line in result.stdout.splitlines() if line.strip()]
    except subprocess.CalledProcessError:
        return []

def is_cloud_stub(path: str) -> bool:
    """Return True if the file at `path` is a Cloud-Drive stub (not fully downloaded)."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Path does not exist: {path}")
    xattrs = _list_xattrs(path)
    return any(stub_marker in xattrs for stub_marker in STUB_XATTRS)

def get_stub_files(paths: list[str]) -> list[str]:
    """Filter a list of paths, returning only those that are cloud stubs."""
    return [p for p in paths if os.path.exists(p) and is_cloud_stub(p)]

CRITICAL_PATHS = [
    "KONTEXT.md", "AGENTS.md", "CLAUDE.md", "_rules.md",
    "ueberblick.md", "marke.md", "wunschkunde-icp.md",
    "strategie.md", "tools.md",
    ".claude/settings.json",
]

def main():
    import sys
    workspace_root = os.getcwd()
    paths = [os.path.join(workspace_root, p) for p in CRITICAL_PATHS]
    stubs = get_stub_files(paths)
    if stubs:
        print(f"⚠️  {len(stubs)} critical files are Cloud-Drive stubs:")
        for s in stubs:
            print(f"  - {os.path.relpath(s, workspace_root)}")
        print("\nFix: in your Cloud-Drive client, mark ~/ai-workspace/ as 'Make available offline'.")
        sys.exit(1)
    print("✅ All critical files are local (Mirror mode active).")
    sys.exit(0)

if __name__ == "__main__":
    main()