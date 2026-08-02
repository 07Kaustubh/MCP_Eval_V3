ROUTER MARGIN AUDIT — detect_universe() scoring path
========================================================================================================
Confidence score kappa = (top1 - top2) / top1   (normalised margin; 1.0 = only one universe fires)
========================================================================================================
task dirs scanned            : 122
ZERO-signal (silent default) : 40
exact TIES (silent default)  : 0
normalised margin  min=1.000  p10=1.000  median=1.000  p90=1.000  max=1.000
   abstain if margin < 0.10  ->    0/82 tasks abstain  (coverage 100.0%)
   abstain if margin < 0.20  ->    0/82 tasks abstain  (coverage 100.0%)
   abstain if margin < 0.30  ->    0/82 tasks abstain  (coverage 100.0%)
   abstain if margin < 0.50  ->    0/82 tasks abstain  (coverage 100.0%)

LOW-MARGIN TASKS (the ones a silent argmax decides on thin evidence):
   (none below 0.35)

ZERO-SIGNAL / TIE TASKS (decided entirely by the back-compat default):
   QC_Tasks/V2.1_Buckets/QC_False_Fails_PT_Dispute_Accepted/Task1_6a3 ZERO-SIGNAL -> default brookfield
   QC_Tasks/V2.1_Buckets/QC_False_Fails_PT_Dispute_Accepted/Task3_6a2 ZERO-SIGNAL -> default brookfield
   QC_Tasks/V2.1_Buckets/QC_Non_Fails/Task1_6a3ac526db5033881f6b872d  ZERO-SIGNAL -> default brookfield
   QC_Tasks/V2.1_Buckets/QC_Passed/Task1_6a26c29d5f5b7cf1ea90c0cc     ZERO-SIGNAL -> default brookfield
   QC_Tasks/V2.1_Buckets/QC_Passed/Task2_6a27b70a80b7729ca5d6d88d     ZERO-SIGNAL -> default brookfield
   QC_Tasks/V2.1_Buckets/QC_Passed/Task3_6a2b528b5612fb11a6502d7a     ZERO-SIGNAL -> default brookfield
   QC_Tasks/V2.1_Buckets/QC_Passed/Task4_6a30fe7ec1d692ab3ccad616     ZERO-SIGNAL -> default brookfield
   QC_Tasks/V2.1_Tasks/QC_False_Fails_PT_Dispute_Accepted/Task1_6a312 ZERO-SIGNAL -> default brookfield
   QC_Tasks/V2.1_Tasks/QC_False_Fails_PT_Dispute_Accepted/Task3_6a2b0 ZERO-SIGNAL -> default brookfield
   QC_Tasks/V2.1_Tasks/QC_Non_Fails/Task1_6a3ac526db5033881f6b872d    ZERO-SIGNAL -> default brookfield
   QC_Tasks/V2.1_Tasks/QC_Passed/Task1_6a26c29d5f5b7cf1ea90c0cc       ZERO-SIGNAL -> default brookfield
   QC_Tasks/V2.1_Tasks/QC_Passed/Task2_6a27b70a80b7729ca5d6d88d       ZERO-SIGNAL -> default brookfield
   QC_Tasks/V2.1_Tasks/QC_Passed/Task3_6a2b528b5612fb11a6502d7a       ZERO-SIGNAL -> default brookfield
   QC_Tasks/V2.1_Tasks/QC_Passed/Task4_6a30fe7ec1d692ab3ccad616       ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3.1_Buckets/QC_False_Fails_PT_Dispute_Accepted/Task1_6a3 ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3.1_Buckets/QC_False_Fails_PT_Dispute_Accepted/Task3_6a2 ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3.1_Buckets/QC_Non_Fails/Task1_6a3ac526db5033881f6b872d  ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3.1_Buckets/QC_Passed/Task1_6a26c29d5f5b7cf1ea90c0cc     ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3.1_Buckets/QC_Passed/Task2_6a27b70a80b7729ca5d6d88d     ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3.1_Buckets/QC_Passed/Task3_6a2b528b5612fb11a6502d7a     ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3.1_Buckets/QC_Passed/Task4_6a30fe7ec1d692ab3ccad616     ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3.1_Tasks/Task1_6a26c29d5f5b7cf1ea90c0cc                 ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3.1_Tasks/Task2_6a27b70a80b7729ca5d6d88d                 ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3.1_Tasks/Task3_6a2b528b5612fb11a6502d7a                 ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3.1_Tasks/Task4_6a30fe7ec1d692ab3ccad616                 ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3_Buckets/QC_False_Fails_PT_Dispute_Accepted/Task1_6a312 ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3_Buckets/QC_False_Fails_PT_Dispute_Accepted/Task3_6a2b0 ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3_Buckets/QC_Non_Fails/Task1_6a3ac526db5033881f6b872d    ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3_Buckets/QC_Passed/Task1_6a26c29d5f5b7cf1ea90c0cc       ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3_Buckets/QC_Passed/Task2_6a27b70a80b7729ca5d6d88d       ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3_Buckets/QC_Passed/Task3_6a2b528b5612fb11a6502d7a       ZERO-SIGNAL -> default brookfield
   QC_Tasks/V3_Buckets/QC_Passed/Task4_6a30fe7ec1d692ab3ccad616       ZERO-SIGNAL -> default brookfield
   QC_Tasks/V4_Tasks/QC_False_Fails_PT_Dispute_Accepted/Task1_6a312ac ZERO-SIGNAL -> default brookfield
   QC_Tasks/V4_Tasks/QC_False_Fails_PT_Dispute_Accepted/Task3_6a2b0e6 ZERO-SIGNAL -> default brookfield
   QC_Tasks/V4_Tasks/QC_Non_Fails/Task1_6a3ac526db5033881f6b872d      ZERO-SIGNAL -> default brookfield
   QC_Tasks/V4_Tasks/QC_Passed/Task1_6a26c29d5f5b7cf1ea90c0cc         ZERO-SIGNAL -> default brookfield
   QC_Tasks/V4_Tasks/QC_Passed/Task2_6a27b70a80b7729ca5d6d88d         ZERO-SIGNAL -> default brookfield
   QC_Tasks/V4_Tasks/QC_Passed/Task3_6a2b528b5612fb11a6502d7a         ZERO-SIGNAL -> default brookfield
   QC_Tasks/V4_Tasks/QC_Passed/Task4_6a30fe7ec1d692ab3ccad616         ZERO-SIGNAL -> default brookfield
   Tasks/32_6a3fe578d025d8fbe48a3f99                                  ZERO-SIGNAL -> default brookfield
