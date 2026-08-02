# Services_Data - hydration pointer (NOT in git)

HarmonyGames stores universe truth here, not in the per-task JSON (that file is a
~721-byte pointer). Gitignored: too large to vendor.

- source: `/Users/kaustubhbhargava/Downloads/ABDM/Compressed/MCP_Eval_V3_HarmonyGames/HarmonyGames_Base_Universe/Services_Data`
- size: 5.6G
- service dirs: 13
- Base_Universe_Complete_Data.json bytes: 233946251
- sha256: 30751b6066af0ae5c84bf782dbceeb53c143902d3cee55542d8c611640858ebf

## Hydrate
```
rsync -a --exclude=.git '/Users/kaustubhbhargava/Downloads/ABDM/Compressed/MCP_Eval_V3_HarmonyGames/HarmonyGames_Base_Universe/Services_Data/' HarmonyGames_Base_Universe/Services_Data/
```

Contains four nested git packs under `github/root/harmonygames-Games/`; the rsync
excludes `.git` so they never become broken gitlinks.
