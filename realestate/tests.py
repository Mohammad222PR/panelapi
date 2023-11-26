from django.test import TestCase
from .models import PropertyInformation, State, City, PropertyModel, TypeFloorProperty, PropertyType, PropertyPossibilities, HeatingSystemProperty, CoolingSystemProperty, SelectionSans, KitchenEquipment, WelfarePossibilities, EntertainmentPossibilities, OtherSpacesResidence, EnvironmentalContext, BedCount, RoomPossibilities, TypeOwnership

class PropertyInformationTestCase(TestCase):
    def setUp(self):
        # Create some required related objects
        self.state = State.objects.create(name='Test State')
        self.city = City.objects.create(name='Test City')
        self.property_model = PropertyModel.objects.create(name='Test Model')
        self.type_floor_property = TypeFloorProperty.objects.create(name='Test Type Floor')
        self.property_type = PropertyType.objects.create(name='Test Property Type')
        self.heating_system_property = HeatingSystemProperty.objects.create(name='Test Heating System')
        self.cooling_system = CoolingSystemProperty.objects.create(name='Test Cooling System')
        self.selection_sans = SelectionSans.objects.create(name='Test Selection Sans')
        self.kitchen_equipment = KitchenEquipment.objects.create(name='Test Kitchen Equipment')
        self.welfare_possibilities = WelfarePossibilities.objects.create(name='Test Welfare Possibilities')
        self.entertainment_possibilities = EntertainmentPossibilities.objects.create(name='Test Entertainment Possibilities')
        self.other_spaces_residence = OtherSpacesResidence.objects.create(name='Test Other Spaces Residence')
        self.environmental_context = EnvironmentalContext.objects.create(name='Test Environmental Context')
        self.bed_count = BedCount.objects.create(name='Test Bed Count')
        self.room_possibilities = RoomPossibilities.objects.create(name='Test Room Possibilities')
        self.type_ownership = TypeOwnership.objects.create(name='Test Type Ownership')

    def test_property_information_creation(self):
        property_info = PropertyInformation.objects.create(
            user_id=1,
            owner_name='Test Owner Name',
            state=self.state,
            city=self.city,
            property_address='Test Address',
            post_card=123456,
            property_phone=7890123456,
            name_property_owner='Test Property Owner',
            phone_property_manager=9876543210,
            phone_property=1234567890,
            square_footage_property=100,
            about_property='Test About Property',
            created_at_property='2023-01-01',
            villa_registration_rules='Test Villa Rules',
            capacity_property='Test Capacity',
            lease_date='2023-01-01',
            property_image='test_image.jpg',
            property_image2='test_image2.jpg',
            property_image3='test_image3.jpg',
            property_image4='test_image4.jpg',
            enter_limit='08:00',
            exit_limit='20:00',
            property_model=self.property_model,
            type_floor_property=self.type_floor_property,
            property_type=self.property_type,
            heating_system_property=self.heating_system_property,
            cooling_system=self.cooling_system,
            parking_count=2,
            classes=1,
            image='test_bills_image.jpg',
            selection_sans=self.selection_sans,
            lease_price=1000,
            property_number=987654321,
            days_booking='Mon, Tue, Wed',
            shaba_number=123456789012345678901234,
            cart_number=1234567890123456,
            account_number=1234567890123456,
            melli_cart='test_melli_cart.jpg',
            discount=False,
            residence_rules='Test Residence Rules',
            cancel_request='Test Cancel Request Rules',
            kitchen_equipment=[self.kitchen_equipment],
            entertainment_possibilities=[self.entertainment_possibilities],
            enter_time='08:00',
            exit_time='12:00',
            minimum_stay_limit='2',
            maximum_stay_limit='5',
            welfare_possibilities=[self.welfare_possibilities],
            other_spaces_residence=[self.other_spaces_residence],
            environmental_context=self.environmental_context,
            room_title='Test Room Title',
            slug='test-room',
            bed_count=self.bed_count,
            room_possibilities=[self.room_possibilities],
            type_ownership=self.type_ownership,
            is_public=True,
            is_reserve=True,
        )

        self.assertEqual(property_info.user_id, 1)
        # Add more assertions for other fields as needed
