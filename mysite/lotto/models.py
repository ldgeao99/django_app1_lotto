from django.db import models
from django.utils import timezone
import random
# Create your models here.

class GuessNumbers(models.Model):  # models 클래스의 자식클래스인 Model을 상속받은 클래스
    name = models.CharField(max_length=24)
    lottos = models.CharField(max_length=255, default='[1,2,3,4,5,6]')
    text = models.CharField(max_length=255)
    num_lotto = models.IntegerField(default=5)
    update_date = models.DateTimeField()

    def generate(self):
        self.lottos=""
        origin = list(range(1,46))
        for _ in range(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) + '\n'
        self.update_date = timezone.now()   # 현재시간을 가져옴
        self.save()                         # 오브젝트를 DB에 저장하는 메소드