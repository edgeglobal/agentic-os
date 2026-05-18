"""Tests for check_sync.is_cloud_stub() on macOS Google Drive / iCloud / OneDrive paths."""
import os
import subprocess
import pytest
from check_sync import is_cloud_stub, get_stub_files

# Real Google Drive stub indicator (macOS): xattr "com.google.drivefs.item-id" present
# Real iCloud stub indicator (macOS): xattr "com.apple.brokendownloadednotyet" or sparse-file
# Real OneDrive stub indicator (macOS): xattr "com.microsoft.OneDrive.RecallOnOpen" present

def test_local_file_is_not_stub(tmp_path):
    """A regular local file is NOT a cloud stub."""
    f = tmp_path / "local.md"
    f.write_text("hello")
    assert is_cloud_stub(str(f)) is False

def test_google_drive_stub_detected(tmp_path):
    """File with com.google.drivefs.item-id xattr IS a cloud stub."""
    f = tmp_path / "gdrive-stub.md"
    f.write_text("placeholder")
    subprocess.run(["xattr", "-w", "com.google.drivefs.item-id", "stub-12345", str(f)], check=True)
    assert is_cloud_stub(str(f)) is True

def test_nonexistent_file_raises(tmp_path):
    """Nonexistent path raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        is_cloud_stub(str(tmp_path / "doesnotexist.md"))

def test_get_stub_files_returns_only_stubs(tmp_path):
    """get_stub_files returns only files that are cloud stubs."""
    local = tmp_path / "local.md"
    local.write_text("hi")
    stub = tmp_path / "stub.md"
    stub.write_text("hi")
    subprocess.run(["xattr", "-w", "com.google.drivefs.item-id", "x", str(stub)], check=True)

    results = get_stub_files([str(local), str(stub)])
    assert results == [str(stub)]