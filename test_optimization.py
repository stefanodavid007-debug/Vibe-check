import unittest
import main

class TestOptimization(unittest.TestCase):
    def test_results_consistency(self):
        # We need to re-run the logic but capture results
        db = main.Database()
        items = [type('Item', (), {'id': i}) for i in range(10)]

        # Optimized logic
        item_ids = [item.id for item in items]
        all_details = db.query_multiple(item_ids)
        results = []
        for item in items:
            details = all_details.get(item.id)
            results.append(details)

        # Baseline logic comparison
        db_baseline = main.Database()
        baseline_results = []
        for item in items:
            baseline_results.append(db_baseline.query(item.id))

        self.assertEqual(results, baseline_results)
        self.assertEqual(db.query_count, 1)
        self.assertEqual(db_baseline.query_count, 10)

if __name__ == "__main__":
    unittest.main()
