from django.test import TestCase

from .models import Post

# Create your tests here.

class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Post.objects.create(title='test_title',
                            talework=True,
                            agent='test_agent',
                            # slug='test_slug'
                            ).save()
        # Post.objects.create(link='',
        #                     title='',
        #                     specialization='',
        #                     level='',
        #                     experience='',
        #                     level_english='',
        #                     salary='',
        #                     city='',
        #                     mode_work='',
        #                     size_team='',
        #                     size_company='',
        #                     talework=True,
        #                     agent='',
        #                     description='',
        #                     slug='',
        #                     status='active'
        #                     )

# start test verbose name-----------------------------------------------------------------------------------------------
    def test_title_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

    def test_link_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('link').verbose_name
        self.assertEquals(field_label,'link')

    def test_specialization_label(self):
        author=Post.objects.get(id=1)
        field_label = author._meta.get_field('specialization').verbose_name
        self.assertEquals(field_label,'specialization')

    def test_level_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('level').verbose_name
        self.assertEquals(field_label,'level')

    def test_experience_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('experience').verbose_name
        self.assertEquals(field_label,'experience')

    def test_level_english_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('level_english').verbose_name
        self.assertEquals(field_label,'level english')

    def test_salary_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('salary').verbose_name
        self.assertEquals(field_label,'salary')

    def test_city_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('city').verbose_name
        self.assertEquals(field_label,'city')

    def test_mode_work_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('mode_work').verbose_name
        self.assertEquals(field_label,'mode work')

    def test_size_team_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('size_team').verbose_name
        self.assertEquals(field_label,'size team')

    def test_size_company_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('size_company').verbose_name
        self.assertEquals(field_label,'size company')

    def test_talework_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('talework').verbose_name
        self.assertEquals(field_label,'talework')

    def test_agent_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('agent').verbose_name
        self.assertEquals(field_label, 'agent')

    def test_description_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_slug_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')

    def test_status_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('status').verbose_name
        self.assertEquals(field_label, 'status')

    def test_publish_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('publish').verbose_name
        self.assertEquals(field_label, 'publish')

    def test_tags_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('tags').verbose_name
        self.assertEquals(field_label, 'Tags')
# finish test verbose name----------------------------------------------------------------------------------------------

# start test max length-------------------------------------------------------------------------------------------------
    def test_link_size(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('link').max_length
        self.assertEquals(field_label, 200)

    def test_title_size(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('title').max_length
        self.assertEquals(field_label, 300)

    def test_specialization_size(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('specialization').max_length
        self.assertEquals(field_label, 40)

    def test_level_size(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('level').max_length
        self.assertEquals(field_label, 40)

    def test_experience_size(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('experience').max_length
        self.assertEquals(field_label, 40)

    def test_level_english_size(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('level_english').max_length
        self.assertEquals(field_label, 40)

    def test_salary_size(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('salary').max_length
        self.assertEquals(field_label, 40)

    def test_city_size(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('city').max_length
        self.assertEquals(field_label, 40)

    def test_mode_work_size(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('mode_work').max_length
        self.assertEquals(field_label, 40)

    def test_size_team_size(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('size_team').max_length
        self.assertEquals(field_label, 20)

    def test_size_company_size(self):
        author=Post.objects.get(id=1)
        field_label = author._meta.get_field('size_company').max_length
        self.assertEquals(field_label, 20)

    def test_agent_size(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('agent').max_length
        self.assertEquals(field_label, 100)

    def test_slug_size(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('slug').max_length
        self.assertEquals(field_label, 300)

    def test_status_size(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('status').max_length
        self.assertEquals(field_label, 20)
# finish test max length------------------------------------------------------------------------------------------------

# start test blank------------------------------------------------------------------------------------------------------
    def test_title_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').blank
        self.assertFalse(field_label)

    def test_link_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('link').blank
        self.assertFalse(field_label)

    def test_specialization_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('specialization').blank
        self.assertTrue(field_label)

    def test_level_blank(self):
        author = Post.objects.get(id=1)
        field_label = author._meta.get_field('level').blank
        self.assertTrue(field_label)

    def test_experience_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('experience').blank
        self.assertTrue(field_label)

    def test_level_english_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('level_english').blank
        self.assertTrue(field_label)

    def test_salary_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('salary').blank
        self.assertTrue(field_label)

    def test_city_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('city').blank
        self.assertTrue(field_label)

    def test_mode_work_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('mode_work').blank
        self.assertTrue(field_label)

    def test_size_team_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('size_team').blank
        self.assertTrue(field_label)

    def test_size_company_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('size_company').blank
        self.assertTrue(field_label)

    def test_talework_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('talework').blank
        self.assertFalse(field_label)

    def test_agent_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('agent').blank
        self.assertFalse(field_label)

    def test_description_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('description').blank
        self.assertTrue(field_label)

    def test_slug_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('slug').blank
        self.assertFalse(field_label)

    def test_status_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('status').blank
        self.assertFalse(field_label)

    def test_publish_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('publish').blank
        self.assertTrue(field_label)

    def test_tags_blank(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('tags').blank
        self.assertFalse(field_label)

# finish test blank-----------------------------------------------------------------------------------------------------

# start test get_unique-------------------------------------------------------------------------------------------------
    def test_link_unique(self):
        post = Post.objects.get(id=1)
        field_unique = post._meta.get_field('link').unique
        self.assertTrue(field_unique)

    def test_slug_unique_for_date(self):
        post = Post.objects.get(id=1)
        field_unique = post._meta.get_field('slug').unique_for_date
        self.assertTrue(field_unique)
# finish test unique----------------------------------------------------------------------------------------------------

# start test default----------------------------------------------------------------------------------------------------
    def test_status_default(self):
        post = Post.objects.get(id=1)
        field_unique = post._meta.get_field('status').default
        self.assertEqual(field_unique, 'active')

    def test_talework_dafault(self):
        post = Post.objects.get(id=1)
        field_unique = post._meta.get_field('talework').default
        self.assertIsNone(field_unique)

# finish test default---------------------------------------------------------------------------------------------------

# start test auto_now_add-----------------------------------------------------------------------------------------------
    def test_publish_auto_now_add(self):
        post = Post.objects.get(id=1)
        field_unique = post._meta.get_field('publish').auto_now_add
        self.assertTrue(field_unique)

# finish test auto_now_add----------------------------------------------------------------------------------------------

# start test choices----------------------------------------------------------------------------------------------------
    def test_status_choices(self):
        post = Post.objects.get(id=1)
        field_unique = post._meta.get_field('status').choices
        self.assertEqual(field_unique, (('active', 'Active'),('inactivate', 'Inactivate')))

# finish test choices---------------------------------------------------------------------------------------------------

# start test get_absolute_url-------------------------------------------------------------------------------------------
    def test_get_absolute_url_url(self):
        post = Post.objects.last()
        field_url = post.get_absolute_url()
        self.assertEquals(field_url, '/works/2021/4/29/test_title/1/')
# finish test get_absolute_url------------------------------------------------------------------------------------------

# start test str--------------------------------------------------------------------------------------------------------
    def test_str_title(self):
        post = Post.objects.last()
        field_str = post.__str__()
        self.assertEquals(field_str, 'test_title')
# finish test str-------------------------------------------------------------------------------------------------------

# start test str--------------------------------------------------------------------------------------------------------
    def test_save_slug(self):
        post = Post.objects.get(id=1)
        field_slug = post.slug
        print(field_slug, 'test_title')
# finish test str

if __name__ == '__main__':
    PostModelTest().run()

