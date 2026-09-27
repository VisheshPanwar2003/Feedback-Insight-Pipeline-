## Task 6: Cluster Interpretation (Centroid Analysis)

**Objective:** Automatically extract human-readable themes from mathematical vector clusters.

**Tech Stack:** Python, `scikit-learn` (Pairwise Distances)

**Key Implementations:**
* **Centroid Calculation:** Computed the exact mathematical center of each K-Means cluster using `kmeans.cluster_centers_`.
* **Representative Extraction:** Utilized `pairwise_distances_argmin_min` to map the geometric centroid back to the closest real customer comment.
* **Automated Summarization:** Successfully summarized large semantic groups into single, representative sentences without requiring LLM API calls.