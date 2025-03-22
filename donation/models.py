from django.db import models
from django.contrib.auth.models import User
# Create your models here.
blood_types = [
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("O+", "O+"),
    ("O-", "O-")
]
districts_of_bangladesh = [
    ('Bagerhat', 'Bagerhat'), ('Bandarban', 'Bandarban'), ('Barguna', 'Barguna'), ('Barisal', 'Barisal'),
    ('Bhola', 'Bhola'), ('Bogra', 'Bogra'), ('Brahmanbaria', 'Brahmanbaria'), ('Chandpur', 'Chandpur'),
    ('Chapai Nawabganj', 'Chapai Nawabganj'), ('Chattogram', 'Chattogram'), ('Chuadanga', 'Chuadanga'), ("Cox's Bazar", "Cox's Bazar"),
    ('Cumilla', 'Cumilla'), ('Dhaka', 'Dhaka'), ('Dinajpur', 'Dinajpur'), ('Faridpur', 'Faridpur'),
    ('Feni', 'Feni'), ('Gaibandha', 'Gaibandha'), ('Gazipur', 'Gazipur'), ('Gopalganj', 'Gopalganj'),
    ('Habiganj', 'Habiganj'), ('Jamalpur', 'Jamalpur'), ('Jashore', 'Jashore'), ('Jhalokathi', 'Jhalokathi'),
    ('Jhenaidah', 'Jhenaidah'), ('Joypurhat', 'Joypurhat'), ('Khagrachari', 'Khagrachari'), ('Khulna', 'Khulna'),
    ('Kishoreganj', 'Kishoreganj'), ('Kurigram', 'Kurigram'), ('Kushtia', 'Kushtia'), ('Lakshmipur', 'Lakshmipur'),
    ('Lalmonirhat', 'Lalmonirhat'), ('Madaripur', 'Madaripur'), ('Magura', 'Magura'), ('Manikganj', 'Manikganj'),
    ('Meherpur', 'Meherpur'), ('Moulvibazar', 'Moulvibazar'), ('Munshiganj', 'Munshiganj'), ('Mymensingh', 'Mymensingh'),
    ('Naogaon', 'Naogaon'), ('Narail', 'Narail'), ('Narayanganj', 'Narayanganj'), ('Narsingdi', 'Narsingdi'),
    ('Natore', 'Natore'), ('Netrokona', 'Netrokona'), ('Nilphamari', 'Nilphamari'), ('Noakhali', 'Noakhali'),
    ('Pabna', 'Pabna'), ('Panchagarh', 'Panchagarh'), ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'),
    ('Rajbari', 'Rajbari'), ('Rajshahi', 'Rajshahi'), ('Rangamati', 'Rangamati'), ('Rangpur', 'Rangpur'),
    ('Satkhira', 'Satkhira'), ('Shariatpur', 'Shariatpur'), ('Sherpur', 'Sherpur'), ('Sirajganj', 'Sirajganj'),
    ('Sunamganj', 'Sunamganj'), ('Sylhet', 'Sylhet'), ('Tangail', 'Tangail'), ('Thakurgaon', 'Thakurgaon')
]


class DonateBlood(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE)
    bloodType = models.CharField(choices=blood_types,max_length=400)
    date_of_birth = models.DateField()  # Date of birth to check eligibility
    distics = models.CharField(choices=districts_of_bangladesh,null=True,blank=True,max_length=400)
    address = models.TextField()  # Address of the donor
    last_donation_date = models.DateField(null=True, blank=True)  # Last blood donation date
    eligibility = models.BooleanField(default=True)  # Eligibility status
    donation_center = models.CharField(max_length=255)  # Location where the donation will take place
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for the record creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for the last update
    totalRequest = models.IntegerField(null=True,blank=True)
    
    
    def __str__(self):
        return f'{self.user.username} {self.bloodType} {self.distics}'
    


statusType = [
    ('pending','pending'),
    ('Accepted','Accepted')
]

class BloodRequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    DonateBlood  = models.ForeignKey(DonateBlood,null=True,blank=True,on_delete=models.CASCADE)
    numberOfBag = models.IntegerField(null=True,blank=True)
    donateDate = models.DateField(null=True,blank=True)
    place = models.CharField(max_length=200,null=True,blank=True)
    mobile = models.CharField(max_length=12,null=True,blank=True)
    status = models.CharField(choices=statusType,null=True,blank=True,default='pending')
    massage = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.user.username} {self.DonateBlood}'