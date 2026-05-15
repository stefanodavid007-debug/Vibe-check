from src.database import Database
import time

def run_unoptimized():
    db = Database()
    print("--- Running Unoptimized (N+1) ---")
    start_time = time.time()

    products = db.get_products() # 1 query

    product_details = []
    for p_id, p_name, cat_id in products:
        cat_name = db.get_category_name(cat_id) # N queries!
        product_details.append({
            "id": p_id,
            "name": p_name,
            "category": cat_name
        })

    end_time = time.time()
    print(f"Processed {len(product_details)} products.")
    print(f"Total Database Queries: {db.query_count}")
    print(f"Execution Time: {end_time - start_time:.4f} seconds\n")

def run_optimized():
    db = Database()
    print("--- Running Optimized (Eager Loading) ---")
    start_time = time.time()

    products = db.get_products() # 1 query

    # Eager load categories
    category_ids = {p[2] for p in products}
    categories_map = db.get_categories_batch(category_ids) # 1 query

    product_details = []
    for p_id, p_name, cat_id in products:
        cat_name = categories_map.get(cat_id)
        product_details.append({
            "id": p_id,
            "name": p_name,
            "category": cat_name
        })

    end_time = time.time()
    print(f"Processed {len(product_details)} products.")
    print(f"Total Database Queries: {db.query_count}")
    print(f"Execution Time: {end_time - start_time:.4f} seconds\n")

if __name__ == "__main__":
    run_unoptimized()
    run_optimized()
