from django.test import TestCase, Client
from models import BacklogItem
from backlogs.models import Backlog
from django.contrib.auth.models import AnonymousUser, User

from django.core.urlresolvers import reverse
# Create your tests here.
class BacklogItemViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='carl',
            email='carl.bednorz@gmail.com',
            password='super_secret_password'
        )

        self.name = "My first Backlog with User Stories"
        self.description = "That is the description for my Backlog. It's optional tough."
        self.short_id = "FRNKN"
        self.backlog = Backlog.objects.create(
            user=self.user,
            name=self.name,
            description=self.description,
            short_id=self.short_id
        )

        self.who = "Product Manager"
        self.what = "create a backlog item"
        self.why = "I can write down a user story for my requirement"
        self.acceptance_criteria = "* Product Manager is logged in"
        self.notes = "***Needs breakdown***"

        self.story_points = 5
        self.business_value = 150

        self.backlog_item = BacklogItem.objects.create(
            user=self.user,
            backlog=self.backlog,
            who=self.who,
            what=self.what,
            why=self.why,
            acceptance_criteria=self.acceptance_criteria,
            notes=self.notes,
            story_points=self.story_points,
            business_value=self.business_value
        )

        self.client = Client()

    def test_backlog_item_update_view(self):
        """
        Tests the update view for updating a backlog item
        """
        response = self.client.get(reverse('backlog_item_update_view', kwargs={'backlog_item_uuid':self.backlog_item.uuid}))

        self.assertEqual(response.status_code, 302)

    def test_backlog_item_create_view(self):
        """
        Tests the create view of a backlog item
        """
        response = self.client.get(reverse('backlog_item_create_view', kwargs={'backlog_uuid':self.backlog.uuid}))

        self.assertEqual(response.status_code, 302)


    """
    def test_backlog_item_view(self):
        response = self.client.get('/backlog/item/333')
        self.assertEqual(response.status_code, 555)
    """

class BacklogItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='carl',
            email='carl.bednorz@gmail.com',
            password='super_secret_password'
        )

        self.name = "My first Backlog with User Stories"
        self.description = "That is the description for my Backlog. It's optional tough."
        self.short_id = "FRNKN"
        self.backlog = Backlog.objects.create(
            user=self.user,
            name=self.name,
            description=self.description,
            short_id=self.short_id
        )

        self.who = "Product Manager"
        self.what = "create a backlog item"
        self.why = "I can write down a user story for my requirement"
        self.acceptance_criteria = "* Product Manager is logged in"
        self.notes = "***Needs breakdown***"

        self.story_points = 5
        self.business_value = 150

        self.backlog_item = BacklogItem.objects.create(
            user=self.user,
            backlog=self.backlog,
            who=self.who,
            what=self.what,
            why=self.why,
            acceptance_criteria=self.acceptance_criteria,
            notes=self.notes,
            story_points=self.story_points,
            business_value=self.business_value
        )


    def tearDown(self):
        pass

    def test_backlog_item_model(self):
        """
        Tests the creation of a backlog item.
        """
        bi = BacklogItem.objects.get(id=self.backlog_item.id)

        self.assertEqual("As a Product Manager I'd like to create a backlog item, so that I can write down a user story for my requirement.", bi.get_user_story())
        self.assertTrue(bi)
        self.assertEqual(self.user, bi.user)
        self.assertEqual(self.backlog, bi.backlog)
        self.assertEqual(self.who, bi.who)
        self.assertEqual(self.what, bi.what)
        self.assertEqual(self.why, bi.why)
        self.assertEqual(self.acceptance_criteria, bi.acceptance_criteria)
        self.assertEqual(self.notes, bi.notes)
        self.assertEqual(self.story_points, bi.story_points)
        self.assertEqual(self.business_value, bi.business_value)
        self.assertTrue(bi.created_on)
        self.assertTrue(bi.updated_on)
        self.assertEqual(bi.sequence_increment, 0)
        self.assertTrue(bi.item_short_id)
        self.assertEqual(bi.backlog.short_id + "-" + str(bi.sequence_increment), bi.item_short_id)


    def test_short_id(self):
        """
        User creates 3 items, deletes the third one.
        The system handles internal sequence ids correctly.
        """
        backlog_item_1 = BacklogItem.objects.create(
            user=self.user,
            backlog=self.backlog,
            who=self.who,
            what=self.what,
            why=self.why,
            acceptance_criteria=self.acceptance_criteria,
            notes=self.notes,
            story_points=self.story_points,
            business_value=self.business_value
        )

        backlog_item_2 = BacklogItem.objects.create(
            user=self.user,
            backlog=self.backlog,
            who=self.who,
            what=self.what,
            why=self.why,
            acceptance_criteria=self.acceptance_criteria,
            notes=self.notes,
            story_points=self.story_points,
            business_value=self.business_value
        )

        backlog_item_3 = BacklogItem.objects.create(
            user=self.user,
            backlog=self.backlog,
            who=self.who,
            what=self.what,
            why=self.why,
            acceptance_criteria=self.acceptance_criteria,
            notes=self.notes,
            story_points=self.story_points,
            business_value=self.business_value
        )

        self.assertEqual(backlog_item_1.sequence_increment, 1)
        self.assertEqual(backlog_item_2.sequence_increment, 2)
        self.assertEqual(backlog_item_3.sequence_increment, 3)

        backlog_item_3.delete()

        backlog_item_4= BacklogItem.objects.create(
            user=self.user,
            backlog=self.backlog,
            who=self.who,
            what=self.what,
            why=self.why,
            acceptance_criteria=self.acceptance_criteria,
            notes=self.notes,
            story_points=self.story_points,
            business_value=self.business_value
        )

        self.assertEqual(backlog_item_4.sequence_increment, 3)
