import pandas as pd
from analytics.trends import get_monthly_category_trends, identify_critical_issues
from clustering.interpret import get_cluster_representatives
from llm.explain import generate_executive_summary

def run_insight_pipeline():
    print("===========================================")
    print("   🚀 FEEDBACK INSIGHT PIPELINE 🚀")
    print("===========================================\n")
    
    # --- PHASE 1: Quantitative Analysis ---
    print("[1/2] Analyzing Quantitative Trends (SQL + Pandas)...")
    trends = get_monthly_category_trends()
    critical_issues = identify_critical_issues(trends, rating_threshold=3.0)
    
    if critical_issues.empty:
        print(" ✅ No critical issues identified (All average ratings >= 3.0)")
    else:
        print(" ⚠️ CRITICAL ISSUES IDENTIFIED:")
        print("-" * 40)
        print(critical_issues.to_string(index=False))
        print("-" * 40)
        
    # --- PHASE 2: Qualitative Analysis ---
    print("\n[2/2] Extracting Semantic Themes (Vector DB + NLP)...")
    reps_df = get_cluster_representatives(n_clusters=2)
    
    print(" 🗣️ CORE CUSTOMER THEMES (Cluster Centroids):")
    print("-" * 40)
    if not reps_df.empty:
        pd.set_option('display.max_colwidth', None)
        print(reps_df[['Representative_Comment']].to_string(index=False))
    else:
        print(" ❌ No semantic data available.")
    print("-" * 40)
    
    # --- PHASE 3: LLM Synthesis ---
    print("\n[3/3] Generating LLM Executive Summary...")
    summary = generate_executive_summary(critical_issues, reps_df)
    
    print(" 🤖 AI EXECUTIVE INSIGHT:")
    print("-" * 40)
    print(summary)
    print("-" * 40)
    
    print("\n✅ Pipeline Execution Complete.")

if __name__ == "__main__":
    run_insight_pipeline()