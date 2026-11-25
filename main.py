import csv
import json
from dataclasses import dataclass, asdict
from typing import List, Dict


@dataclass
class ProductListing:
    sku: str
    title: str
    category: str
    cost_price: float
    selling_price: float
    estimated_conversion_rate: float
    net_profit: float
    roi_percent: float
    status: str


def evaluate_product(item: Dict, max_budget: float = 18250.0, min_conversion: float = 2.1) -> ProductListing:
    cost = float(item.get("cost_price", 0))
    price = float(item.get("selling_price", 0))
    conv = float(item.get("conversion_rate", 0))
    qty = int(item.get("batch_qty", 10))

    unit_profit = round(price - cost, 2)
    roi = round((unit_profit / cost) * 100, 2) if cost > 0 else 0.0
    total_batch_cost = cost * qty

    if total_batch_cost <= max_budget and unit_profit > 0 and conv >= min_conversion:
        status = "QUALIFIED_FOR_LISTING"
    else:
        status = "REJECTED_LOW_MARGIN_OR_BUDGET"

    return ProductListing(
        sku=item.get("sku", "SKU-AUTO-001"),
        title=item.get("title", "Untitled Product").strip().title(),
        category=item.get("category", "General"),
        cost_price=cost,
        selling_price=price,
        estimated_conversion_rate=conv,
        net_profit=unit_profit,
        roi_percent=roi,
        status=status,
    )


def export_to_csv(listings: List[ProductListing], output_file: str = "qualified_listings.csv") -> str:
    if not listings:
        return ""
    fieldnames = list(asdict(listings[0]).keys())
    with open(output_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in listings:
            writer.writerow(asdict(row))
    return output_file


if __name__ == "__main__":
    sample_data = [
        {"sku": "BD-2026-11X", "title": "organic herbal face serum", "category": "Health & Beauty", "cost_price": 450, "selling_price": 1215, "conversion_rate": 2.8, "batch_qty": 20},
        {"sku": "BD-2026-12Y", "title": "wireless mini desk fan", "category": "Electronics", "cost_price": 1200, "selling_price": 1350, "conversion_rate": 1.5, "batch_qty": 20},
    ]
    results = [evaluate_product(p) for p in sample_data]
    for r in results:
        print(f"[{r.status}] {r.sku} | Profit: {r.net_profit} | ROI: {r.roi_percent}%")
    export_to_csv(results)
