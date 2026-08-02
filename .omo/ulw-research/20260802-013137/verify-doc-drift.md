RUNBOOK CORPUS: 16 files, 200 KB total

PAIRWISE SIMILARITY (difflib quick_ratio) — pairs above 0.60 are near-duplicates:
   0.948  FINAL.md           <-> REVIEW.md
   0.933  S1.md              <-> S3.md
   0.929  S1.md              <-> S2.md
   0.923  FEEDBACK.md        <-> S3.md
   0.923  S1.5.md            <-> S3.md
   0.921  REVIEW.md          <-> S4.md
   0.918  FINAL.md           <-> S4.md
   0.918  S1.5.md            <-> S1.md
   0.916  FEEDBACK.md        <-> S1.5.md
   0.916  FEEDBACK.md        <-> HARDNESS.md
   0.915  FEEDBACK.md        <-> S1.md
   0.905  HARDNESS.md        <-> S3.md
   (67 of 120 pairs >= 0.60)

FIVE-UNIVERSE COVERAGE per runbook (the '5th arm' the user added by hand):
   COMPARE.md         MISSING: brookfield, keystone, moveops, starpm
   FEEDBACK.md        MISSING: keystone, moveops
   MATERIALIZE.md     MISSING: brookfield, keystone, moveops, starpm
   NEW.md             MISSING: brookfield, keystone, moveops
   REDO.md            MISSING: brookfield, keystone, moveops, starpm
   S1.5.md            MISSING: brookfield, keystone, moveops, starpm
   => 6/16 runbooks do not name all five universes.

SHARED BOILERPLATE BLOCKS (identical >=3-line runs appearing in >=4 runbooks):
   4 distinct 3-line blocks repeat in >=4 runbooks
     x8   ```
     x8   
     x6   Refuses if upstream artifacts are missing. If it STOPs, run the upstream phase first.
     x4   | `Tasks/<TASK_DIR>/_aux/Universe_Split/*` | S0 |

TEMPLATE TREES: 5
   Tasks_Template                    17 files
   Tasks_Template_harmonygames       16 files
   Tasks_Template_keystone           16 files
   Tasks_Template_moveops            16 files
   Tasks_Template_starpm             23 files
