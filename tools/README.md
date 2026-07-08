# Local Tool Shims

This directory may contain local build shims that should not be committed.

On this machine, the TeX Live universal `biber` executable fails because it invokes `/usr/bin/lipo -extract_family`, while the available `/usr/bin/lipo` does not support that option. The workaround is to create a thin arm64 Biber binary:

```bash
make bootstrap-biber-macos
```

The main `make pdf` target prefers `tools/biber` when it exists, then falls back to the system `PATH`.

