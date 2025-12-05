from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from core.models import Bank, Branch

class BankBranchAPITestCase(APITestCase):

    def setUp(self):
        # Create banks
        self.bank1 = Bank.objects.create(name="Test Bank 1")
        self.bank2 = Bank.objects.create(name="Test Bank 2")

        # Create branches
        self.branch1 = Branch.objects.create(
            bank=self.bank1,
            branch="Main Branch",
            ifsc="TEST0001",
            address="Address 1",
            city="City 1",
            district="District 1",
            state="State 1"
        )
        self.branch2 = Branch.objects.create(
            bank=self.bank1,
            branch="Second Branch",
            ifsc="TEST0002",
            address="Address 2",
            city="City 2",
            district="District 2",
            state="State 2"
        )

    def test_bank_list_endpoint(self):
        """
        Test /api/banks/ returns all banks
        """
        url = reverse('bank-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], "Test Bank 1")

    def test_branch_list_endpoint(self):
        """
        Test /api/branches/ returns all branches
        """
        url = reverse('branch-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['ifsc'], "TEST0001")

    def test_branch_search_endpoint(self):
        """
        Test /api/branches/search/?ifsc=TEST0001 returns the correct branch
        """
        url = reverse('branch-search')
        response = self.client.get(url, {'ifsc': 'TEST0001'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['branch'], "Main Branch")
