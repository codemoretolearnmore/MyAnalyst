import unittest
from ..services.text_to_tables import process_text_to_tables
from ..services.text_to_query import process_text_to_query
from ..services.query_to_metrics import process_query_to_metrics
from ..services.metrics_to_insights import process_metrics_to_insights

class TestServices(unittest.TestCase):
    def test_text_to_tables(self):
        response = process_text_to_tables("test_1234", "Get sales data")
        self.assertIn("tables", response)

    def test_text_to_query(self):
        response = process_text_to_query("test_1234", ["sales"])
        self.assertIn("query", response)

    def test_query_to_metrics(self):
        response = process_query_to_metrics("test_1234", "SELECT * FROM sales")
        self.assertIn("total_sales", response)

    def test_metrics_to_insights(self):
        response = process_metrics_to_insights("test_1234", {"total_sales": 50000})
        self.assertIn("insight", response)

if __name__ == "__main__":
    unittest.main()
