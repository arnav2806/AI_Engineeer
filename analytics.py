from typing import List, Dict

def analyze_purchases(amounts: List[float], threshold: float) -> Dict[str, float]:
    total = sum(amounts)
    avg = total / len(amounts) if amounts else 0.0
    count_above = sum(1 for x in amounts if x > threshold)
    return {"total": total, "avg": avg, "count_above": count_above}

def sort_items_by_cost(records: List[Dict]) -> List[Dict]:
    return sorted(records, key=lambda r: r.get("total_cost", 0), reverse=True)
