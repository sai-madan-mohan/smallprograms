
add = lambda a, b: a + b
print(add(5, 3))  # Output: 8

square = lambda x: x * x
print(square(4))  # Output: 16

pairs = [(1, 5), (3, 1), (10, 2)]
pairs.sort(key=lambda x: x[1])
print(pairs)  # Output: [(3, 1), (10, 2), (1, 5)]

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]

print(add(9,10))

print(square(6))

class FunnelLearningGoal(CommonTimeStamp):
    title = models.CharField(max_length=64, verbose_name=u"Laerning Goal Title")
    is_active = models.BooleanField(default=True)
    order_by = models.IntegerField(null=True, blank=True, verbose_name="Order By")
    class Meta:
        verbose_name = u"Funnel Learning Goal"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return '%s' % (self.title, )
    def __str__(self):
        return '%s' % (self.title, )