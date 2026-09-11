# SmartVolt Protection Standard v1.0

**Status:** Active baseline
**Date:** 2026-09-11
**Applies to:** SmartVolt / SmartVoltISA project family

## 1. Preservation

- Existing source, documentation, commits, tags, and history are not to be erased or rewritten without explicit authorization.
- Improvements are added as new commits whenever practical.
- Cleanup must not destroy provenance.

## 2. Licensing

- Repository-level license: Apache License 2.0 unless a repository explicitly declares another license.
- Root `LICENSE` is the canonical repository license file.
- Existing file-specific or third-party licenses remain valid and must not be silently replaced.

## 3. Attribution and branding

- Copyright and attribution notices must be preserved.
- SmartVolt names, logos, trademarks, and branding are separate from the grant of rights under Apache-2.0.

## 4. Secrets

Never commit credentials or sensitive access material, including API keys, passwords, access tokens, private keys, or secret `.env` files.

Use example configuration files with placeholders instead.

## 5. Security

- Vulnerabilities should be reported privately whenever possible.
- Public issues must not contain exploitable credentials or sensitive personal data.
- Security changes must preserve enough history to establish what changed and why.

## 6. Architecture boundaries

For systems with Core / READ or internal / public contours:

- The trusted Core is the source of truth.
- Public or read-only layers must not silently acquire write authority over the Core.
- Security boundaries must be explicit in documentation and implementation.

## 7. Version anchors

Important stable states should be represented by immutable Git tags/releases where appropriate. Tags provide historical reference points without rewriting earlier commits.

## 8. Backups

GitHub must not be the only copy of important SmartVolt work. Maintain independent local/offline backups of critical repositories and their Git history.

## 9. Change rule

**Find → verify → change → verify result → record → continue.**

No destructive change is considered complete until the resulting state has been independently checked.
