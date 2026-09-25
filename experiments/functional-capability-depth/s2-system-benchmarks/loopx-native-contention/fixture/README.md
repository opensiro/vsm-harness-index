# Frozen contention fixture

This fixture exists only for the preregistered LoopX native-S2 study.

The baseline intentionally implements neither Task A nor Task B. Both tasks are independently useful and both require editing `src/dispatch.py`, creating a known semantic write-surface overlap before any experimental result is observed.

The task-specific acceptance tests therefore fail against the untouched baseline by design. Do not add them to repository-wide test discovery or treat baseline failure as a repository defect.

During execution, each worker receives only its assigned task instruction. The experiment records how the native LoopX coordination path handles the predeclared overlap before judging the integrated result with both acceptance tests.
