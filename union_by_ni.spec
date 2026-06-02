# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec — CNC AI Brain v11.0.8
Build: pyinstaller union_by_ni.spec
Output: dist/CNC-AI-Brain/ (portable folder)
"""
import sys
from pathlib import Path

block_cipher = None
src_root = Path(SPECPATH)

a = Analysis(
    [str(src_root / 'app' / 'main.py')],
    pathex=[str(src_root)],
    binaries=[],
    datas=[
        # Static files (frontend)
        (str(src_root / 'app' / 'static'), 'app/static'),
        # Config files
        (str(src_root / 'config'), 'config'),
        # Templates
        (str(src_root / 'templates'), 'templates'),
        # Source modules (needed at runtime)
        (str(src_root / 'src'), 'src'),
    ],
    hiddenimports=[
        'uvicorn',
        'uvicorn.logging',
        'uvicorn.loops',
        'uvicorn.loops.auto',
        'uvicorn.protocols',
        'uvicorn.protocols.http',
        'uvicorn.protocols.http.auto',
        'uvicorn.protocols.websockets',
        'uvicorn.protocols.websockets.auto',
        'uvicorn.lifespan',
        'uvicorn.lifespan.on',
        'fastapi',
        'trimesh',
        'numpy',
        'numpy-stl',
        'yaml',
        'jsonschema',
        'httpx',
        'pydantic',
        'loguru',
        'cascadio',
        'src.ai_engine.ollama_engine',
        'src.ai_engine.openai_engine',
        'src.core.model_registry',
        'src.runtime.quote_adapter',
        'src.neuro_core.conflict_check',
        'src.runtime.step_generator',
        'src.runtime.step_parser',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter', 'matplotlib', 'scipy', 'pandas',
        'PIL', 'cv2', 'torch', 'tensorflow',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='CNC-AI-Brain',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # Need console for uvicorn output
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='CNC-AI-Brain',
)
