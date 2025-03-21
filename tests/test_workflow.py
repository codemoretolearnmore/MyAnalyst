import unittest
from ..services.workflow import start_workflow

class TestWorkflow(unittest.TestCase):
    def test_workflow_execution(self):
        request_id = "test_1234"
        prompt = "Get sales data"
        response = start_workflow(request_id, prompt)
        self.assertEqual(response["status"], "success")

if __name__ == "__main__":
    unittest.main()