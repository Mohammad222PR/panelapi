from django.test import TestCase
from .models import Color, DeviceTypes, CartTypes, BusInformation, Comment

class BusInformationTestCase(TestCase):
    def setUp(self):
        # Create objects required for the ForeignKey relationships
        self.device_color = Color.objects.create(name='Test Color')
        self.device_type = DeviceTypes.objects.create(name='Test Device Type')
        self.car_type = CartTypes.objects.create(name='Test Car Type')

    def test_bus_information_creation(self):
        bus_info = BusInformation.objects.create(
            device_color=self.device_color,
            device_type=self.device_type,
            plaque='ABC123',
            car_name='Test Car',
            name_car_owner='Test Owner',
            capacity_number='10 passengers',
            car_type=self.car_type,
            granny=False,
            cooling=True,
            cost=100.00,
            date='2023-01-01',
            origin='Test Origin',
            destination='Test Destination',
            service_date='2023-01-02',
            entity='08:00',
            time_destination='12:00',
            service_company_name='Test Company',
            is_public=True,
        )

        self.assertEqual(bus_info.device_color, self.device_color)
        self.assertEqual(bus_info.device_type, self.device_type)
        self.assertEqual(bus_info.plaque, 'ABC123')
        self.assertEqual(bus_info.car_name, 'Test Car')
        self.assertEqual(bus_info.name_car_owner, 'Test Owner')
        self.assertEqual(bus_info.capacity_number, '10 passengers')
        self.assertEqual(bus_info.car_type, self.car_type)
        self.assertFalse(bus_info.granny)
        self.assertTrue(bus_info.cooling)
        self.assertEqual(bus_info.cost, 100.00)
        self.assertEqual(bus_info.date, '2023-01-01')
        self.assertEqual(bus_info.origin, 'Test Origin')
        self.assertEqual(bus_info.destination, 'Test Destination')
        self.assertEqual(bus_info.service_date, '2023-01-02')
        self.assertEqual(bus_info.entity, '08:00')
        self.assertEqual(bus_info.time_destination, '12:00')
        self.assertEqual(bus_info.service_company_name, 'Test Company')
        self.assertTrue(bus_info.is_public)

class CommentTestCase(TestCase):
    def setUp(self):
        # Create a BusInformation object for testing the ForeignKey relationship
        self.bus_info = BusInformation.objects.create(
            device_color=Color.objects.create(name='Test Color'),
            device_type=DeviceTypes.objects.create(name='Test Device Type'),
            plaque='ABC123',
            car_name='Test Car',
            name_car_owner='Test Owner',
            capacity_number='10 passengers',
            car_type=CartTypes.objects.create(name='Test Car Type'),
            granny=False,
            cooling=True,
            cost=100.00,
            date='2023-01-01',
            origin='Test Origin',
            destination='Test Destination',
            service_date='2023-01-02',
            entity='08:00',
            time_destination='12:00',
            service_company_name='Test Company',
            is_public=True,
        )

    def test_comment_creation(self):
        comment = Comment.objects.create(
            car_post=self.bus_info,
            name='Test Commenter Name',
            body='Test Comment Body',
            parent=None,
        )

        self.assertEqual(comment.car_post, self.bus_info)
        self.assertEqual(comment.name, 'Test Commenter Name')
        self.assertEqual(comment.body, 'Test Comment Body')
        self.assertIsNone(comment.parent)

    def test_comment_with_parent_creation(self):
        parent_comment = Comment.objects.create(
            car_post=self.bus_info,
            name='Parent Commenter',
            body='Parent Comment Body',
            parent=None,
        )

        child_comment = Comment.objects.create(
            car_post=self.bus_info,
            name='Child Commenter',
            body='Child Comment Body',
            parent=parent_comment,
        )

        self.assertEqual(child_comment.parent, parent_comment)

    def test_comment_str_representation(self):
        comment = Comment.objects.create(
            car_post=self.bus_info,
            name='Test Commenter Name',
            body='Test Comment Body',
            parent=None,
        )

        self.assertEqual(str(comment), 'Test Commenter Name')
