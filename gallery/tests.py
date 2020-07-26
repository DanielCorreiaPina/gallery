from django.test import TestCase

# Tentei escrever um teste, mas não fui bem sucedido por falta de tempo
""" from PIL import Image as Img

from .models import Image

class ImageModelTests(TestCase):

    def test_file_was_deleted_from_the_system(self):
        #Verifies if a file is deleted from the system when using the delete() method
        size = (200, 200)
        color = (255, 0, 0)
        img_test = Img.new("RGBA", size, color)
        img_io = io.BytesIO()
        img_test.save(img_io,format='png')
        img = Image.objects.create(title='test', image=img_test)
        
        img.save()
        path = img.image
        img.delete()
        self.assertIs(os.path.exists(path), False) """