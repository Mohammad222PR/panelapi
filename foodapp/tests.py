from django.test import TestCase
from realestate.models import State
from account.models import User
from .models import CookType, FoodInformation, Comment

class CookTypeModelTest(TestCase):
    def test_cook_type_str(self):
        cook_type = CookType.objects.create(name="Test Cook Type")
        self.assertEqual(str(cook_type), "Test Cook Type")

class FoodInformationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="testuser")
        state = State.objects.create(name="Test State")
        cook_type = CookType.objects.create(name="Test Cook Type")
        FoodInformation.objects.create(
            user=user,
            number=123,
            state=state,
            address="Test Address",
            how_much_cook=3,
            what_can_cook=cook_type,
            date_cook="Test Date",
            time_cook="10:00:00",
            master_chef_name="Test Master Chef",
            chef_name="Test Chef",
            point=4,
            is_public=True
        )

    def test_food_information_str(self):
        food_info = FoodInformation.objects.get(id=1)
        self.assertEqual(str(food_info), "Test Address")

class CommentModelTest(TestCase):
    def test_comment_str(self):
        food_info = FoodInformation.objects.create(
            user=User.objects.create(username="testuser"),
            number=123,
            state=State.objects.create(name="Test State"),
            address="Test Address",
            how_much_cook=3,
            what_can_cook=CookType.objects.create(name="Test Cook Type"),
            date_cook="Test Date",
            time_cook="10:00:00",
            master_chef_name="Test Master Chef",
            chef_name="Test Chef",
            point=4,
            is_public=True
        )

        comment = Comment.objects.create(
            food_post=food_info,
            name="Test Commenter",
            body="Test Comment Body"
        )

        self.assertEqual(str(comment), "Test Commenter")
