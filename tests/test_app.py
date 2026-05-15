import unittest
from src.database import Database

class TestApp(unittest.TestCase):
    def test_optimized_vs_unoptimized_consistency(self):
        db = Database()
        products = db.get_products()

        # Unoptimized
        results_unopt = []
        for p_id, p_name, cat_id in products:
            results_unopt.append(db.get_category_name(cat_id))

        # Optimized
        category_ids = {p[2] for p in products}
        categories_map = db.get_categories_batch(category_ids)
        results_opt = [categories_map.get(p[2]) for p in products]

        self.assertEqual(results_unopt, results_opt)

if __name__ == "__main__":
    unittest.main()
